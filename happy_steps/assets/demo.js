/* Happy Steps — live demo engine */
(() => {
"use strict";
const $ = s => document.querySelector(s);
const css = n => getComputedStyle(document.documentElement).getPropertyValue(n).trim();
const store = {
  get(k){ try { return localStorage.getItem(k); } catch(e){ return null; } },
  set(k,v){ try { localStorage.setItem(k,v); } catch(e){} },
  del(k){ try { localStorage.removeItem(k); } catch(e){} }
};

/* ================= data ================= */
const REC = (window.WALKERS || []).map(w => {
  const bin = atob(w.b64), u8 = new Uint8Array(bin.length);
  for (let k = 0; k < bin.length; k++) u8[k] = bin.charCodeAt(k);
  const i16 = new Int16Array(u8.buffer), x = new Float32Array(i16.length);
  for (let k = 0; k < i16.length; k++) x[k] = i16[k] / 32767;
  delete w.b64;
  return Object.assign(w, { x });
});
if (!REC.length) { $("#srcNote").textContent = "No recordings found: data/walkers.js is missing."; }
const RES = REC.find(w => w.id === "A") || REC[0];
const VIS = REC.find(w => w.id === "B") || REC[1] || REC[0];
const ENROLL_S = 60;

/* ================= signal tools ================= */
function fft(re, im) {
  const n = re.length;
  for (let i = 1, j = 0; i < n; i++) {
    let bit = n >> 1; for (; j & bit; bit >>= 1) j ^= bit; j ^= bit;
    if (i < j) { let t = re[i]; re[i] = re[j]; re[j] = t; t = im[i]; im[i] = im[j]; im[j] = t; }
  }
  for (let len = 2; len <= n; len <<= 1) {
    const ang = -2 * Math.PI / len, wr = Math.cos(ang), wi = Math.sin(ang), h = len >> 1;
    for (let i = 0; i < n; i += len) {
      let cr = 1, ci = 0;
      for (let k = 0; k < h; k++) {
        const a = i + k, b = a + h;
        const tr = re[b] * cr - im[b] * ci, ti = re[b] * ci + im[b] * cr;
        re[b] = re[a] - tr; im[b] = im[a] - ti; re[a] += tr; im[a] += ti;
        const nr = cr * wr - ci * wi; ci = cr * wi + ci * wr; cr = nr;
      }
    }
  }
}
function ifft(re, im) {
  const n = re.length;
  for (let i = 0; i < n; i++) im[i] = -im[i];
  fft(re, im);
  for (let i = 0; i < n; i++) { re[i] /= n; im[i] = -im[i] / n; }
}
const NF = 40, FMIN = 5, FMAX = 400, W0 = 6;
const FREQS = Float32Array.from({ length: NF }, (_, i) => FMIN * Math.pow(FMAX / FMIN, i / (NF - 1)));

function stepSegment(x, s, fs) {
  const a = s - Math.round(0.05 * fs), L = Math.round(0.5 * fs), seg = new Float32Array(L);
  let m = 0;
  for (let k = 0; k < L; k++) { const v = x[a + k] || 0; seg[k] = v; m += v; }
  m /= L; for (let k = 0; k < L; k++) seg[k] -= m;
  return seg;
}
/* CWT with an analytic complex Morlet wavelet, done in the frequency domain */
function cwt(seg, fs) {
  const T = seg.length; let N = 1; while (N < 2 * T) N <<= 1;
  const re = new Float64Array(N), im = new Float64Array(N);
  re.set(seg); fft(re, im);
  const mag = new Float32Array(NF * T), yr = new Float64Array(N), yi = new Float64Array(N);
  for (let f = 0; f < NF; f++) {
    const s = W0 / (2 * Math.PI * FREQS[f]);
    for (let k = 0; k < N; k++) {
      const om = 2 * Math.PI * k * fs / N;
      const psi = k > 0 && k < N / 2 ? 2 * Math.exp(-0.5 * (s * om - W0) * (s * om - W0)) : 0;
      yr[k] = re[k] * psi; yi[k] = im[k] * psi;
    }
    ifft(yr, yi);
    for (let t = 0; t < T; t++) mag[f * T + t] = Math.hypot(yr[t], yi[t]);
  }
  return { mag, T };
}
/* gain-free spectral fingerprint: log energy per scale, mean removed, unit length */
function fingerprint({ mag, T }) {
  const v = new Float32Array(NF);
  for (let f = 0; f < NF; f++) { let e = 0; for (let t = 0; t < T; t++) e += mag[f * T + t] ** 2; v[f] = Math.log10(e / T + 1e-20); }
  let m = 0; for (const a of v) m += a; m /= NF;
  let n = 0; for (let f = 0; f < NF; f++) { v[f] -= m; n += v[f] * v[f]; }
  n = Math.sqrt(n) || 1; for (let f = 0; f < NF; f++) v[f] /= n;
  return v;
}
const dot = (a, b) => { let s = 0; for (let i = 0; i < a.length; i++) s += a[i] * b[i]; return s; };
const median = a => { const b = Float64Array.from(a).sort(); const n = b.length; return n ? (n % 2 ? b[(n - 1) / 2] : (b[n / 2 - 1] + b[n / 2]) / 2) : 0; };
function gaitFromSteps(stepSamples, fs) {
  const isi = [];
  for (let i = 1; i < stepSamples.length; i++) {
    const d = (stepSamples[i] - stepSamples[i - 1]) / fs;
    if (d > 0.3 && d < 1.2) isi.push(d);
  }
  if (isi.length < 2) return null;
  const mean = isi.reduce((a, b) => a + b, 0) / isi.length;
  const sd = Math.sqrt(isi.reduce((a, b) => a + (b - mean) ** 2, 0) / isi.length);
  const odd = isi.filter((_, i) => i % 2), even = isi.filter((_, i) => !(i % 2));
  const mo = odd.reduce((a, b) => a + b, 0) / (odd.length || 1), me = even.reduce((a, b) => a + b, 0) / (even.length || 1);
  return {
    cadence: 60 / median(isi), cv: sd / mean,
    symmetry: odd.length ? 1 - Math.abs(mo - me) / ((mo + me) / 2) : 1
  };
}

/* ================= enrolment (first minute of the resident) ================= */
const ENR = (() => {
  const fs = RES.fs, steps = RES.steps.filter(s => s > 0.1 * fs && s < ENROLL_S * fs);
  const feats = steps.map(s => fingerprint(cwt(stepSegment(RES.x, s, fs), fs)));
  const c = new Float32Array(NF); feats.forEach(f => f.forEach((v, i) => c[i] += v));
  let n = Math.sqrt(dot(c, c)) || 1; c.forEach((v, i) => c[i] = v / n);
  const sims = feats.map(f => dot(f, c)).sort((a, b) => a - b);
  const thr = Math.max(0.5, sims[Math.floor(0.05 * sims.length)] - 0.05);
  // usual gait from the walking bouts in the enrolment minute
  const bouts = []; let cur = [];
  steps.forEach(s => { if (cur.length && s - cur[cur.length - 1] > 2 * fs) { bouts.push(cur); cur = []; } cur.push(s); });
  if (cur.length) bouts.push(cur);
  const gs = bouts.map(b => gaitFromSteps(b, fs)).filter(Boolean);
  const avg = k => gs.reduce((a, g) => a + g[k], 0) / (gs.length || 1);
  let dom = 0; for (let f = 1; f < NF; f++) if (c[f] > c[dom]) dom = f;
  return { centroid: c, thr, n: feats.length, cadence: avg("cadence") || RES.cadence, cv: avg("cv") || 0.05,
           symmetry: avg("symmetry") || 0.95, domHz: FREQS[dom] };
})();

/* ================= edge processor (runs on any stream) ================= */
class Edge {
  constructor(fs, clockBaseMs) {
    this.fs = fs; this.FR = Math.max(1, Math.round(fs * 0.01));
    this.buf = new Float32Array(fs * 120); this.N = 0;
    this.fe = []; this.env = []; this.pi = 0; this.thr = Infinity; this.lastPeak = -1e9;
    this.pending = []; this.steps = []; this.bout = []; this.events = [];
    this.clockBase = clockBaseMs; this.latest = null; this.onEvent = null;
  }
  push(arr) {
    if (this.N + arr.length > this.buf.length) {
      const nb = new Float32Array(Math.max(this.buf.length * 2, this.N + arr.length)); nb.set(this.buf.subarray(0, this.N)); this.buf = nb;
    }
    this.buf.set(arr, this.N); this.N += arr.length; this.process();
  }
  process() {
    const { FR } = this, H = 30;
    while ((this.fe.length + 1) * FR <= this.N) {
      const a = this.fe.length * FR; let e = 0;
      for (let k = a; k < a + FR; k++) e += this.buf[k] * this.buf[k];
      this.fe.push(e / FR);
    }
    while (this.env.length < this.fe.length - 1) {
      const i = this.env.length, fe = this.fe;
      this.env.push(Math.sqrt((fe[Math.max(0, i - 1)] + fe[i] + fe[i + 1]) / 3));
    }
    while (this.pi + H < this.env.length) {
      const i = this.pi++;
      if (i < 150) continue;
      if (i % 50 === 0 || this.thr === Infinity) {
        const w = this.env.slice(Math.max(0, i - 3000), i + 1), med = median(w);
        this.thr = med + 8 * (median(w.map(v => Math.abs(v - med))) + 1e-12);
      }
      const v = this.env[i];
      if (v <= this.thr || i - this.lastPeak < H) continue;
      let ok = true;
      for (let j = i - H; j <= i + H && ok; j++) if (j !== i && (this.env[j] > v || (j < i && this.env[j] === v))) ok = false;
      if (!ok) continue;
      this.lastPeak = i; this.pending.push(i * FR + (FR >> 1));
    }
    const need = Math.round(0.46 * this.fs);
    while (this.pending.length && this.pending[0] + need <= this.N) this.classify(this.pending.shift());
  }
  classify(s) {
    const c = cwt(stepSegment(this.buf, s, this.fs), this.fs), fp = fingerprint(c), sim = dot(fp, ENR.centroid);
    const step = { s, sim, who: sim >= ENR.thr ? "resident_01" : "unknown" };
    this.steps.push(step); this.latest = { cwt: c, fp, sim, who: step.who };
    if (this.bout.length && s - this.bout[this.bout.length - 1].s > 2 * this.fs) this.closeBout();
    this.bout.push(step);
    if ((s - this.bout[0].s) / this.fs > 40) this.closeBout();
  }
  tick() { if (this.bout.length && this.N - this.bout[this.bout.length - 1].s > 2.2 * this.fs) this.closeBout(); }
  closeBout() {
    const b = this.bout; this.bout = [];
    if (b.length < 4) return;
    const g = gaitFromSteps(b.map(x => x.s), this.fs); if (!g) return;
    const sims = b.map(x => x.sim), meanSim = sims.reduce((a, c) => a + c, 0) / sims.length;
    const person = meanSim >= ENR.thr - 0.02 ? "resident_01" : "unknown";
    const ev = {
      schema: "footstep-event/v1", home_id: "H001", sensor_id: "geo-01",
      time: isoJST(this.clockBase + b[0].s / this.fs * 1000),
      duration_s: +((b[b.length - 1].s - b[0].s) / this.fs).toFixed(1),
      person, id_similarity: +(sims.reduce((a, c) => a + c, 0) / sims.length).toFixed(2),
      steps: b.length, cadence_spm: Math.round(g.cadence),
      step_interval_cv: +g.cv.toFixed(3), temporal_symmetry: +g.symmetry.toFixed(2),
      event_type: "walk", raw_signal_included: false
    };
    this.events.push(ev); this.onEvent && this.onEvent(ev);
  }
}

/* ================= time helpers (home clock in Japan time) ================= */
const JST = 9 * 3600e3;
function todayAt(hhmm, dayOffset = 0) {
  const [h, m] = hhmm.split(":").map(Number), now = new Date(Date.now() + JST);
  return Date.UTC(now.getUTCFullYear(), now.getUTCMonth(), now.getUTCDate() + dayOffset, h, m) - JST;
}
function isoJST(ms) { return new Date(ms + JST).toISOString().slice(0, 19) + "+09:00"; }
const hhmm = iso => iso.slice(11, 16);

/* ================= sources ================= */
function retime(w, from, factor) {
  // keep every real step waveform, but place the steps further apart (slower walking)
  const fs = w.fs, x = w.x, steps = w.steps.filter(s => s >= from);
  const n = Math.round((w.n - from) * factor), out = new Float32Array(n);
  const noise = 1.4826 * median(Array.from(x.subarray(from, from + 20 * fs), Math.abs).filter((_, i) => i % 7 === 0));
  let seed = 7; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
  for (let i = 0; i < n; i++) out[i] = (rnd() + rnd() + rnd() - 1.5) * noise * 1.4;
  const pre = Math.round(0.1 * fs);
  steps.forEach((s, i) => {
    const end = Math.min(i + 1 < steps.length ? steps[i + 1] - pre : w.n, s + Math.round(0.6 * fs));
    const at = Math.round((s - from) * factor) - pre;
    for (let k = s - pre, j = at; k < end; k++, j++) if (j >= 0 && j < n) out[j] = x[k];
  });
  return out;
}

/* ================= scenarios ================= */
const SCEN = {
  normal: { clock: "10:00", note: "Walks earlier this morning are simulated. The live recording continues the day from 10:00." },
  slower: { clock: "10:00", stretch: 1.18, note: "The real resident recording is re-timed so each step is 18% further apart. Morning walks were also slower." },
  night:  { clock: "10:00", note: "Simulated: four short walks between 1 and 5 a.m. The resident is usually asleep then." },
  quiet:  { clock: "14:30", note: "Simulated: one short walk at 06:55, then nothing until the live recording at 14:30." },
  fall:   { clock: "10:00", note: "Simulated: a heavy impact right after the live walk, then no steps for 25 minutes." }
};
function rngFrom(seed) { let s = seed >>> 0 || 1; return () => (s = (s * 1664525 + 1013904223) >>> 0) / 4294967296; }
function synthWalk(ms, r, k = {}) {
  const cad = ENR.cadence * (k.cad || 1) * (1 + (r() - .5) * .04), steps = Math.round(10 + r() * 24);
  return { schema: "footstep-event/v1", home_id: "H001", sensor_id: "geo-01", time: isoJST(ms),
    duration_s: +(steps * 60 / cad).toFixed(1), person: "resident_01", id_similarity: +(0.9 + r() * .07).toFixed(2),
    steps, cadence_spm: Math.round(cad), step_interval_cv: +(ENR.cv * (k.cv || 1) * (0.9 + r() * .2)).toFixed(3),
    temporal_symmetry: +Math.min(0.99, ENR.symmetry * (k.sym || 1) * (0.98 + r() * .03)).toFixed(2),
    event_type: "walk", raw_signal_included: false, simulated: true };
}
function scenarioEvents(key) {
  const r = rngFrom(42 + key.length * 13), ev = [];
  const morning = ["06:48", "07:14", "07:52", "08:31", "09:06", "09:41"];
  if (key === "quiet") { ev.push(synthWalk(todayAt("06:55"), r)); return ev; }
  if (key === "night") ["01:42", "02:35", "03:58", "04:21"].forEach(t => ev.push(synthWalk(todayAt(t), r, { cad: .92, cv: 1.3 })));
  const k = key === "slower" ? { cad: 0.85, cv: 1.6, sym: 0.97 } : {};
  morning.forEach(t => ev.push(synthWalk(todayAt(t) + Math.round(r() * 4) * 60e3, r, k)));
  return ev;
}
function fallEvent(afterMs) {
  return { schema: "footstep-event/v1", home_id: "H001", sensor_id: "geo-01", time: isoJST(afterMs + 60e3),
    event_type: "impact_then_silence", person: "resident_01", impact_energy_vs_usual_step: 5.3,
    silence_after_min: 25, raw_signal_included: false, simulated: true };
}
function baseline14() {
  const r = rngFrom(2024), days = [];
  for (let d = 14; d >= 1; d--) {
    days.push({ date: isoJST(todayAt("12:00", -d)).slice(0, 10),
      walk_events: Math.round(20 + r() * 8), total_steps: Math.round(2300 + r() * 700),
      mean_cadence_spm: Math.round(ENR.cadence + (r() - .5) * 4),
      mean_step_interval_cv: +(ENR.cv * (0.9 + r() * .2)).toFixed(3),
      first_activity: `06:${String(35 + Math.floor(r() * 20)).padStart(2, "0")}`,
      walks_between_00_05: r() < 0.15 ? 1 : 0, longest_daytime_gap_h: +(1.5 + r() * 1.5).toFixed(1) });
  }
  const m = k => +(days.reduce((a, x) => a + x[k], 0) / days.length).toFixed(k.includes("cv") ? 3 : 1);
  return { summary: { mean_cadence_spm: m("mean_cadence_spm"), mean_step_interval_cv: m("mean_step_interval_cv"),
    mean_total_steps: m("total_steps"), mean_walks_between_00_05: m("walks_between_00_05"),
    mean_longest_daytime_gap_h: m("longest_daytime_gap_h") }, days };
}

/* ================= app state ================= */
const st = { src: "resident", speed: 4, scen: "normal", running: false, edge: null, srcX: null, srcFs: 2000, pos: 0,
             ws: null, live: false, bytesOut: 0, lastT: 0, ended: false };

function resetEdge() {
  const sc = SCEN[st.scen];
  st.edge = new Edge(st.src === "live" ? st.srcFs : RES.fs, todayAt(sc.clock));
  st.edge.onEvent = ev => { st.bytesOut += JSON.stringify(ev).length; showEvent(ev); renderEvents(); };
  st.bytesOut = 0; st.pos = 0; st.ended = false;
  if (st.src === "resident") {
    const from = ENROLL_S * RES.fs;
    st.srcX = sc.stretch ? retime(RES, from, sc.stretch) : RES.x.subarray(from); st.srcFs = RES.fs;
  } else if (st.src === "visitor") { st.srcX = VIS.x; st.srcFs = VIS.fs; }
  else st.srcX = null;
  $("#lastEvent").textContent = "Start the sensor. When a walk ends, its summary appears here.";
  updateNotes(); renderEvents(); updateTiles(); drawAll();
}
function updateNotes() {
  const notes = {
    resident: `The resident’s floor (wooden). The first minute was used once to enrol her (${ENR.n} steps). What plays now is the rest of the recording, which the system has not seen.`,
    visitor: "A different person, never enrolled, on a different floor. The system should say “not recognised”.",
    live: "Run bridge/geophone_bridge.py on the computer your geophone is plugged into, then connect. See README."
  };
  $("#srcNote").textContent = notes[st.src];
  $("#scenNote").textContent = SCEN[st.scen].note;
  $("#liveRow").hidden = st.src !== "live";
  $("#runBtn").style.display = st.src === "live" ? "none" : "";
}

/* ================= main loop ================= */
function loop(t) {
  if (!st.running) return;
  const dt = Math.min(0.1, (t - (st.lastT || t)) / 1000); st.lastT = t;
  if (st.srcX) {
    const n = Math.round(dt * st.speed * st.srcFs), end = Math.min(st.srcX.length, st.pos + n);
    if (end > st.pos) { st.edge.push(st.srcX.subarray(st.pos, end)); st.pos = end; }
    if (st.pos >= st.srcX.length) { st.edge.tick(); st.edge.closeBout(); stopRun(true); }
  }
  st.edge.tick(); updateTiles(); drawWave(); drawLatest();
  requestAnimationFrame(loop);
}
function startRun() {
  if (st.ended) resetEdge();
  st.running = true; st.lastT = 0; $("#runBtn").textContent = "Pause"; requestAnimationFrame(loop);
}
function stopRun(finished) {
  st.running = false; st.ended = !!finished;
  $("#runBtn").textContent = finished ? "Play again" : "Continue";
  drawAll();
}

/* ================= live bridge (WebSocket) ================= */
function connectWS() {
  if (st.ws) { st.ws.close(); return; }
  let ws;
  try { ws = new WebSocket($("#wsUrl").value.trim()); } catch (e) { $("#srcNote").textContent = "Could not open: " + e.message; return; }
  st.ws = ws; $("#wsBtn").textContent = "Connecting…";
  ws.onopen = () => { $("#wsBtn").textContent = "Disconnect"; $("#srcNote").textContent = "Connected. Waiting for the sensor…"; };
  ws.onclose = () => { st.ws = null; st.running = false; $("#wsBtn").textContent = "Connect"; };
  ws.onerror = () => { $("#srcNote").textContent = "Could not reach the bridge. Is geophone_bridge.py running? (Pages on https can reach ws://localhost only.)"; };
  ws.onmessage = m => {
    let d; try { d = JSON.parse(m.data); } catch (e) { return; }
    if (d.type === "meta") {
      st.srcFs = d.fs; resetEdge(); st.running = true; st.lastT = 0; requestAnimationFrame(loop);
      $("#srcNote").textContent = `Live: ${d.source || "sensor"} at ${d.fs} Hz.`;
    } else if (d.type === "chunk" && st.edge) {
      const bin = atob(d.b64), u8 = new Uint8Array(bin.length);
      for (let k = 0; k < bin.length; k++) u8[k] = bin.charCodeAt(k);
      const i16 = new Int16Array(u8.buffer), f = new Float32Array(i16.length);
      for (let k = 0; k < i16.length; k++) f[k] = i16[k] / 32767;
      st.edge.push(f);
    }
  };
}

/* ================= drawing ================= */
function fit(c) {
  const r = c.getBoundingClientRect(), d = window.devicePixelRatio || 1;
  const W = Math.max(1, Math.round(r.width * d)), H = Math.max(1, Math.round(r.height * d));
  if (c.width !== W || c.height !== H) { c.width = W; c.height = H; }
  const g = c.getContext("2d"); g.setTransform(1, 0, 0, 1, 0, 0); return { g, W, H, d };
}
function drawWave() {
  const { g, W, H, d } = fit($("#wave")), e = st.edge; g.clearRect(0, 0, W, H);
  if (!e) return;
  const fs = e.fs, span = 8 * fs, i1 = e.N, i0 = i1 - span, mid = H / 2;
  g.fillStyle = "#DADCE0"; g.fillRect(0, mid, W, d);
  let pk = 1e-4; for (let k = Math.max(0, i0); k < i1; k++) pk = Math.max(pk, Math.abs(e.buf[k]));
  const gain = 0.92 / pk, per = span / W;
  g.fillStyle = "#3C4043";
  for (let px = 0; px < W; px++) {
    const a = Math.floor(i0 + px * per), b = Math.floor(i0 + (px + 1) * per);
    if (b <= 0) continue;
    let lo = 0, hi = 0; for (let k = Math.max(0, a); k < b && k < i1; k++) { const v = e.buf[k]; if (v < lo) lo = v; if (v > hi) hi = v; }
    const y1 = mid - hi * gain * (H / 2 - 12 * d), y2 = mid - lo * gain * (H / 2 - 12 * d);
    g.fillRect(px, y1, 1, Math.max(d, y2 - y1));
  }
  const cr = css("--green-500"), cu = css("--red");
  for (let j = e.steps.length - 1; j >= 0; j--) {
    const s = e.steps[j]; if (s.s < i0) break;
    const px = (s.s - i0) / span * W; g.fillStyle = s.who === "unknown" ? cu : cr;
    g.beginPath(); g.arc(px, 8 * d, 4.5 * d, 0, 7); g.fill(); g.fillRect(px - d / 2, 12 * d, d, H - 24 * d);
  }
  g.fillStyle = css("--muted"); g.font = `${11 * d}px ${css("--font")}`;
  g.fillText(isoJST(e.clockBase + e.N / fs * 1000).slice(11, 19), W - 64 * d, H - 6 * d);
}
const RAMP = [[248,249,250],[210,227,252],[138,180,248],[26,115,232],[23,78,166],[32,33,36]];
function ramp(t) {
  t = Math.max(0, Math.min(1, t)) * (RAMP.length - 1); const i = Math.min(RAMP.length - 2, Math.floor(t)), u = t - i;
  return RAMP[i].map((v, k) => v + (RAMP[i + 1][k] - v) * u);
}
function drawLatest() {
  const L = st.edge && st.edge.latest;
  { // scalogram
    const { g, W, H, d } = fit($("#scalo")); g.clearRect(0, 0, W, H);
    if (L) {
      const { mag, T } = L.cwt; let mx = 1e-12; for (const v of mag) if (v > mx) mx = v;
      const img = g.createImageData(W, H);
      for (let px = 0; px < W; px++) {
        const t = Math.floor(px / W * T);
        for (let py = 0; py < H; py++) {
          const f = Math.min(NF - 1, Math.floor((1 - py / H) * NF));
          const db = 20 * Math.log10(mag[f * T + t] / mx + 1e-9);
          const c = ramp((db + 40) / 40), o = (py * W + px) * 4;
          img.data[o] = c[0]; img.data[o + 1] = c[1]; img.data[o + 2] = c[2]; img.data[o + 3] = 255;
        }
      }
      g.putImageData(img, 0, 0);
      g.fillStyle = "rgba(255,255,255,.9)"; g.font = `${10 * d}px ${css("--font")}`;
      g.fillText("400 Hz", 4 * d, 12 * d); g.fillText("5 Hz", 4 * d, H - 5 * d); g.fillText("0.5 s →", W - 44 * d, H - 5 * d);
    } else { g.fillStyle = css("--muted"); g.font = `${12 * d}px ${css("--font")}`; g.fillText("waiting for a step…", 10 * d, H / 2); }
  }
  { // fingerprint vs resident
    const { g, W, H, d } = fit($("#match")); g.clearRect(0, 0, W, H);
    const pad = 8 * d, plot = (v, color, dash) => {
      g.strokeStyle = color; g.lineWidth = 2.2 * d; g.setLineDash(dash ? [5 * d, 4 * d] : []); g.beginPath();
      for (let f = 0; f < NF; f++) { const x = pad + f / (NF - 1) * (W - 2 * pad), y = H / 2 - v[f] * (H * 1.1);
        f ? g.lineTo(x, y) : g.moveTo(x, y); }
      g.stroke(); g.setLineDash([]);
    };
    plot(ENR.centroid, "#9AA0A6", true);
    if (L) plot(L.fp, L.who === "unknown" ? css("--red") : css("--green-500"), false);
    g.fillStyle = css("--muted"); g.font = `${10 * d}px ${css("--font")}`;
    g.fillText("5 Hz", pad, H - 5 * d); g.fillText("400 Hz", W - 40 * d, H - 5 * d);
  }
}
function drawAll() { drawWave(); drawLatest(); }

function updateTiles() {
  const e = st.edge; if (!e) return;
  $("#tSteps").textContent = e.steps.length;
  const recent = e.steps.slice(-12).map(s => s.s), g = recent.length > 4 ? gaitFromSteps(recent, e.fs) : null;
  $("#tCad").textContent = g ? Math.round(g.cadence) : "–";
  const L = e.latest;
  $("#tWho").innerHTML = L ? (L.who === "unknown" ? '<span class="who-unk">Visitor?</span>' : '<span class="who-res">Resident</span>') : "–";
  $("#tSim").textContent = L ? L.sim.toFixed(2) : "–";
  const rawBytes = e.N * 2;
  $("#bytes").innerHTML = `sent <b class="num">${fmtB(st.bytesOut)}</b> · raw signal kept at home <b class="num">${fmtB(rawBytes)}</b>`;
  $("#clock").textContent = "home clock " + isoJST(e.clockBase + e.N / e.fs * 1000).slice(11, 16);
}
const fmtB = b => b < 1024 ? b + " B" : b < 1048576 ? (b / 1024).toFixed(1) + " KB" : (b / 1048576).toFixed(1) + " MB";
function showEvent(ev) {
  $("#lastEvent").textContent = JSON.stringify(ev, null, 2);
  const p = $("#packet"); p.classList.remove("go"); void p.offsetWidth; p.classList.add("go");
}

/* ================= today's data ================= */
function todayEvents() {
  const live = (st.edge ? st.edge.events : []).map(e => Object.assign({}, e));
  const all = scenarioEvents(st.scen).concat(live);
  if (st.scen === "fall") {
    const last = live.length ? Date.parse(live[live.length - 1].time) + live[live.length - 1].duration_s * 1000 : todayAt("10:03");
    all.push(fallEvent(last));
  }
  return all.sort((a, b) => Date.parse(a.time) - Date.parse(b.time));
}
function renderEvents() {
  const ev = todayEvents(), box = $("#events"); box.innerHTML = "";
  const live = ev.filter(e => !e.simulated).length;
  $("#evCount").textContent = `(${ev.length}: ${live} live, ${ev.length - live} simulated)`;
  ev.slice().reverse().forEach(e => {
    const div = document.createElement("div"); div.className = "ev";
    const what = e.event_type === "walk"
      ? `${e.steps} steps · ${e.cadence_spm}/min · ${e.person === "unknown" ? "not recognised" : "resident"}`
      : `heavy impact (×${e.impact_energy_vs_usual_step}), then ${e.silence_after_min} min silence`;
    const pill = e.event_type !== "walk" ? '<span class="pill alert">simulated</span>' : e.simulated ? '<span class="pill sim">simulated</span>' : '<span class="pill live">live</span>';
    div.innerHTML = `<span class="t num">${hhmm(e.time)}</span><span>${what}<br><span class="k">${e.event_type}</span></span>${pill}`;
    box.appendChild(div);
  });
}

/* ================= Gemini ================= */
const SYSTEM = `You are a gentle family-care assistant inside a privacy-first home system for an older person who lives alone.
You only receive footstep summaries from a floor vibration sensor. There is no camera, no microphone and no raw signal.
Compare TODAY with the resident's OWN 14-day baseline. Look at: walking speed (cadence_spm), rhythm steadiness (step_interval_cv, higher = less steady), balance of rhythm (temporal_symmetry), walks at night (00:00-05:00), long daytime gaps with no walking, how much she walked, and any event that is not a normal walk.
Rules:
- Never diagnose a disease. Describe changes in plain words, and suggest a kind, simple action (a phone call, a visit).
- An "unknown" person is probably a visitor. Mention it gently, never as a threat.
- Events marked simulated:true are part of today's test data; treat them like real events.
- Call exactly ONE function. Use send_family_report for a usual day or mild changes. Use raise_alert only when someone should check soon (for example a heavy impact followed by silence, or an unusually long daytime gap).
- Japanese text must be warm, natural and short (family: 2-4 sentences). Give an English translation of each Japanese text.
- message_to_resident_ja is spoken aloud to the resident: one or two short, cheerful sentences, never worrying.`;
const TOOLS = [{ functionDeclarations: [
  { name: "send_family_report", description: "Send the family a short, kind daily update.",
    parameters: { type: "OBJECT", properties: {
      status: { type: "STRING", enum: ["good", "gentle_watch"], description: "good = usual day, gentle_watch = small changes worth noticing" },
      headline_ja: { type: "STRING" }, headline_en: { type: "STRING" },
      report_ja: { type: "STRING" }, report_en: { type: "STRING" },
      changes: { type: "ARRAY", items: { type: "OBJECT", properties: {
        metric: { type: "STRING" }, today: { type: "STRING" }, usual: { type: "STRING" }, note_en: { type: "STRING" } },
        required: ["metric", "today", "usual"] } },
      message_to_resident_ja: { type: "STRING" }, message_to_resident_en: { type: "STRING" } },
      required: ["status", "headline_ja", "headline_en", "report_ja", "report_en", "message_to_resident_ja", "message_to_resident_en"] } },
  { name: "raise_alert", description: "Ask a family member or carer to check on the resident soon.",
    parameters: { type: "OBJECT", properties: {
      level: { type: "STRING", enum: ["check_in", "urgent"] },
      headline_ja: { type: "STRING" }, headline_en: { type: "STRING" },
      reason_ja: { type: "STRING" }, reason_en: { type: "STRING" },
      suggested_action_ja: { type: "STRING" }, suggested_action_en: { type: "STRING" },
      message_to_resident_ja: { type: "STRING" }, message_to_resident_en: { type: "STRING" } },
      required: ["level", "headline_ja", "headline_en", "reason_ja", "reason_en", "suggested_action_ja", "suggested_action_en", "message_to_resident_ja", "message_to_resident_en"] } }
] }];
function buildPayload() {
  const ev = todayEvents(), last = ev.length ? ev[ev.length - 1] : null;
  const nowMs = Math.max(st.edge ? st.edge.clockBase + st.edge.N / st.edge.fs * 1000 : 0,
    last ? Date.parse(last.time) + (last.duration_s || 0) * 1000 + (last.silence_after_min || 0) * 60e3 : 0);
  return {
    task: "daily_family_update", now: isoJST(nowMs),
    resident: { id: "resident_01", family_calls_her: "お母さん", lives_alone: true, age_group: "80s" },
    privacy: "Footstep summaries only. No raw vibration, audio or video.",
    baseline_14_days: baseline14(), today_events: ev
  };
}
function requestBody(payload) {
  return {
    systemInstruction: { parts: [{ text: SYSTEM }] },
    contents: [{ role: "user", parts: [{ text: "Here is today's data. Write the family update.\n```json\n" + JSON.stringify(payload) + "\n```" }] }],
    tools: TOOLS, toolConfig: { functionCallingConfig: { mode: "ANY" } },
    generationConfig: { temperature: 0.4 }
  };
}
const modelId = () => ($("#modelCustom").value.trim() || $("#model").value);
async function gemini(model, body, key) {
  const r = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${encodeURIComponent(model)}:generateContent`,
    { method: "POST", headers: { "Content-Type": "application/json", "x-goog-api-key": key }, body: JSON.stringify(body) });
  const j = await r.json().catch(() => ({}));
  if (!r.ok) throw new Error((j.error && j.error.message) || `HTTP ${r.status}`);
  return j;
}

/* offline stand-in: same function schema, simple rules (clearly labelled) */
function offlineReason(p) {
  const walks = p.today_events.filter(e => e.event_type === "walk"), res = walks.filter(e => e.person === "resident_01");
  const visitors = walks.filter(e => e.person === "unknown").length, b = p.baseline_14_days.summary;
  const cad = res.length ? Math.round(res.reduce((a, e) => a + e.cadence_spm, 0) / res.length) : null;
  const night = res.filter(e => +e.time.slice(11, 13) < 5).length;
  const impact = p.today_events.find(e => e.event_type === "impact_then_silence");
  const day = res.map(e => Date.parse(e.time)).filter(t => +isoJST(t).slice(11, 13) >= 6);
  const nowMs = Date.parse(p.now); if (day.length) day.push(nowMs);
  let gap = 0; for (let i = 1; i < day.length; i++) gap = Math.max(gap, (day[i] - day[i - 1]) / 3600e3);
  const vis = visitors ? { ja: "今日はお客さまが来ていたようです。", en: "It looks like someone visited today." } : { ja: "", en: "" };
  if (impact) return { name: "raise_alert", args: { level: "urgent",
    headline_ja: "お母さんの様子を、すぐに確かめてください", headline_en: "Please check on Mother now",
    reason_ja: `${hhmm(impact.time)}ごろ、いつもの足音より大きな衝撃があり、その後${impact.silence_after_min}分間、足音がありません。`,
    reason_en: `Around ${hhmm(impact.time)} there was an impact much stronger than a usual step, and no steps for ${impact.silence_after_min} minutes since.`,
    suggested_action_ja: "まずお電話を。つながらなければ、近くの方に見に行ってもらってください。",
    suggested_action_en: "Call her first. If she does not answer, ask someone nearby to visit.",
    message_to_resident_ja: "大丈夫ですか？ いま、ご家族に連絡しましたよ。", message_to_resident_en: "Are you okay? I have let your family know." } };
  if (gap > 5) return { name: "raise_alert", args: { level: "check_in",
    headline_ja: "今日はとても静かな一日です", headline_en: "Today has been very quiet",
    reason_ja: `朝のあと、約${gap.toFixed(0)}時間ほど足音がありませんでした。いつもは長くても${b.mean_longest_daytime_gap_h}時間ほどです。`,
    reason_en: `After the morning, there were no steps for about ${gap.toFixed(0)} hours. Usually the longest gap is about ${b.mean_longest_daytime_gap_h} hours.`,
    suggested_action_ja: "お時間のあるときに、声をかけてみてください。", suggested_action_en: "When you have a moment, give her a call.",
    message_to_resident_ja: "こんにちは。少しお散歩して、お茶でもいかがですか。", message_to_resident_en: "Hello! How about a short walk and a cup of tea?" } };
  const changes = [];
  if (cad != null) changes.push({ metric: "walking speed (steps/min)", today: String(cad), usual: String(Math.round(b.mean_cadence_spm)) });
  changes.push({ metric: "walks at night (0–5 a.m.)", today: String(night), usual: String(b.mean_walks_between_00_05) });
  if (cad != null && cad < b.mean_cadence_spm * 0.92) return { name: "send_family_report", args: { status: "gentle_watch", changes,
    headline_ja: "今日はいつもより、ゆっくり歩いていました", headline_en: "She walked more slowly than usual today",
    report_ja: `お母さんは今日も家の中で歩いていました。歩く速さはいつもより少しゆっくりで、リズムも少し不安定でした。疲れているだけかもしれません。数日続くようなら、声をかけてみてください。${vis.ja}`,
    report_en: `Mother was walking around the house today. Her pace was a little slower than usual and her rhythm a bit less steady. She may just be tired. If it continues for a few days, give her a call. ${vis.en}`,
    message_to_resident_ja: "今日もよく歩けましたね。ゆっくり休んでくださいね。", message_to_resident_en: "You walked well today. Have a good rest." } };
  if (night >= 2) return { name: "send_family_report", args: { status: "gentle_watch", changes,
    headline_ja: "夜中に何度か起きていたようです", headline_en: "She was up a few times during the night",
    report_ja: `昨夜は${night}回、夜中に歩いていました。いつもはほとんどありません。よく眠れなかったのかもしれません。今日の昼間はいつも通り歩いています。${vis.ja}`,
    report_en: `She walked ${night} times during the night. Usually this almost never happens. She may not have slept well. During the day she walked as usual. ${vis.en}`,
    message_to_resident_ja: "おはようございます。今夜はゆっくり眠れるといいですね。", message_to_resident_en: "Good morning. I hope you sleep well tonight." } };
  return { name: "send_family_report", args: { status: "good", changes,
    headline_ja: "お母さんは今日も元気に歩いています", headline_en: "Mother is walking well today",
    report_ja: `今日も朝から、いつものペースで家の中を歩いています。歩くリズムも安定していて、夜もよく休めていたようです。${vis.ja}`,
    report_en: `Since the morning she has been walking around the house at her usual pace. Her rhythm is steady, and she seems to have rested well at night. ${vis.en}`,
    message_to_resident_ja: "今日もよく歩けましたね。いい一日を！", message_to_resident_en: "You walked well today. Have a lovely day!" } };
}

let lastCall = null;
async function ask() {
  const key = $("#apiKey").value.trim(), payload = buildPayload(), body = requestBody(payload);
  $("#reqPre").textContent = `POST https://generativelanguage.googleapis.com/v1beta/models/${modelId()}:generateContent\nx-goog-api-key: ••••••\n\n` + JSON.stringify(body, null, 2);
  const status = $("#status"); status.className = "status";
  if ($("#remember").checked && key) store.set("gemini_key", key); else if (!$("#remember").checked) store.del("gemini_key");
  $("#askBtn").disabled = true;
  try {
    let call, src;
    if (key) {
      status.textContent = `Asking ${modelId()}…`;
      const j = await gemini(modelId(), body, key);
      const parts = (j.candidates && j.candidates[0] && j.candidates[0].content && j.candidates[0].content.parts) || [];
      const fc = parts.find(p => p.functionCall);
      if (!fc) throw new Error("Gemini answered without a function call. Try again.");
      call = { name: fc.functionCall.name, args: fc.functionCall.args || {} }; src = " · live Gemini response";
      $("#resPre").textContent = JSON.stringify(j, null, 2);
      status.textContent = `Done. ${j.usageMetadata ? j.usageMetadata.totalTokenCount + " tokens." : ""}`;
    } else {
      call = offlineReason(payload); src = " · offline sample (add an API key for the real Gemini call)";
      $("#resPre").textContent = JSON.stringify({ functionCall: call }, null, 2);
      status.textContent = "Showing an offline sample. Paste a Gemini API key to get Gemini’s own answer.";
    }
    lastCall = call; showResult(call, src);
  } catch (e) {
    status.className = "status err"; status.textContent = "Gemini error: " + e.message;
  } finally { $("#askBtn").disabled = false; }
}
function esc(s) { return String(s == null ? "" : s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c])); }
function showResult(call, src) {
  const a = call.args, alert = call.name === "raise_alert";
  $("#fnName").textContent = call.name + "()"; $("#fnSrc").textContent = src;
  const L = $("#letter"); L.className = "letter" + (alert ? " alert" : a.status === "gentle_watch" ? " watch" : "");
  $("#letterTo").textContent = alert ? (a.level === "urgent" ? "Alert to the family · 至急 ご家族へ" : "Please check in · ご家族へ") : "Daily note to the family · ご家族へ";
  $("#hJa").textContent = a.headline_ja || ""; $("#hEn").textContent = a.headline_en || "";
  $("#bJa").textContent = alert ? `${a.reason_ja || ""} ${a.suggested_action_ja || ""}` : (a.report_ja || "");
  $("#bEn").textContent = alert ? `${a.reason_en || ""} ${a.suggested_action_en || ""}` : (a.report_en || "");
  const ch = Array.isArray(a.changes) ? a.changes : [];
  $("#changes").innerHTML = ch.length ? "<tr><th>What</th><th>Today</th><th>Usual</th></tr>" +
    ch.map(c => `<tr><td>${esc(c.metric)}${c.note_en ? `<br><span class="cap">${esc(c.note_en)}</span>` : ""}</td><td class="num">${esc(c.today)}</td><td class="num">${esc(c.usual)}</td></tr>`).join("") : "";
  $("#toRes").innerHTML = `${esc(a.message_to_resident_ja)}<small>${esc(a.message_to_resident_en)}</small>`;
  $("#voiceNote").textContent = "";
  $("#result").classList.add("show");
}

/* voice: Gemini TTS when a key is present, the browser's Japanese voice otherwise */
let actx = null;
async function speak() {
  if (!lastCall) return;
  const text = lastCall.args.message_to_resident_ja || "", key = $("#apiKey").value.trim(), note = $("#voiceNote");
  if (key) {
    try {
      note.textContent = "Gemini is making the voice…";
      const j = await gemini("gemini-2.5-flash-preview-tts", {
        contents: [{ parts: [{ text: "Say warmly and slowly, like a kind grandchild: " + text }] }],
        generationConfig: { responseModalities: ["AUDIO"], speechConfig: { voiceConfig: { prebuiltVoiceConfig: { voiceName: "Leda" } } } }
      }, key);
      const part = j.candidates[0].content.parts.find(p => p.inlineData);
      const rate = +((part.inlineData.mimeType || "").match(/rate=(\d+)/) || [0, 24000])[1];
      const bin = atob(part.inlineData.data), u8 = new Uint8Array(bin.length);
      for (let k = 0; k < bin.length; k++) u8[k] = bin.charCodeAt(k);
      const i16 = new Int16Array(u8.buffer, 0, u8.length >> 1);
      actx = actx || new (window.AudioContext || window.webkitAudioContext)();
      if (actx.state === "suspended") await actx.resume();
      const buf = actx.createBuffer(1, i16.length, rate), ch = buf.getChannelData(0);
      for (let k = 0; k < i16.length; k++) ch[k] = i16[k] / 32768;
      const src = actx.createBufferSource(); src.buffer = buf; src.connect(actx.destination); src.start();
      note.textContent = "Voice by Gemini text-to-speech (gemini-2.5-flash-preview-tts).";
      return;
    } catch (e) { note.textContent = "Gemini voice failed (" + e.message + "). Using the browser voice."; }
  }
  if ("speechSynthesis" in window) {
    const u = new SpeechSynthesisUtterance(text); u.lang = "ja-JP"; u.rate = 0.9;
    speechSynthesis.cancel(); speechSynthesis.speak(u);
    if (!key) note.textContent = "Browser voice. With an API key, Gemini’s own voice is used.";
  }
}

/* ================= controls ================= */
function segGroup(id, fn) {
  const el = $(id);
  el.addEventListener("click", e => {
    const b = e.target.closest("button"); if (!b) return;
    el.querySelectorAll("button").forEach(x => x.setAttribute("aria-pressed", x === b)); fn(b.dataset.v);
  });
}
segGroup("#srcSeg", v => { if (st.ws) st.ws.close(); st.running = false; st.src = v; resetEdge(); $("#runBtn").textContent = "Start sensor"; });
segGroup("#speedSeg", v => st.speed = +v);
segGroup("#scenSeg", v => {
  const restart = st.src === "resident" && (!!SCEN[v].stretch !== !!SCEN[st.scen].stretch);
  const prevClock = SCEN[st.scen].clock; st.scen = v; updateNotes();
  if (restart || prevClock !== SCEN[v].clock) { st.running = false; resetEdge(); $("#runBtn").textContent = "Start sensor"; }
  renderEvents();
});
$("#runBtn").addEventListener("click", () => st.running ? stopRun(false) : startRun());
$("#wsBtn").addEventListener("click", connectWS);
$("#askBtn").addEventListener("click", ask);
$("#speakBtn").addEventListener("click", speak);
const saved = store.get("gemini_key"); if (saved) { $("#apiKey").value = saved; $("#remember").checked = true; }

let rt; new ResizeObserver(() => { clearTimeout(rt); rt = setTimeout(drawAll, 80); }).observe(document.body);
resetEdge();
window.__hs = { st, ENR, todayEvents, buildPayload, offlineReason };
})();
