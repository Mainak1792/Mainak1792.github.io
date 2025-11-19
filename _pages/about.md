---
permalink: /
title: "PhD student at IIT Delhi — Mainak Chakraborty"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<div class="academic-container">
  <header class="profile-header">
    <div class="profile-left">
      <img class="avatar" src="/assets/avatar.jpg" alt="Mainak Chakraborty">
    </div>
    <div class="profile-right">
      <h1 class="name">Mainak Chakraborty</h1>
      <p class="role">PhD Scholar — Signal Processing & Machine Learning, IIT Delhi</p>
      <p class="affil">Advisor: <a href="https://web.iitd.ac.in/~subrat/" target="_blank">Prof. Subrat Kar</a> · PMRF & SPS Fellow</p>
      <div class="badges">
        <a href="mailto:you@example.com" class="badge">✉️ Email</a>
        <a href="https://scholar.google.com" target="_blank" class="badge">🧾 Google Scholar</a>
        <a href="https://orcid.org" target="_blank" class="badge">🔗 ORCID</a>
        <a href="https://github.com/Mainak1792" target="_blank" class="badge">💻 GitHub</a>
        <a href="/assets/Mainak_Chakraborty_CV.pdf" class="badge">📄 Download CV</a>
      </div>
    </div>
  </header>

  <section class="research">
    <h2>Research Statement</h2>
    <p>My research targets robust perception from non‑traditional sensors (structural vibration, seismic) using multi‑modal and contrastive learning techniques. I work on dataset creation, principled feature learning, and deployable real‑time systems for recognition, anomaly detection and cognition estimation.</p>
    <ul class="keywords">
      <li>Signal processing for vibration & seismic sensors</li>
      <li>Contrastive & self-supervised learning</li>
      <li>Embedded ML & real-time inference</li>
      <li>Dataset building & reproducible research</li>
    </ul>
  </section>

  <section class="selected-publications">
    <h2>Selected Publications</h2>
    <ol>
      <li><a href="https://www.nature.com/articles/s41597-025-05517-4" target="_blank">A Structural Vibration-based Dataset for Human Gait Recognition</a>. Nature Scientific Data (2025).</li>
      <li><a href="https://ieeexplore.ieee.org/document/11141764" target="_blank">Deep Multi-Class Novelty Detection in Structural Vibrations with Modified Contrastive Loss</a>. IEEE Trans. Mobile Computing (2025).</li>
      <li><a href="https://ieeexplore.ieee.org/document/10634750" target="_blank">Gaj-Gamini: Detecting Moving Elephants Using Ground Vibration</a>. IEEE Sensors Letters (2024).</li>
      <li><a href="https://ieeexplore.ieee.org/document/10314463" target="_blank">Enhancing Person Identification Through Data Augmentation of Footstep Signals</a>. IEEE Signal Processing Letters (2023).</li>
    </ol>
    <p class="more"><a href="/publications">See full publications / BibTeX</a></p>
  </section>

  <section class="software-data">
    <h2>Software & Data</h2>
    <p>Open datasets and code to reproduce experiments are available. Example:</p>
    <ul>
      <li><a href="https://github.com/Mainak1792/vibegait" target="_blank">VibeGait — gait recognition codebase</a></li>
      <li><a href="https://doi.org/10.6084/m9.figshare..." target="_blank">Structural Vibration Gait Dataset (DOI)</a></li>
    </ul>
  </section>

  <section class="teaching-mentoring">
    <h2>Teaching & Mentoring</h2>
    <p>Guest lectures (JNU), course instructor (Delhi University), supervision of student projects in sensor ML and embedded AI.</p>
  </section>

  <section class="awards">
    <h2>Grants & Awards</h2>
    <ul class="compact-list">
      <li>IEEE SPS Fellowship (2024, 2025)</li>
      <li>PMRF Fellowship (2022–)</li>
      <li>GATE Fellowship (M.Tech)</li>
    </ul>
  </section>

  <section class="contact-cta">
    <p>If you are interested in collaborations, datasets, or student supervision, please <a href="mailto:you@example.com">email me</a>.</p>
  </section>
</div>

<style>
/* Academic / Tech-friendly styles */
.academic-container {
  max-width: 980px;
  margin: 2.2rem auto;
  font-family: "Inter", system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
  color: #1f2937;
  line-height: 1.6;
  background: transparent;
  padding: 1rem;
}

.profile-header {
  display: flex;
  gap: 1.25rem;
  align-items: center;
  margin-bottom: 1.5rem;
  border-bottom: 1px solid #e6e9ee;
  padding-bottom: 1rem;
}

.avatar { width: 96px; height: 96px; border-radius: 8px; object-fit: cover; }

.name { margin: 0; font-size: 1.6rem; color: #0f172a; font-weight: 600; }
.role { margin: 0.25rem 0; color: #334155; }
.affil a { color: #2563eb; text-decoration: none; }

.badges { display:flex; gap:0.5rem; flex-wrap:wrap; margin-top:0.5rem; }
.badge { background:#eef2ff; color:#1e40af; padding:0.35rem 0.6rem; border-radius:8px; font-size:0.9rem; text-decoration:none; }

h2 { color:#0b3b74; font-size:1.2rem; margin-top:1.1rem; margin-bottom:0.5rem; }
.keywords { display:flex; gap:0.75rem; flex-wrap:wrap; list-style:none; padding:0; margin:0.5rem 0; }
.keywords li { background:#f1f5f9; padding:0.25rem 0.6rem; border-radius:999px; font-size:0.9rem; color:#0f172a; }

.selected-publications ol { margin-left:1.1rem; }
.selected-publications li { margin:0.5rem 0; }
.more a { color:#2563eb; text-decoration:none; font-weight:500; }

.compact-list { list-style:none; padding:0; margin:0.5rem 0; display:flex; gap:0.75rem; flex-wrap:wrap; }
.compact-list li { background:#f8fafc; padding:0.35rem 0.6rem; border-radius:8px; font-size:0.9rem; }

.contact-cta { margin-top:1.25rem; padding:0.8rem; background:#fff; border-radius:8px; border:1px solid #eef2f7; }

@media (max-width:768px) {
  .profile-header { flex-direction:row; align-items:center; }
  .avatar { width:80px; height:80px; }
}
</style>
