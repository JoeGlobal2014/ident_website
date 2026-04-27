import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scrape_services_page(url):
    # Setup directory for images
    if not os.path.exists('assets'):
        os.makedirs('assets')

    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve page: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    
    print(f"--- Scraping Report for: {url} ---\n")

    # 1. Extract Headers
    print("HEADERS FOUND:")
    headers = soup.find_all(['h1', 'h2', 'h3', 'h4'])
    for h in headers:
        print(f"[{h.name}]: {h.get_text(strip=True)}")

    # 2. Extract Paragraphs / Text Content
    print("\nTEXT CONTENT:")
    paragraphs = soup.find_all(['p', 'li'])
    for p in paragraphs:
        text = p.get_text(strip=True)
        if text:
            print(f"- {text}")

    # 3. Extract and Download Images
    print("\nIMAGES FOUND & DOWNLOADING:")
    images = soup.find_all('img')
    for img in images:
        img_url = img.get('src')
        if not img_url:
            continue
            
        # Handle relative URLs
        full_img_url = urljoin(url, img_url)
        img_name = os.path.basename(full_img_url.split('?')[0])
        
        if not img_name:
            continue

        try:
            img_data = requests.get(full_img_url).content
            with open(f'assets/{img_name}', 'wb') as handler:
                handler.write(img_data)
            print(f"Successfully downloaded: {img_name}")
        except Exception as e:
            print(f"Could not download {img_name}: {e}")

if __name__ == "__main__":
    target_url = "https://independent.checkmynewsite.com/services/"
    scrape_services_page(target_url)