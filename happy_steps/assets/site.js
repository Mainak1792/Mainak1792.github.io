/* Happy Steps — shared page behaviour */
(() => {
  "use strict";
  const bar = document.querySelector(".appbar");
  if (bar) {
    const onScroll = () => bar.classList.toggle("scrolled", window.scrollY > 4);
    onScroll(); window.addEventListener("scroll", onScroll, { passive: true });
    const btn = bar.querySelector(".menu-btn");
    btn && btn.addEventListener("click", () => {
      const open = bar.classList.toggle("open"); btn.setAttribute("aria-expanded", open);
    });
  }

  const els = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    const io = new IntersectionObserver(es => es.forEach(e => {
      if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
    }), { rootMargin: "0px 0px -8% 0px" });
    els.forEach(e => io.observe(e));
  } else els.forEach(e => e.classList.add("in"));

  /* hero: a real 7-second geophone recording, swept by a playhead */
  const c = document.getElementById("heroWave"), H = window.HERO_WAVE;
  if (!c || !H) return;
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const css = n => getComputedStyle(document.documentElement).getPropertyValue(n).trim();
  const blue = css("--blue"), green = css("--green-500"), line = css("--line-2");
  const counter = document.getElementById("heroSteps");
  let t0 = null;
  function draw(ts) {
    const r = c.getBoundingClientRect(), d = window.devicePixelRatio || 1;
    const W = Math.round(r.width * d), Hh = Math.round(r.height * d);
    if (c.width !== W || c.height !== Hh) { c.width = W; c.height = Hh; }
    const g = c.getContext("2d"); g.clearRect(0, 0, W, Hh);
    if (t0 == null) t0 = ts;
    const p = reduce ? 1 : ((ts - t0) / 1000 / H.secs) % 1.15;
    const mid = Hh * .56, amp = Hh * .38, n = H.mm.length;
    g.fillStyle = line; g.fillRect(0, mid, W, d);
    for (let i = 0; i < n; i++) {
      const x = i / n * W, [lo, hi] = H.mm[i], seen = i / n <= p;
      g.fillStyle = seen ? blue : "#C6CACF";
      g.fillRect(x, mid - hi * amp, Math.max(1, W / n - .4 * d), Math.max(d, (hi - lo) * amp));
    }
    let k = 0;
    H.steps.forEach(s => {
      if (s > p) return; k++;
      const x = s * W, age = Math.min(1, (p - s) * 6);
      g.fillStyle = green; g.globalAlpha = 1;
      g.beginPath(); g.arc(x, 12 * d, (4 + (1 - age) * 4) * d, 0, 7); g.fill();
      g.globalAlpha = .25; g.fillRect(x - d / 2, 18 * d, d, Hh - 26 * d); g.globalAlpha = 1;
    });
    if (p <= 1) { g.fillStyle = css("--ink"); g.fillRect(p * W, 0, 1.5 * d, Hh); }
    if (counter) counter.textContent = k;
    if (!reduce) requestAnimationFrame(draw);
  }
  requestAnimationFrame(draw);
  window.addEventListener("resize", () => reduce && requestAnimationFrame(draw));
})();
