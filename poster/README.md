# What a footstep sounds like to a floor

Interactive page: geophone footstep recordings you can see, zoom into, view as a
Morlet wavelet scalogram or spectrogram, and listen to.

## 1. Arrange the recordings

    data/environment/e1/   one .mat file   (same walker on floor 1)
    data/environment/e2/   one .mat file   (same walker on floor 2)
    data/environment/e3/   one .mat file   (same walker on floor 3)
    data/gender/male/      one .mat file   (same floor as female)
    data/gender/female/    one .mat file

If a folder has several files, the first one alphabetically is used. Open
prepare_data.py and edit GROUPS to choose a file, rename the floors
(e.g. "Wooden floor"), or change how many seconds are kept (MAX_SECONDS).

## 2. Build the data

    pip install numpy scipy
    python prepare_data.py

This writes assets/environment.js and assets/gender.js.

## 3. Put it online (GitHub Pages)

Upload index.html, assets/, .gitignore and prepare_data.py. Do not upload data/:
.gitignore already keeps the raw recordings out of git.
Then Settings → Pages → Deploy from a branch → main → / (root).

## Presenting

Space plays all, 1–5 plays one recording, B toggles blind listening.
index.html also works offline straight from a USB stick.
