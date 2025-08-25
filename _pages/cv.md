---
layout: archive
title: "Curriculum Vitae"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

<style>
.cv-container {
    max-width: 900px;
    margin: 0 auto;
    padding: 2rem;
    background: #ffffff;
    box-shadow: 0 2px 15px rgba(0,0,0,0.1);
    border-radius: 8px;
}

.cv-header {
    text-align: center;
    margin-bottom: 2rem;
    padding-bottom: 1rem;
    border-bottom: 2px solid #f2f2f2;
}

.cv-header h1 {
    color: #2a2a2a;
    font-size: 2.5em;
    margin-bottom: 0.5rem;
}

.cv-subtitle {
    color: #666;
    font-size: 1.1em;
    margin: 0.5rem 0;
}

.cv-pdf-viewer {
    margin-top: 2rem;
    border-radius: 4px;
    overflow: hidden;
    box-shadow: 0 1px 10px rgba(0,0,0,0.05);
}

.download-btn {
    display: inline-block;
    margin-top: 1rem;
    padding: 0.8rem 1.5rem;
    background: #007bff;
    color: white;
    text-decoration: none;
    border-radius: 4px;
    transition: background 0.3s ease;
}

.download-btn:hover {
    background: #0056b3;
    text-decoration: none;
}
</style>

<div class="cv-container">
  <div class="cv-header">
    <h1>Mainak Chakraborty</h1>
    <p class="cv-subtitle">Last Updated 1st August 2025</p>
    <p class="cv-contact">Indian Institute of Technology Delhi</p>
    
    <div class="cv-pdf-viewer">
      <iframe 
        src="/assets/resume.pdf"
        width="100%"
        height="800px"
        frameborder="0"
        scrolling="auto">
      </iframe>
      <p style="text-align: center;">
        <a href="/assets/resume.pdf" target="_blank" class="download-btn">
          <i class="fas fa-download"></i> Download CV
        </a>
      </p>
    </div>
  </div>
</div>