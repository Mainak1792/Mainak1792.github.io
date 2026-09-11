# What a footstep sounds like to a floor

Interactive page: geophone footstep recordings you can see, zoom into and listen to.

## Put it online (GitHub Pages)
1. Create a public repo, e.g. `footsteps`.
2. Upload `index.html` and the `data/` folder (keep the folder structure).
3. Settings → Pages → Source: "Deploy from a branch", branch `main`, folder `/ (root)`.
4. After a minute the page is at `https://<your-username>.github.io/footsteps/`.

## Use other recordings
Put your `.mat` files (variable `geo_data`, 8 kHz) next to `prepare_data.py`,
edit the `WALKERS` list, run `python prepare_data.py`, and re-upload `data/walkers.js`.
Raw `.mat` files never need to go on GitHub.

## Presenting
Space = play both, 1 / 2 = one walker, B = blind listening (hides who is who).
The page works offline too: open index.html directly from a USB stick.
