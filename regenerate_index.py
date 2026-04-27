import urllib.request
import re

def regenerate_index():
    url = "https://independent.checkmynewsite.com/"
    print("Fetching index.html from live staging...")
    
    # Download the live page
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        
    # 1. KILL ALL WORDPRESS JAVASCRIPT (Fixes the clicks)
    html = re.sub(r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>', '', html, flags=re.IGNORECASE)
    
    # 2. RE-WIRE THE NAVIGATION LINKS
    replacements = {
        'href="https://independent.checkmynewsite.com/"': 'href="index.html"',
        'href="https://independent.checkmynewsite.com"': 'href="index.html"',
        'href="https://independent.checkmynewsite.com/about/"': 'href="about.html"',
        'href="https://independent.checkmynewsite.com/about"': 'href="about.html"',
        'href="/about/"': 'href="about.html"',
        'href="/about"': 'href="about.html"',
        'href="https://independent.checkmynewsite.com/services/"': 'href="services.html"',
        'href="https://independent.checkmynewsite.com/services"': 'href="services.html"',
        'href="/services/"': 'href="services.html"',
        'href="/services"': 'href="services.html"',
        'href="https://independent.checkmynewsite.com/gallery/"': 'href="gallery.html"',
        'href="https://independent.checkmynewsite.com/gallery"': 'href="gallery.html"',
        'href="/gallery/"': 'href="gallery.html"',
        'href="/gallery"': 'href="gallery.html"',
        'href="https://independent.checkmynewsite.com/contact/"': 'href="contacts.html"',
        'href="https://independent.checkmynewsite.com/contact"': 'href="contacts.html"',
        'href="/contact/"': 'href="contacts.html"',
        'href="/contact"': 'href="contacts.html"'
    }
    for old, new in replacements.items():
        html = html.replace(old, new)
        
    # 3. FIX THE LIGHTNING VIDEO BACKGROUND
    # This points the code directly to the actual video file on the live server
    video_url = "https://independent.checkmynewsite.com/wp-content/uploads/2026/04/20260427-0433-47.6823325.mp4"
    html = re.sub(r'src="[^"]*20260427-0433-47\.6823325\.mp4"', f'src="{video_url}"', html)
    
    # 4. ADD THE DARK OVERLAY
    # This injects a dark, semi-transparent layer over the lightning so the text is readable
    overlay = '\n<div style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0, 0, 0, 0.6); z-index: -99;"></div>\n'
    html = html.replace('</video>', f'</video>{overlay}')
    
    # Save the perfected file
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
        
    print("✅ index.html has been completely regenerated with the lightning video working!")

if __name__ == "__main__":
    regenerate_index()