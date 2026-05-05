"""
Scrapling-based fetcher for sheltertheanimation.com
Fetches fully rendered HTML + downloads all assets
"""
import os
import re
import json
import httpx
from pathlib import Path

BASE_URL = "https://sheltertheanimation.com"
OUTPUT_DIR = Path("D:/O/Shelter/shelter-clone")
ASSETS_DIR = OUTPUT_DIR / "assets" / "images"
CHECKPOINT_DIR = OUTPUT_DIR / "_checkpoint"
CHECKPOINT_DIR.mkdir(parents=True, exist_ok=True)

def get_image_urls_from_html(html: str) -> list[tuple[str, str]]:
    """Extract all image URLs from HTML"""
    # Match src="..." patterns for images
    src_pattern = re.compile(r'src=["\']([^"\']*\.(?:png|jpg|jpeg|gif|webp|svg))["\']', re.IGNORECASE)
    # Match url(...) in CSS
    url_pattern = re.compile(r'url\(["\']?([^"\']*\.(?:png|jpg|jpeg|gif|webp|svg))["\']?\)', re.IGNORECASE)

    urls = []
    for match in src_pattern.finditer(html):
        url = match.group(1)
        if url.startswith('http') or url.startswith('//'):
            urls.append((url, os.path.basename(url)))
        elif not url.startswith('data:'):
            full_url = BASE_URL + ("/" if not url.startswith('/') else "") + url.lstrip('/')
            urls.append((full_url, os.path.basename(url)))

    for match in url_pattern.finditer(html):
        url = match.group(1)
        if url.startswith('http'):
            urls.append((url, os.path.basename(url)))

    return list(set(urls))

def get_css_urls(html: str) -> list[tuple[str, str]]:
    """Extract CSS URLs"""
    href_pattern = re.compile(r'href=["\']([^"\']*\.css[^"\']*)["\']', re.IGNORECASE)
    urls = []
    for match in href_pattern.finditer(html):
        url = match.group(1)
        if url.startswith('http'):
            urls.append((url, os.path.basename(url)))
        elif url.startswith('//'):
            urls.append(("https:" + url, os.path.basename(url)))
        elif not url.startswith('data:'):
            full_url = BASE_URL + ("/" if not url.startswith('/') else "") + url.lstrip('/')
            urls.append((full_url, os.path.basename(url)))
    return urls

def rewrite_html(html: str, downloaded: dict[str, str]) -> str:
    """Rewrite URLs in HTML to point to local assets"""
    # Rewrite absolute URLs to relative
    for original_url, local_path in downloaded.items():
        if original_url in html:
            html = html.replace(original_url, f"assets/images/{local_path}")
    # Rewrite protocol-relative URLs
    html = re.sub(r'src=["\']//(sheltertheanimation\.com[^"\']*)["\']', r'src="https://\1"', html)
    html = re.sub(r'href=["\']//(sheltertheanimation\.com[^"\']*)["\']', r'href="\1"', html)
    return html

def download_file(url: str, dest_path: Path, timeout: int = 30) -> bool:
    """Download a file with retry"""
    try:
        with httpx.Client(timeout=timeout, follow_redirects=True) as client:
            resp = client.get(url)
            if resp.status_code == 200:
                dest_path.parent.mkdir(parents=True, exist_ok=True)
                dest_path.write_bytes(resp.content)
                return True
    except Exception as e:
        print(f"  ERROR downloading {url}: {e}")
    return False

def main():
    from scrapling.fetchers import DynamicFetcher

    print("Fetching sheltertheanimation.com with DynamicFetcher (Playwright)...")
    try:
        fetcher = DynamicFetcher()
        result = fetcher.fetch(BASE_URL, headless=True, network_idle=True, wait_for_timeout=3000)
        html = result.text
    except Exception as e:
        print(f"DynamicFetcher failed: {e}")
        print("Falling back to basic HTTP fetch...")
        with httpx.Client(timeout=30, follow_redirects=True) as client:
            resp = client.get(BASE_URL)
            html = resp.text

    # Save checkpoint
    checkpoint_file = CHECKPOINT_DIR / "fetched.html"
    checkpoint_file.write_text(html, encoding='utf-8')
    print(f"Saved checkpoint: {checkpoint_file}")

    # Get all image URLs
    img_urls = get_image_urls_from_html(html)
    print(f"\nFound {len(img_urls)} image URLs:")
    for url, name in img_urls:
        print(f"  {name} <- {url}")

    # Get CSS URLs
    css_urls = get_css_urls(html)
    print(f"\nFound {len(css_urls)} CSS URLs:")
    for url, name in css_urls:
        print(f"  {name} <- {url}")

    # Download images
    downloaded = {}
    for url, name in img_urls:
        dest = ASSETS_DIR / name
        ok = download_file(url, dest)
        if ok:
            downloaded[url] = name
            print(f"  Downloaded: {name}")
        else:
            # Try alternate path
            pass

    # Download CSS
    css_dir = OUTPUT_DIR / "assets" / "css"
    for url, name in css_urls:
        dest = css_dir / name
        ok = download_file(url, dest)
        if ok:
            downloaded[url] = name
            print(f"  Downloaded CSS: {name}")

    # Rewrite HTML
    rewritten_html = rewrite_html(html, downloaded)
    # Make URLs relative
    rewritten_html = rewritten_html.replace('src="resources/img/', 'src="assets/images/')
    rewritten_html = rewritten_html.replace(BASE_URL + '/', '')

    # Save main HTML
    index_path = OUTPUT_DIR / "index.html"
    index_path.write_text(rewritten_html, encoding='utf-8')
    print(f"\nSaved index.html")

    # Save asset manifest
    manifest = {
        "base_url": BASE_URL,
        "images": [list(x) for x in img_urls],
        "css": [list(x) for x in css_urls],
        "downloaded": downloaded,
    }
    manifest_path = CHECKPOINT_DIR / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    print(f"Saved manifest: {manifest_path}")

    print("\nDone!")

if __name__ == "__main__":
    main()
