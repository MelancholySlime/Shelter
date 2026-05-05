"""
Download all assets from sheltertheanimation.com
"""
import os
import httpx
from pathlib import Path

BASE_URL = "https://sheltertheanimation.com"
OUTPUT_DIR = Path("D:/O/Shelter/shelter-clone")
IMG_DIR = OUTPUT_DIR / "assets" / "images"
CSS_DIR = OUTPUT_DIR / "assets" / "css"
JS_DIR = OUTPUT_DIR / "assets" / "js"

for d in [IMG_DIR, CSS_DIR, JS_DIR]:
    d.mkdir(parents=True, exist_ok=True)

def download(url: str, dest: Path) -> bool:
    try:
        resp = httpx.get(url, timeout=30, follow_redirects=True)
        if resp.status_code == 200:
            dest.write_bytes(resp.content)
            print(f"  OK  {dest.name} ({len(resp.content):,} bytes)")
            return True
        else:
            print(f"  FAIL {url} -> {resp.status_code}")
    except Exception as e:
        print(f"  ERROR {url}: {e}")
    return False

# CSS files
css_files = [
    "resources/css/lib/colorbox.css",
    "resources/css/setup.min.css",
    "resources/css/style.css",
]
print("=== Downloading CSS ===")
for f in css_files:
    url = f"{BASE_URL}/{f}"
    dest = CSS_DIR / os.path.basename(f)
    download(url, dest)

# JS files
js_files = [
    "resources/js/lib/jquery-3.1.1.min.js",
    "resources/js/lib/jquery.colorbox-min.js",
    "resources/js/script.js",
]
print("\n=== Downloading JS ===")
for f in js_files:
    url = f"{BASE_URL}/{f}"
    dest = JS_DIR / os.path.basename(f)
    download(url, dest)

# Image files
img_files = [
    "resources/img/logo_s.png",
    "resources/img/mv_bg.jpg",
    "resources/img/head_introduction.png",
    "resources/img/img_movie.jpg",
    "resources/img/head_movie.png",
    "resources/img/head_story.png",
    "resources/img/name_rin.png",
    "resources/img/pct_rin1.png",
    "resources/img/pct_rin2.png",
    "resources/img/pct_rin3.png",
    "resources/img/pct_rin.png",
    "resources/img/head_character.png",
    "resources/img/pct_shigeru.png",
    "resources/img/name_shigeru.png",
    "resources/img/pct_shigeru1.png",
    "resources/img/pct_shigeru2.png",
    "resources/img/head_artist.png",
    "resources/img/pct_artist.jpg",
    "resources/img/head_music.png",
    "resources/img/head_music2.png",
    "resources/img/pct_music.jpg",
    "resources/img/head_lyrics.png",
    "resources/img/head_staff.png",
    "resources/img/head_cast.png",
    "resources/img/pct_misawa.jpg",
    "resources/img/ogp.png",
]
print("\n=== Downloading Images ===")
for f in img_files:
    url = f"{BASE_URL}/{f}"
    dest = IMG_DIR / os.path.basename(f)
    download(url, dest)

print("\nDone!")
