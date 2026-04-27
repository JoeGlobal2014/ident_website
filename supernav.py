import os

# This script forces the browser to read the text of the links and route them manually,
# while completely destroying the WordPress/SingleFile click-blockers.
js_force_nav = """
<script>
document.addEventListener("DOMContentLoaded", function() {
    const allLinks = document.querySelectorAll("a");
    
    allLinks.forEach(link => {
        const text = link.innerText.toUpperCase().trim();
        
        // Re-route the links based on what the button says
        if (text === "ABOUT") link.href = "about.html";
        if (text === "SERVICES") link.href = "services.html";
        if (text === "GALLERY") link.href = "gallery.html";
        if (text === "CONTACT" || text === "CONTACTS") link.href = "contacts.html";
        if (text === "HOME") link.href = "index.html";
        
        // If it's a navigation link, FORCE the click to happen
        if (["HOME", "ABOUT", "SERVICES", "GALLERY", "CONTACT", "CONTACTS"].includes(text)) {
            link.addEventListener("click", function(e) {
                e.preventDefault();
                e.stopImmediatePropagation(); // Kills the WordPress blocker instantly
                window.location.href = link.href;
            }, true);
        }
    });
});
</script>
</body>
"""

def fix_all_navigation():
    for filename in os.listdir('.'):
        if filename.endswith('.html'):
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Inject the sledgehammer script right before the end of the body
            if 'stopImmediatePropagation' not in content:
                content = content.replace('</body>', js_force_nav)
                
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ Sledgehammer navigation applied to: {filename}")
            else:
                print(f"⏩ Already applied to {filename}")

if __name__ == "__main__":
    fix_all_navigation()
    