import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def scrape_site(url):
    print(f"🚀 Starting deep extraction of: {url}")
    
    # 1. Setup local environment
    if not os.path.exists('assets'):
        os.makedirs('assets')
        
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 2. Extract and Save all Images (including lazy-loaded ones)
        images = soup.find_all('img')
        print(f"📸 Found {len(images)} potential images. Downloading...")
        
        for i, img in enumerate(images):
            # WordPress often hides real URLs in these attributes
            img_url = img.get('data-lazy-src') or img.get('data-src') or img.get('src') or img.get('data-srcset')
            
            if not img_url:
                continue
                
            # Clean the URL (handle srcset strings)
            img_url = img_url.split(' ')[0]
            full_url = urljoin(url, img_url)
            
            try:
                img_data = requests.get(full_url, headers=headers).content
                ext = os.path.splitext(urlparse(full_url).path)[1] or '.jpg'
                # Rename to a consistent asset name
                filename = f"assets/asset_{hash(full_url) & 0xffffffff:08x}{ext}"
                
                with open(filename, 'wb') as f:
                    f.write(img_data)
                # Update the soup object so we can save a "local" version of the HTML
                img['src'] = filename
            except Exception as e:
                print(f"❌ Failed to download {full_url}: {e}")

        # 3. Save the Cleaned HTML and Text Structure
        with open('scraped_structure.txt', 'w', encoding='utf-8') as f:
            f.write("--- HEADINGS ---\n")
            for h in soup.find_all(['h1', 'h2', 'h3', 'h4']):
                f.write(f"[{h.name}] {h.get_text(strip=True)}\n")
            
            f.write("\n--- FULL PAGE CONTENT ---\n")
            f.write(soup.get_text(separator='\n', strip=True))

        print("✅ Extraction Complete! Check the 'assets' folder and 'scraped_structure.txt'.")

    except Exception as e:
        print(f"💥 Fatal Error: {e}")

if __name__ == "__main__":
    target = "https://independent.checkmynewsite.com/services/"
    scrape_site(target)