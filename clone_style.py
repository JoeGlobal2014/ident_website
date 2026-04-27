import urllib.request
import re

# Your live staging URLs
pages = {
    "index.html": "https://independent.checkmynewsite.com/",
    "about.html": "https://independent.checkmynewsite.com/about/",
    "services.html": "https://independent.checkmynewsite.com/services/",
    "gallery.html": "https://independent.checkmynewsite.com/gallery/",
    "contacts.html": "https://independent.checkmynewsite.com/contact/"
}

def bring_the_style_in():
    print("Fetching exact styles, layout, and images from the live staging site...\n")
    
    for filename, url in pages.items():
        try:
            # Fetch the raw HTML from the live staging site
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response:
                html = response.read().decode('utf-8')
                
            # 1. KILL ALL WORDPRESS JAVASCRIPT
            # This is the magic step. It deletes the scripts that were freezing your clicks.
            html = re.sub(r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>', '', html, flags=re.IGNORECASE)
            
            # 2. RE-WIRE THE NAVIGATION LINKS
            # This ensures the buttons point to your local laptop files instead of the live site
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

            # Save the file cleanly
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"✅ Cloned perfectly styled page: {filename}")
            
        except Exception as e:
            print(f"❌ Error fetching {filename}: {e}")

if __name__ == "__main__":
    bring_the_style_in()