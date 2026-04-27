import re

def build_hero():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. NUKE THE BROKEN WORDPRESS SLIDER
    html = re.sub(r'<rs-module-wrap.*?</rs-module-wrap>', '', html, flags=re.DOTALL|re.IGNORECASE)
    html = re.sub(r'<p class="rs-p-wp-fix".*?</p>', '', html, flags=re.IGNORECASE)
    
    # Clean up our previous video injection attempt
    html = re.sub(r'.*?</div>', '', html, flags=re.DOTALL)

    # 2. CREATE A CLEAN, JAVASCRIPT-FREE HERO SECTION
    hero_section = """
    <div style="position: relative; width: 100%; min-height: 80vh; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; overflow: hidden; padding: 2rem; border-bottom: 2px solid #222;">
        
        <video autoplay loop muted playsinline style="position: absolute; top: 50%; left: 50%; min-width: 100%; min-height: 100%; width: auto; height: auto; z-index: 1; transform: translate(-50%, -50%); object-fit: cover;">
            <source src="assets/asset_cd0f89fe.mp4" type="video/mp4">
        </video>
        
        <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.65); z-index: 2;"></div>

        <div style="position: relative; z-index: 3; max-width: 1100px; margin: 0 auto;">
            <h3 style="color: #a3e635; font-size: 1.6rem; font-weight: 700; margin-bottom: 1.5rem; font-style: italic; font-family: sans-serif; text-shadow: 1px 1px 3px rgba(0,0,0,0.8);">
                Trade-Only PDR Services. Reliable. Precise. Fast Turnaround.
            </h3>
            <h1 style="color: #ffffff; font-size: 4rem; font-weight: 800; line-height: 1.1; text-transform: uppercase; margin: 0 auto; font-family: sans-serif; text-shadow: 2px 2px 5px rgba(0,0,0,0.8);">
                PAINTLESS DENT REPAIR FOR BODY SHOPS, DEALERS & WHOLESALE ACCOUNTS.
            </h1>
        </div>
    </div>
    """

    # 3. INJECT THE NEW HERO RIGHT AFTER THE HEADER
    if '</header>' in html:
        html = re.sub(r'(</header>)', r'\1\n' + hero_section, html, count=1, flags=re.IGNORECASE)
    else:
        html = re.sub(r'(<body[^>]*>)', r'\1\n' + hero_section, html, count=1, flags=re.IGNORECASE)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

    print("✅ Broken slider deleted and clean Hero section installed!")

if __name__ == "__main__":
    build_hero()