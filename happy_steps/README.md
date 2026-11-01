# Happy Steps — every step says "I'm okay"

足音が「元気だよ」と伝えてくれる

Camera-free care. A geophone on the floor feels footsteps. A small device in the home finds each step, checks who is walking and how, and sends only a tiny JSON summary out of the home. Gemini compares today with the resident's own last 14 days, chooses an action with function calling, writes a kind note in Japanese and English, and speaks to the resident with Gemini text-to-speech.

## Site map

| Page | File |
|---|---|
| Product (landing) | `index.html` |
| How it works | `how-it-works.html` |
| Technology & results | `technology.html` |
| Live demo (working prototype) | `demo.html` |
| Privacy & safety | `privacy.html` |
| About & roadmap | `about.html` |

Shared files: `assets/site.css`, `assets/site.js`, `assets/hero-data.js` (7 s of a real recording for the landing page), `assets/demo.css`, `assets/demo.js` (the prototype engine), `data/walkers.js` (recordings).

## Publish on GitHub Pages

1. Create a public repository, for example `happy-steps`.
2. Upload **everything in this folder** (keep the folders, and the `.nojekyll` file).
3. **Settings → Pages → Deploy from a branch → `main` / root → Save**.
4. The site appears at `https://<your-user>.github.io/happy-steps/` in about a minute.

## Edit the pages

The six HTML pages share one header and footer. To change text, edit `_src/pages.py` (or `_src/demo_body.html` for the demo), then run:

```
python _src/build.py
```

This rewrites the six HTML files in this folder. You can also edit the HTML files directly, but then the next build will overwrite them.

## Real Gemini call

Get a free key at Google AI Studio and paste it on the demo page. The key stays in the visitor's browser and goes only to `generativelanguage.googleapis.com`. Never commit a key to the repository. Without a key, a clearly labelled offline sample is shown.

## Connect a real geophone

```
pip install websockets numpy scipy pyserial
python bridge/geophone_bridge.py --sim
python bridge/geophone_bridge.py --mat Aayushi_wooden_3.mat --fs-in 8000
python bridge/geophone_bridge.py --serial /dev/ttyUSB0 --baud 500000 --fs 1000
```

Then on the demo page choose **Live sensor → Connect** (`ws://localhost:8765`). A page on https can reach `ws://localhost` only, so run the bridge on the same computer as the browser.

`bridge/prepare_data.py` turns `.mat` recordings into `data/walkers.js`.

## Facts and sources used on the landing page

- 7.4 million people aged 65+ lived alone in Japan in 2020; 10.8 million projected by 2050 — National Institute of Population and Social Security Research (reported by The Japan Times, 13 Apr 2024).
- 58,044 people aged 65+ died alone at home in 2024 — National Police Agency (reported by Jiji Press, 2025).
- Research results are from the author's doctoral thesis (lab studies).

This is a research prototype and a care helper, not a medical device. It does not diagnose.
