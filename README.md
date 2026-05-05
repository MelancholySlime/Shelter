# SHELTER — Offline Archive Clone

> **⚠️ DISCLAIMER — FOR ARCHIVAL PURPOSES ONLY**
>
> This repository is a **personal offline archive** created solely to preserve a piece of internet history. All content (text, images, code, music, characters) belongs to its respective copyright holders:
> **Porter Robinson**, **Madeon**, and **A-1 Pictures**.
>
> This clone is **non-commercial**, **not affiliated** with any of the above, and is provided **as-is** for personal reference and nostalgia only.
>
> If you are a rights holder and wish this repository removed, please contact me directly. I will comply immediately.

---

This is an offline-capable, static archive of the official SHELTER website. This is kept here purely as a personal memory archive.

## Why Does This Exist?

**SHELTER** — a 2016 animated short produced by Porter Robinson, Madeon, and A-1 Pictures — is a genuinely beautiful piece of art that deserved to be remembered. This archive exists so that the site doesn't disappear entirely from the internet.

All credit goes to Porter Robinson, Madeon, A-1 Pictures, and everyone who worked on this project. This is purely a fan's attempt to keep a piece of internet history alive.

## Project Structure

```
Shelter/
├── index.html              # Main page (all 7 sections, hash-based nav)
├── 404.html                # GitHub Pages SPA fallback
├── .nojekyll               # Prevents Jekyll processing on GitHub Pages
├── README.md               # This file
├── LICENSE                # Legal disclaimer — read it
├── assets/
│   ├── css/
│   │   ├── style.css       # Main styles
│   │   ├── setup.min.css   # Reset/base styles
│   │   └── colorbox.css    # Modal video player styles
│   └── js/
│   │   ├── script.js       # Navigation + animations
│   │   ├── jquery-3.1.1.min.js
│   │   └── jquery.colorbox-min.js
│   └── images/             # All images (38 files)
└── _checkpoint/           # Fetching scripts + raw HTML
```

## Features

- **100% offline capable** — all assets bundled locally
- **GitHub Pages compatible** — `.nojekyll`, `404.html` SPA fallback
- **Hash-based navigation** — all 7 sections navigable via `#section`
- **Full animations preserved** — loading intro, scroll-spy nav, parallax backgrounds
- **jQuery + colorbox modal** — YouTube embed opens in modal lightbox
- **Tracking scripts removed** — Google Analytics + Facebook Pixel stripped

## Sections

| Section | Hash | Content |
|---------|------|---------|
| INTRODUCTION | `#introduction` | English + Japanese intro |
| MOVIE | `#movie` | YouTube embed with colorbox modal |
| STORY | `#story` | English + Japanese plot synopsis |
| CHARACTER | `#character` | Rin + Shigeru profiles + art |
| MUSIC | `#music` | Porter Robinson & Madeon + track info |
| LYRICS | `#lyrics` | Full English + Japanese lyrics |
| STAFF | `#staff` | Full credits |

## Run Locally

### Open directly
Open `index.html` in any modern browser.

### Local HTTP server (recommended)

```bash
cd shelter-clone
python -m http.server 8080
# → Open http://localhost:8080
```

## License

**Please read [LICENSE](LICENSE) before doing anything with this repository.**

In short:
- All original SHELTER content (text, images, characters, music) belongs to **Porter Robinson, Madeon, and A-1 Pictures**.
- This archive is for **personal, non-commercial use only**.
- You **cannot** use this clone to claim ownership of any content.
- You **cannot** sell, redistribute, or profit from this in any way.
- If a rights holder requests removal, I will comply immediately.
