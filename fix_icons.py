import os

# This CSS forces any social or footer images to behave, stay small, and line up.
css_fix = """
<style>
    /* Jules Social Icon Fix */
    footer img, .footer img, [class*="social"] img, a[href*="facebook.com"] img, a[href*="instagram.com"] img {
        max-width: 35px !important;
        max-height: 35px !important;
        width: auto !important;
        height: auto !important;
        display: inline-block !important;
        margin: 0 10px !important;
        vertical-align: middle !important;
    }
</style>
</head>
"""

def fix_social_icons():
    for filename in os.listdir('.'):
        if filename.endswith('.html'):
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Inject the CSS right before the closing </head> tag
            if '/* Jules Social Icon Fix */' not in content:
                content = content.replace('</head>', css_fix)
                
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ Applied icon fix to: {filename}")

if __name__ == "__main__":
    fix_social_icons()