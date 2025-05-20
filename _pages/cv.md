---
layout: archive
title: "Curriculum Vitae"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

<div class="cv-container">
  <div class="cv-header">
    <h1>Mainak Chakraborty</h1>
    <p class="cv-subtitle">Ph.D. Candidate in Multi-Modal Gait Recognition</p>
    <p class="cv-contact">Indian Institute of Technology Delhi</p>
    <div class="cv-download">
      <a href="https://drive.google.com/file/d/1hspu7UHovxWJ4525ijE_H3uQ8TbArUNw/view?usp=sharing" class="btn btn--primary">
        <i class="fas fa-download"></i> Download Full CV
      </a>
    </div>
  </div>

  <section class="cv-section">
    <h2><i class="fas fa-graduation-cap"></i> Education</h2>
    <div class="cv-timeline">
      <div class="cv-timeline-item">
        <div class="cv-timeline-content">
          <h3>Ph.D. in Multi-Modal Gait Recognition</h3>
          <p class="cv-institution">Indian Institute of Technology Delhi (IIT Delhi)</p>
          <p class="cv-date">Expected 2025</p>
        </div>
      </div>
      <div class="cv-timeline-item">
        <div class="cv-timeline-content">
          <h3>M.Tech.</h3>
          <p class="cv-institution">Indian Institute of Engineering Science and Technology, Shibpur (IIEST)</p>
          <p class="cv-date">2021</p>
        </div>
      </div>
    </div>
  </section>

  <section class="cv-section">
    <h2><i class="fas fa-award"></i> Scholarships & Awards</h2>
    <div class="cv-grid">
      <div class="cv-card">
        <h3>PMRF Scholarship</h3>
        <p>Top 0.5% among 212,568 candidates (India)</p>
        <span class="cv-year">2022</span>
      </div>
      <div class="cv-card">
        <h3>GATE Fellowship</h3>
        <p>Top 6% among 167,376 candidates (India)</p>
        <span class="cv-year">2019</span>
      </div>
      <div class="cv-card">
        <h3>ASDC Scholarship</h3>
        <p>Top 1% among the batch (India)</p>
        <span class="cv-year">2015</span>
      </div>
      <div class="cv-card">
        <h3>IEEE SPS Scholarship</h3>
        <p>IEEE Signal Processing Society Scholarship recipient (USA)</p>
        <span class="cv-year">2024</span>
      </div>
    </div>
  </section>

  <section class="cv-section">
    <h2><i class="fas fa-book"></i> Publications</h2>
    <div class="publications-container">
      <h3>Journal Articles</h3>
      <div class="publications-list">
        {% for post in site.publications reversed %}
          {% if post.venue_type == 'journal' %}
            {% include archive-single-cv.html %}
          {% endif %}
        {% endfor %}
      </div>

      <h3>Conference Papers</h3>
      <div class="publications-list">
        {% for post in site.publications reversed %}
          {% if post.venue_type == 'conference' %}
            {% include archive-single-cv.html %}
          {% endif %}
        {% endfor %}
      </div>
    </div>
  </section>

  <section class="cv-section">
    <h2><i class="fas fa-chalkboard-teacher"></i> Teaching Experience</h2>
    <p class="teaching-intro">Dedicated to fostering academic excellence through innovative teaching methods and practical learning approaches.</p>
    <div class="teaching-list">
      {% for post in site.teaching reversed %}
        {% include archive-single-cv.html %}
      {% endfor %}
    </div>
  </section>

  <section class="cv-section">
    <h2><i class="fas fa-code"></i> Technical Skills</h2>
    <div class="skills-container">
      <div class="skills-category">
        <h3>Programming Languages</h3>
        <div class="skills-tags">
          <span class="skill-tag">Python</span>
          <span class="skill-tag">C/C++</span>
          <span class="skill-tag">C#</span>
          <span class="skill-tag">Embedded C</span>
          <span class="skill-tag">CUDA</span>
          <span class="skill-tag">MATLAB</span>
        </div>
      </div>
      <div class="skills-category">
        <h3>Tools & Technologies</h3>
        <div class="skills-tags">
          <span class="skill-tag">TensorFlow</span>
          <span class="skill-tag">PyTorch</span>
          <span class="skill-tag">Docker</span>
          <span class="skill-tag">OpenCV</span>
          <span class="skill-tag">Git</span>
          <span class="skill-tag">LaTeX</span>
        </div>
      </div>
    </div>
  </section>

  <section class="cv-section">
    <h2><i class="fas fa-certificate"></i> Certifications</h2>
    <div class="certifications-list">
      <div class="certification-item">
        <h3>TensorFlow Developer Certificate</h3>
        <p>ID: 87883013</p>
        <span class="cert-year">2023</span>
      </div>
      <div class="certification-item">
        <h3>Associate Member of the Institution of Engineers (AMIE)</h3>
        <p>ID: AM3115693</p>
        <span class="cert-year">2023</span>
      </div>
      <div class="certification-item">
        <h3>Deeplearning.ai TensorFlow Developer</h3>
        <span class="cert-year">2021</span>
      </div>
    </div>
  </section>

  <section class="cv-section">
    <h2><i class="fas fa-hands-helping"></i> Service & Leadership</h2>
    <div class="service-list">
      <div class="service-item">
        <h3>Youth Ideathon 2024</h3>
        <p>Mentor at India's largest high-school-level competition of ideas</p>
        <span class="service-year">2024-continuing</span>
      </div>
      <div class="service-item">
        <h3>Hindu College, Deep Learning Workshop</h3>
        <p>Conducted AtoZ workshop for Delhi University Students</p>
        <span class="service-year">2023</span>
      </div>
      <div class="service-item">
        <h3>IIEST Covid‑19 Volunteering Team</h3>
        <p>Active volunteer during the pandemic</p>
        <span class="service-year">2020</span>
      </div>
    </div>
  </section>
</div>

<style>
.cv-container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 2rem;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
}

.cv-header {
  text-align: center;
  margin-bottom: 3rem;
  padding-bottom: 2rem;
  border-bottom: 2px solid #eee;
}

.cv-header h1 {
  font-size: 2.5rem;
  margin-bottom: 0.5rem;
  color: #2a7ae2;
}

.cv-subtitle {
  font-size: 1.2rem;
  color: #666;
  margin-bottom: 0.5rem;
}

.cv-contact {
  color: #888;
  margin-bottom: 1.5rem;
}

.cv-download {
  margin-top: 1rem;
}

.cv-section {
  margin-bottom: 3rem;
}

.cv-section h2 {
  color: #2a7ae2;
  border-bottom: 2px solid #eee;
  padding-bottom: 0.5rem;
  margin-bottom: 1.5rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.cv-timeline {
  position: relative;
  padding-left: 2rem;
}

.cv-timeline-item {
  position: relative;
  margin-bottom: 2rem;
}

.cv-timeline-item::before {
  content: '';
  position: absolute;
  left: -2rem;
  top: 0;
  width: 1px;
  height: 100%;
  background: #eee;
}

.cv-timeline-content {
  background: #f8f9fa;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

.cv-timeline-content h3 {
  margin: 0 0 0.5rem;
  color: #333;
}

.cv-institution {
  color: #666;
  margin-bottom: 0.25rem;
}

.cv-date {
  color: #888;
  font-size: 0.9rem;
}

.cv-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
}

.cv-card {
  background: #f8f9fa;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

.cv-card h3 {
  margin: 0 0 0.5rem;
  color: #333;
}

.cv-year {
  display: inline-block;
  background: #2a7ae2;
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 4px;
  font-size: 0.9rem;
  margin-top: 0.5rem;
}

.publications-container {
  display: grid;
  gap: 2rem;
}

.publications-list {
  background: #f8f9fa;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

.teaching-intro {
  font-size: 1.1rem;
  color: #666;
  margin-bottom: 1.5rem;
  font-style: italic;
}

.skills-container {
  display: grid;
  gap: 2rem;
}

.skills-category {
  background: #f8f9fa;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

.skills-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-top: 1rem;
}

.skill-tag {
  background: #2a7ae2;
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  font-size: 0.9rem;
}

.certifications-list, .service-list {
  display: grid;
  gap: 1.5rem;
}

.certification-item, .service-item {
  background: #f8f9fa;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}

.certification-item h3, .service-item h3 {
  margin: 0 0 0.5rem;
  color: #333;
}

.cert-year, .service-year {
  display: inline-block;
  background: #2a7ae2;
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 4px;
  font-size: 0.9rem;
  margin-top: 0.5rem;
}

@media (max-width: 768px) {
  .cv-container {
    padding: 1rem;
  }
  
  .cv-grid {
    grid-template-columns: 1fr;
  }
  
  .skills-tags {
    flex-direction: column;
  }
  
  .skill-tag {
    width: 100%;
    text-align: center;
  }
}
</style>