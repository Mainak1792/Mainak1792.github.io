"""Build the Happy Steps static site: shared header/footer + page bodies."""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from pages import PAGES

OUT = pathlib.Path(__file__).resolve().parent.parent

LOGO = """<svg viewBox="0 0 32 32" aria-hidden="true"><defs><linearGradient id="{id}" x1="0" y1="0" x2="1" y2="1">
<stop offset="0" stop-color="#1A73E8"/><stop offset="1" stop-color="#1E8E3E"/></linearGradient></defs>
<rect width="32" height="32" rx="9" fill="url(#{id})"/>
<ellipse cx="11.6" cy="12.4" rx="3.1" ry="4.9" fill="#fff" transform="rotate(-14 11.6 12.4)"/>
<ellipse cx="20.4" cy="15.6" rx="3.1" ry="4.9" fill="#fff" fill-opacity=".82" transform="rotate(14 20.4 15.6)"/>
<path d="M10.2 24.2q5.8 3.4 11.6 0" stroke="#fff" stroke-width="2.2" fill="none" stroke-linecap="round"/></svg>"""

FAVICON = ("data:image/svg+xml," + LOGO.format(id="f").replace("\n", "").replace("#", "%23")
           .replace('"', "'").replace("<", "%3C").replace(">", "%3E"))

NAV = [("index.html", "Product"), ("how-it-works.html", "How it works"), ("technology.html", "Technology"),
       ("demo.html", "Live demo"), ("privacy.html", "Privacy & safety"), ("about.html", "About")]

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta name="theme-color" content="#ffffff">
<link rel="icon" href="{favicon}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto+Flex:opsz,wght@8..144,300..700&family=Roboto+Mono:wght@400;500&family=Noto+Sans+JP:wght@400;500&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Google+Sans+Flex:opsz,wght@6..144,300..700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css">
{extra_head}
</head>
<body>
<a class="sr" href="#main">Skip to content</a>
<header class="appbar">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="Happy Steps home">{logo}<span>Happy Steps</span></a>
    <nav class="nav" aria-label="Main">{nav}</nav>
    <a class="btn btn-primary cta" href="demo.html">Try the live demo</a>
    <button class="menu-btn" aria-label="Menu" aria-expanded="false"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
  </div>
</header>
<main id="main">
"""

FOOT = """
</main>
<footer class="footer">
  <div class="wrap">
    <div class="cols">
      <div>
        <a class="brand" href="index.html">{logo}<span>Happy Steps</span></a>
        <p class="about">Camera-free care that turns everyday footsteps into kind words for the family. Built on floor-vibration research and the Gemini API.</p>
        <p class="about ja" style="margin-top:6px">足音を、家族へのやさしい言葉に。</p>
      </div>
      <div><h4>Product</h4><ul>
        <li><a href="index.html">Overview</a></li><li><a href="how-it-works.html">How it works</a></li>
        <li><a href="demo.html">Live demo</a></li></ul></div>
      <div><h4>Research</h4><ul>
        <li><a href="technology.html">Technology</a></li><li><a href="technology.html#results">Results</a></li>
        <li><a href="technology.html#limits">Limits</a></li></ul></div>
      <div><h4>Company</h4><ul>
        <li><a href="about.html">About</a></li><li><a href="privacy.html">Privacy &amp; safety</a></li>
        <li><a href="https://mainakchakraborty.com">Contact</a></li></ul></div>
    </div>
    <div class="legal">
      <span>© 2026 Happy Steps · Mainak Chakraborty. A research prototype, not a medical device.</span>
      <span>Built with Gemini and Google AI Studio · Google AI Challenge 2026 entry</span>
    </div>
  </div>
</footer>
{scripts}
<script src="assets/site.js"></script>
</body>
</html>
"""


def build():
    for p in PAGES:
        nav = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == p["file"] else ""}>{t}</a>' for h, t in NAV)
        html = (HEAD.format(title=p["title"], desc=p["desc"], favicon=FAVICON, extra_head=p.get("head", ""),
                            logo=LOGO.format(id="lg-h"), nav=nav)
                + p["body"]
                + FOOT.format(logo=LOGO.format(id="lg-f"), scripts=p.get("scripts", "")))
        (OUT / p["file"]).write_text(html, encoding="utf-8")
        print("wrote", p["file"], len(html))


if __name__ == "__main__":
    build()
