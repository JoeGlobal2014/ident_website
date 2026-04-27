import re

def fix_video():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
        
    # 1. Kill the infinite loading spinner and make sure the body is transparent
    css_injection = """
    <style>
        /* DESTROY THE WORDPRESS SLIDER SPINNER */
        .tp-loader, .spinner, .preloader, [class*="loader"], .rs-loader { 
            display: none !important; 
            opacity: 0 !important; 
            visibility: hidden !important; 
        }
        /* MAKE SURE BACKGROUNDS DON'T HIDE THE VIDEO */
        body, .wrapper, #page, #main-content, .et_builder_inner_content { 
            background: transparent !important; 
            background-color: transparent !important;
        }
        
        /* FORCE THE VIDEO TO THE VERY BACK */
        #jules-video-bg {
            position: fixed;
            right: 0;
            bottom: 0;
            min-width: 100%;
            min-height: 100%;
            width: auto;
            height: auto;
            z-index: -1000;
            object-fit: cover;
        }
        #jules-dark-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.7);
            z-index: -999;
        }
    </style>
    </head>
    """
    
    if '/* DESTROY THE WORDPRESS SLIDER SPINNER */' not in html:
        html = html.replace('</head>', css_injection, 1)

    # 2. Inject the local video tag pointing to the correct asset
    video_html = """
    <video autoplay loop muted playsinline id="jules-video-bg">
        <source src="assets/asset_cd0f89fe.mp4" type="video/mp4">
    </video>
    <div id="jules-dark-overlay"></div>
    """
    
    # Clean up any old video tags to prevent duplicates
    html = re.sub(r'<video[^>]*id="bg-video"[^>]*>.*?</video>', '', html, flags=re.DOTALL)
    html = re.sub(r'<div style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba\(0, 0, 0, 0\.6\); z-index: -99;"></div>', '', html)
    html = re.sub(r'\s*<video.*?</div>', '', html, flags=re.DOTALL)
    
    # Inject right after the opening body tag
    html = re.sub(r'(<body[^>]*>)', r'\1\n' + video_html, html, count=1)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
        
    print("✅ Successfully injected the local video background: asset_cd0f89fe.mp4!")

if __name__ == "__main__":
    fix_video()