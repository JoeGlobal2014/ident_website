import os

# This is the master layout using Tailwind CSS for a clean, modern design.
# It ensures perfectly working navigation with absolutely zero JavaScript hijacking.
html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | IndepenDent Technician</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-900 text-gray-100 font-sans flex flex-col min-h-screen">

    <header class="bg-black border-b border-cyan-600 sticky top-0 z-50">
        <div class="container mx-auto px-6 py-4 flex justify-between items-center">
            <a href="index.html" class="text-3xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-blue-600">
                IndepenDent
            </a>
            <nav>
                <ul class="flex space-x-8 text-sm font-bold tracking-wider">
                    <li><a href="index.html" class="hover:text-cyan-400 transition">HOME</a></li>
                    <li><a href="about.html" class="hover:text-cyan-400 transition">ABOUT</a></li>
                    <li><a href="services.html" class="hover:text-cyan-400 transition">SERVICES</a></li>
                    <li><a href="gallery.html" class="hover:text-cyan-400 transition">GALLERY</a></li>
                    <li><a href="contacts.html" class="hover:text-cyan-400 transition">CONTACT</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <main class="flex-grow container mx-auto px-6 py-12">
        <div class="max-w-4xl mx-auto">
            <h1 class="text-5xl font-bold mb-8 text-white border-l-4 border-cyan-500 pl-4">
                {heading}
            </h1>
            <div class="bg-gray-800 p-8 rounded-xl shadow-2xl border border-gray-700 text-lg leading-relaxed">
                {content}
            </div>
        </div>
    </main>

    <footer class="bg-black border-t border-gray-800 py-8 mt-auto">
        <div class="container mx-auto px-6 text-center text-gray-500 text-sm">
            <p>&copy; 2026 IndepenDent Technician. Lafayette, LA. All rights reserved.</p>
        </div>
    </footer>

</body>
</html>
"""

# The unique content for each of the 5 pages
pages = {
    "index.html": {
        "title": "Home",
        "heading": "Precision Paintless Dent Repair",
        "content": """
            <p class="mb-6">Welcome to the new, lightning-fast IndepenDent Technician portal. Your website is now running on pure HTML and Tailwind CSS.</p>
            <p class="text-cyan-400"><strong>Next Step:</strong> You can drop your background video and hero images directly into this file.</p>
        """
    },
    "about.html": {
        "title": "About",
        "heading": "About IndepenDent",
        "content": """
            <p>We specialize in maintaining the factory finish of your vehicle while removing unsightly dents and dings.</p>
        """
    },
    "services.html": {
        "title": "Services",
        "heading": "Our Services",
        "content": """
            <ul class="list-disc pl-6 space-y-2">
                <li>Hail Damage Repair</li>
                <li>Door Ding Removal</li>
                <li>Minor Collision Creases</li>
            </ul>
        """
    },
    "gallery.html": {
        "title": "Gallery",
        "heading": "Before & After",
        "content": """
            <p class="mb-6">Check out our recent repairs below.</p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div class="bg-gray-700 h-48 rounded flex items-center justify-center text-gray-400 border border-dashed border-gray-500">
                    Image Placeholder 1 (assets/...)
                </div>
                <div class="bg-gray-700 h-48 rounded flex items-center justify-center text-gray-400 border border-dashed border-gray-500">
                    Image Placeholder 2 (assets/...)
                </div>
            </div>
        """
    },
    "contacts.html": {
        "title": "Contact",
        "heading": "Get a Quote",
        "content": """
            <p>Ready to restore your vehicle?</p>
            <p class="mt-4 text-xl font-bold text-cyan-400">Call us today.</p>
        """
    }
}

def rebuild():
    print("Rebuilding IndepenDent Website from scratch...\n")
    for filename, data in pages.items():
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_template.format(**data))
        print(f"✅ Created clean file: {filename}")
    print("\nRebuild complete. Run your server to test the navigation!")

if __name__ == "__main__":
    rebuild()