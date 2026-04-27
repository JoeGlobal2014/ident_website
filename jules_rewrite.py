import os
import re

# The target pages and the text on the buttons
targets = {
    'ABOUT': 'about.html',
    'SERVICES': 'services.html',
    'GALLERY': 'gallery.html',
    'CONTACT': 'contacts.html',
    'HOME': 'index.html'
}

# This script is injected to kill the WordPress JavaScript hijacking
js_override = """
<script>
// JULES OVERRIDE SCRIPT: Forces links to work
document.addEventListener('click', function(e) {
    let link = e.target.closest('a');
    if(link && link.hasAttribute('data-jules')) {
        e.preventDefault();
        e.stopPropagation(); // Stops WordPress from freezing the click
        window.location.href = link.getAttribute('href');
    }
}, true);
</script>
</body>
"""

def rewrite_site():
    for filename in os.listdir('.'):
        if filename.endswith('.html'):
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()

            # 1. Rewrite the menu buttons based on what they say
            for label, html_file in targets.items():
                pattern = rf'<a([^>]*)href="[^"]*"([^>]*)>([^<]*{label}[^<]*)</a>'
                replacement = rf'<a\1href="{html_file}" data-jules="true"\2>\3</a>'
                content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)

            # 2. Rewrite the Logo image link to go to Home
            logo_pattern = r'<a([^>]*)href="[^"]*"([^>]*)>(\s*<img[^>]*alt="IndepenDent[^>]*>\s*)</a>'
            content = re.sub(logo_pattern, rf'<a\1href="index.html" data-jules="true"\2>\3</a>', content, flags=re.IGNORECASE)

            # 3. Inject the Override script at the bottom of the page
            if 'data-jules' not in content: # Prevents double-injecting
                content = content.replace('</body>', js_override)

            # Save the rewritten file
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Rewrite complete for: {filename}")

if __name__ == "__main__":
    rewrite_site()