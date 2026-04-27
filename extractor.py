import os
import re
import base64
import hashlib

def shrink_html_files():
    # Create an assets folder to hold all the extracted images
    assets_dir = 'assets'
    if not os.path.exists(assets_dir):
        os.makedirs(assets_dir)

    # This pattern hunts down the massive base64 text blocks
    pattern = re.compile(r'data:([^;]+);base64,([a-zA-Z0-9+/=]+)')
    
    for filename in os.listdir('.'):
        if filename.endswith('.html'):
            print(f"Scanning {filename} for bloated assets...")
            
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()

            matches = pattern.findall(content)
            if not matches:
                print(f" -> No base64 assets found in {filename}.")
                continue
                
            print(f" -> Extracting {len(matches)} items from {filename}...")

            for mime, b64_data in matches:
                # Figure out the file type (png, jpg, svg, etc.)
                ext = mime.split('/')[-1]
                if '+' in ext:  # Handles things like svg+xml
                    ext = ext.split('+')[0]
                if ext == 'jpeg': 
                    ext = 'jpg'
                
                # Create a short, unique name for the image
                file_hash = hashlib.md5(b64_data.encode('utf-8')).hexdigest()[:8]
                asset_filename = f"asset_{file_hash}.{ext}"
                asset_path = os.path.join(assets_dir, asset_filename)

                # Decode the text and save it as an actual image file
                if not os.path.exists(asset_path):
                    try:
                        with open(asset_path, 'wb') as img_file:
                            img_file.write(base64.b64decode(b64_data))
                    except Exception as e:
                        print(f"    Skipping {asset_filename} due to error: {e}")
                
                # Replace the million-line string in HTML with "assets/asset_name.jpg"
                full_match = f"data:{mime};base64,{b64_data}"
                content = content.replace(full_match, f"{assets_dir}/{asset_filename}")

            # Save the newly shrunken HTML file
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Successfully shrunken: {filename}\n")

if __name__ == "__main__":
    shrink_html_files()