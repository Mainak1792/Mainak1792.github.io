"""
prepare_data.py — turn geophone .mat recordings into the data files used by
index.html (the footstep web page).

Folder layout (next to this script):

    data/
      environment/        (the misspelling "enviroment" also works)
        e1/  *.mat
        e2/  *.mat
        e3/  *.mat
      gender/
        male/    *.mat
        female/  *.mat

Run:
    python prepare_data.py

Output:
    assets/environment.js
    assets/gender.js

Upload index.html + assets/ to GitHub. Never upload data/ (raw recordings);
the .gitignore in this project already excludes it.

Kaggle: set DATA_DIR to your input dataset (e.g. "/kaggle/input/footsteps/data")
and OUT_DIR to "/kaggle/working/assets", then download the assets folder.
"""
import base64
import glob
import json
import os

import numpy as np
from scipy.io import loadmat
from scipy.signal import decimate, filtfilt, find_peaks, iirnotch, welch

# ----------------------------------------------------------------- settings
DATA_DIR = "data"          # raw .mat files
OUT_DIR = "assets"         # generated files read by index.html
FS_IN = 8000               # geophone sampling rate of the .mat files (Hz)
DECIM = 4                  # 8000 -> 2000 Hz (footstep energy is < 400 Hz)
START_SECONDS = 0          # skip this much at the start of each recording
MAX_SECONDS = 120          # length kept per recording (page size ~0.65 MB each)
MAINS_HZ = 50              # remove power-line hum + harmonics (India: 50); None to skip
VAR_NAME = "geo_data"      # variable inside the .mat; falls back to the largest array

# What the audience sees. "label" is always shown; "detail" is hidden in
# blind-listening mode. "file" is optional: without it the first .mat file
# (alphabetically) in the folder is used.
GROUPS = {
    "environment": dict(
        title="Two Different floors",
        intro="Footsteps recorded on three different floors. "
              "Listen to how much the floor itself changes the sound.",
        folders=[
            dict(folder="e1", label="Floor 1", detail="Wooden Floor"),
            dict(folder="e2", label="Floor 2", detail="Carpetted Floor"),
            # dict(folder="e3", label="Floor 3", detail="Environment 3 (edit in prepare_data.py)"),
        ],
    ),
    "gender": dict(
        title="Two walkers",
        intro="Two people walking. Can you tell who is who from the floor alone?",
        folders=[
            dict(folder="female", label="Walker 1", detail="Female walker"),
            dict(folder="male",   label="Walker 2", detail="Male walker"),
        ],
    ),
}
GROUP_DIR_ALIASES = {"environment": ["environment", "enviroment", "environments"]}


# ---------------------------------------------------------------- helpers
def find_group_dir(key):
    if not os.path.isdir(DATA_DIR):
        return None
    names = {n.lower(): n for n in os.listdir(DATA_DIR)}
    for alias in GROUP_DIR_ALIASES.get(key, [key]):
        if alias.lower() in names:
            return os.path.join(DATA_DIR, names[alias.lower()])
    return None


def find_sub_dir(parent, name):
    names = {n.lower(): n for n in os.listdir(parent)}
    n = names.get(name.lower())
    return os.path.join(parent, n) if n else None


def load_signal(path):
    """Return a 1-D float array from a .mat file (v5 or v7.3)."""
    try:
        m = loadmat(path)
        arrays = {k: v for k, v in m.items()
                  if not k.startswith("__") and isinstance(v, np.ndarray)
                  and np.issubdtype(v.dtype, np.number)}
    except NotImplementedError:          # MATLAB v7.3 = HDF5
        import h5py
        with h5py.File(path, "r") as f:
            arrays = {k: np.array(f[k]) for k in f.keys()
                      if isinstance(f[k], h5py.Dataset)}
    if not arrays:
        raise ValueError(f"no numeric array found in {path}")
    key = VAR_NAME if VAR_NAME in arrays else max(arrays, key=lambda k: arrays[k].size)
    x = np.asarray(arrays[key], dtype=np.float64)
    if x.ndim > 1:                        # take the longest axis, first channel
        x = np.moveaxis(x, int(np.argmax(x.shape)), 0).reshape(x.shape[int(np.argmax(x.shape))], -1)[:, 0]
    return x, key


def process(path, meta):
    x, key = load_signal(path)
    x = x[int(START_SECONDS * FS_IN): int((START_SECONDS + MAX_SECONDS) * FS_IN)]
    if len(x) < FS_IN * 2:
        raise ValueError(f"{path}: fewer than 2 s of data after trimming")

    peak_raw = np.max(np.abs(x))
    clip_frac = float(np.mean(np.abs(x) >= 0.999 * peak_raw)) if peak_raw > 0 else 0.0

    x = x - np.mean(x)
    y = decimate(x, DECIM, ftype="fir", zero_phase=True)
    fs = FS_IN // DECIM
    if MAINS_HZ:
        for h in range(MAINS_HZ, fs // 2, MAINS_HZ):
            b, a = iirnotch(h, Q=30, fs=fs)
            y = filtfilt(b, a, y)

    # footstep detection: 30 ms RMS envelope, robust threshold, >= 0.3 s apart
    win = int(0.03 * fs)
    env = np.sqrt(np.convolve(y * y, np.ones(win) / win, mode="same"))
    med = np.median(env)
    mad = np.median(np.abs(env - med)) + 1e-12
    peaks, _ = find_peaks(env, height=med + 8 * mad, distance=int(0.3 * fs))
    isi = np.diff(peaks) / fs
    walking = isi[(isi > 0.3) & (isi < 1.2)]
    cadence = 60.0 / float(np.median(walking)) if len(walking) else 0.0

    f, p = welch(y, fs=fs, nperseg=4096)
    band = (f > 5) & (f < 400)
    dom_f = float(f[band][np.argmax(p[band])])

    scale = float(np.max(np.abs(y))) or 1.0
    q = np.clip(np.round(y / scale * 32767), -32768, 32767).astype("<i2")
    rec = dict(
        id=meta["folder"], label=meta["label"], detail=meta["detail"],
        fs=fs, scale=scale, n=int(len(q)),
        steps=[int(i) for i in peaks],
        cadence=round(cadence, 1), dominantHz=round(dom_f, 1),
        clipFraction=clip_frac if clip_frac > 1e-4 else 0.0,
        b64=base64.b64encode(q.tobytes()).decode("ascii"),
    )
    print(f"  {meta['folder']:>8}: {os.path.basename(path)} [{key}]  "
          f"{len(peaks)} steps, {cadence:.0f} steps/min, peak {dom_f:.0f} Hz"
          + (f", {clip_frac*100:.2f}% clipped" if rec["clipFraction"] else ""))
    return rec


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    made = 0
    for key, g in GROUPS.items():
        gdir = find_group_dir(key)
        out_path = os.path.join(OUT_DIR, f"{key}.js")
        if gdir is None:
            print(f"[{key}] folder not found in {DATA_DIR}/ — skipped")
            continue
        print(f"[{key}] {gdir}")
        recs = []
        for meta in g["folders"]:
            sub = find_sub_dir(gdir, meta["folder"])
            if sub is None:
                print(f"  {meta['folder']:>8}: folder missing — skipped")
                continue
            if meta.get("file"):
                path = os.path.join(sub, meta["file"])
            else:
                files = sorted(glob.glob(os.path.join(sub, "*.mat")))
                if not files:
                    print(f"  {meta['folder']:>8}: no .mat file — skipped")
                    continue
                if len(files) > 1:
                    print(f"  {meta['folder']:>8}: {len(files)} files, using the first "
                          f"(set 'file' in GROUPS to choose)")
                path = files[0]
            recs.append(process(path, meta))
        if not recs:
            continue
        payload = dict(title=g["title"], intro=g["intro"], walkers=recs)
        with open(out_path, "w") as fh:
            fh.write("// generated by prepare_data.py\n"
                     "window.GROUPS = window.GROUPS || {};\n"
                     f"window.GROUPS[{json.dumps(key)}] = ")
            json.dump(payload, fh)
            fh.write(";\n")
        print(f"  -> {out_path} ({os.path.getsize(out_path)/1e6:.1f} MB)")
        made += 1
    if not made:
        print("Nothing written. Check the folder layout described at the top of this file.")


if __name__ == "__main__":
    main()
