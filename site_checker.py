import requests
from bs4 import BeautifulSoup
from Wappalyzer import Wappalyzer, WebPage
from urllib.parse import urljoin, urlparse
import re

# Vulnerable/outdated library list (sample)
VULNERABLE_LIBS = {
    "jquery": ["1.7", "1.8", "1.9", "1.10", "2.0", "2.1"],  # Example outdated
    "angular": ["1.2", "1.3", "1.4"],                      # Legacy AngularJS
    "react": ["15.0", "15.1"],                             # Old React versions
}

visited = set()
all_links = set()

def crawl_site(url, max_depth=2):
    """Recursively crawl a site and collect links."""
    if url in visited or max_depth == 0:
        return
    visited.add(url)
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return
        
        soup = BeautifulSoup(response.text, "html.parser")
        for link in soup.find_all("a", href=True):
            full_link = urljoin(url, link["href"])
            if urlparse(full_link).netloc == urlparse(url).netloc:
                all_links.add(full_link)
                crawl_site(full_link, max_depth - 1)
    except Exception as e:
        print(f"Error crawling {url}: {e}")

def detect_technologies(url):
    """Detect site technologies (using Wappalyzer)."""
    try:
        webpage = WebPage.new_from_url(url)
        wappalyzer = Wappalyzer.latest()
        techs = wappalyzer.analyze(webpage)
        return techs
    except Exception as e:
        print(f"Error detecting technologies: {e}")
        return []

def find_js_versions(url):
    """Look for JS library versions on the site."""
    js_versions = {}
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return js_versions
        
        scripts = re.findall(r'src=["\']([^"\']+\.js)', response.text)
        for script in scripts:
            for lib, bad_versions in VULNERABLE_LIBS.items():
                if lib in script.lower():
                    match = re.search(r'(\d+\.\d+(\.\d+)?)', script)
                    if match:
                        version = match.group(1)
                        js_versions[lib] = version
    except Exception as e:
        print(f"Error checking JS versions on {url}: {e}")
    return js_versions

def analyze_site(target_url):
    print(f"[*] Crawling site: {target_url}")
    crawl_site(target_url, max_depth=2)
    
    print(f"\n[*] Found {len(all_links)} internal links.")
    
    print("\n[*] Detecting technologies...")
    techs = detect_technologies(target_url)
    print(f"Technologies: {techs}")
    
    print("\n[*] Checking JS library versions...")
    for link in all_links:
        js_libs = find_js_versions(link)
        for lib, version in js_libs.items():
            status = "⚠ OUTDATED" if version in VULNERABLE_LIBS.get(lib, []) else "OK"
            print(f"{lib} - version {version} on {link} => {status}")
    
    print("\n[+] Scan complete.")

if __name__ == "__main__":
    target = input("Enter the website URL (with http/https): ")
    analyze_site(target)
