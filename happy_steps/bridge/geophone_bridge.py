"""
geophone_bridge.py — stream a geophone into the web prototype (index.html).

Run it on the computer the sensor is plugged into, then open the page,
choose "Live sensor" and press Connect (default ws://localhost:8765).

    pip install websockets numpy scipy pyserial

Three ways to feed it:

    # 1) real sensor: a microcontroller (Arduino / ESP32 / Pico) reads the
    #    geophone through an amplifier + ADC and prints ONE integer per line
    python geophone_bridge.py --serial /dev/ttyUSB0 --baud 500000 --fs 1000

    # 2) replay one of your .mat recordings in real time (geo_data, 8 kHz)
    python geophone_bridge.py --mat Aayushi_wooden_3.mat --fs-in 8000

    # 3) no hardware: synthetic footsteps, to test the connection
    python geophone_bridge.py --sim

Messages sent to the page (JSON, one per WebSocket message):
    {"type": "meta",  "fs": 2000, "source": "..."}
    {"type": "chunk", "b64": "<little-endian int16 samples, base64>"}

Note: a page served over https (GitHub Pages) may connect to ws://localhost,
but not to ws://<another-machine>. To use a Raspberry Pi on your network,
run this script on the Pi and open the page on the Pi, or put the bridge
behind wss:// (TLS).
"""
import argparse, asyncio, base64, json, time
import numpy as np

CHUNK_S = 0.05          # send 50 ms at a time
FS_OUT = 2000           # rate used by the page for recordings


def to_b64(x, scale):
    q = np.clip(np.round(x / scale * 32767), -32768, 32767).astype("<i2")
    return base64.b64encode(q.tobytes()).decode("ascii")


# ---------------- sources: each yields (fs, generator of float chunks) -------
def mat_source(path, fs_in, mains):
    import scipy.io as sio
    from scipy.signal import decimate, iirnotch, filtfilt
    x = sio.loadmat(path)["geo_data"].ravel().astype(np.float64)
    x -= x.mean()
    q = max(1, fs_in // FS_OUT)
    y = decimate(x, q, ftype="fir", zero_phase=True) if q > 1 else x
    fs = fs_in // q
    if mains:
        for h in range(mains, fs // 2, mains):
            b, a = iirnotch(h, Q=30, fs=fs)
            y = filtfilt(b, a, y)
    scale = float(np.max(np.abs(y))) or 1.0
    n = int(CHUNK_S * fs)

    def gen():
        while True:                      # loop the recording
            for i in range(0, len(y) - n, n):
                yield y[i:i + n]
    return fs, scale, gen(), f"replay of {path}"


def sim_source(fs=2000):
    rng = np.random.default_rng(0)
    n = int(CHUNK_S * fs)
    t = np.arange(int(0.5 * fs)) / fs
    step = np.exp(-t / 0.06) * np.sin(2 * np.pi * 45 * t) + 0.4 * np.exp(-t / 0.03) * np.sin(2 * np.pi * 110 * t)

    def gen():
        buf = np.zeros(fs * 4)
        pos, nxt, walking_until = 0, int(0.3 * fs), 0
        while True:
            out = rng.normal(0, 0.01, n)
            for k in range(n):
                g = pos + k
                if g == nxt:
                    if g > walking_until + 3 * fs:     # start a new walk
                        walking_until = g + int(rng.uniform(6, 14) * fs)
                    if g < walking_until:
                        buf[: len(step)] += step * rng.uniform(.8, 1.2)
                        nxt = g + int(rng.normal(0.52, 0.02) * fs)
                    else:
                        nxt = g + int(3.5 * fs)
                out[k] += buf[0]
                buf = np.roll(buf, -1); buf[-1] = 0
            pos += n
            yield out
    return fs, 1.5, gen(), "synthetic footsteps"


def serial_source(port, baud, fs):
    import serial
    ser = serial.Serial(port, baud, timeout=1)
    n = int(CHUNK_S * fs)
    state = {"mean": None, "peak": 1.0}

    def gen():
        chunk = []
        while True:
            line = ser.readline().strip()
            try:
                chunk.append(float(line))
            except ValueError:
                continue
            if len(chunk) >= n:
                x = np.asarray(chunk); chunk = []
                m = x.mean() if state["mean"] is None else 0.99 * state["mean"] + 0.01 * x.mean()
                state["mean"] = m
                x = x - m
                state["peak"] = max(state["peak"] * 0.9995, float(np.max(np.abs(x))) or 1.0)
                yield x / state["peak"]
    return fs, 1.0, gen(), f"serial {port}"


# ---------------- server ------------------------------------------------------
async def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--serial"); g.add_argument("--mat"); g.add_argument("--sim", action="store_true")
    ap.add_argument("--baud", type=int, default=500000)
    ap.add_argument("--fs", type=int, default=1000, help="sample rate of the serial stream")
    ap.add_argument("--fs-in", type=int, default=8000, help="sample rate of the .mat file")
    ap.add_argument("--mains", type=int, default=50, help="notch power-line hum (0 = off)")
    ap.add_argument("--port", type=int, default=8765)
    a = ap.parse_args()

    if a.mat:
        fs, scale, gen, name = mat_source(a.mat, a.fs_in, a.mains)
    elif a.serial:
        fs, scale, gen, name = serial_source(a.serial, a.baud, a.fs)
    else:
        fs, scale, gen, name = sim_source()

    import websockets
    clients = set()

    async def handler(ws):
        clients.add(ws)
        await ws.send(json.dumps({"type": "meta", "fs": fs, "source": name}))
        try:
            await ws.wait_closed()
        finally:
            clients.discard(ws)

    async def pump():
        t0, sent = time.perf_counter(), 0
        loop = asyncio.get_running_loop()
        while True:
            x = await loop.run_in_executor(None, next, gen) if a.serial else next(gen)
            msg = json.dumps({"type": "chunk", "b64": to_b64(x, scale)})
            for c in list(clients):
                try:
                    await c.send(msg)
                except Exception:
                    clients.discard(c)
            sent += len(x)
            if not a.serial:                       # pace replay/sim in real time
                wait = t0 + sent / fs - time.perf_counter()
                if wait > 0:
                    await asyncio.sleep(wait)

    async with websockets.serve(handler, "0.0.0.0", a.port):
        print(f"Streaming {name} at {fs} Hz on ws://localhost:{a.port}  (Ctrl+C to stop)")
        await pump()


if __name__ == "__main__":
    asyncio.run(main())
