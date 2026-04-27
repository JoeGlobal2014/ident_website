import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home | IndepenDent Technician</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        /* Custom text shadows to match the live site's typography */
        .text-heavy-shadow { text-shadow: 2px 2px 6px rgba(0,0,0,0.9); }
        .glow-text { text-shadow: 0 0 12px rgba(163, 230, 53, 0.6); }
    </style>
</head>
<body class="bg-gray-900 text-white font-sans antialiased overflow-x-hidden">

    <video autoplay loop muted playsinline class="fixed top-0 left-0 w-full h-full object-cover z-0">
        <source src="assets/asset_cd0f89fe.mp4" type="video/mp4">
    </video>
    
    <div class="fixed top-0 left-0 w-full h-full bg-black/60 z-0"></div>

    <header class="relative z-50 w-full py-6 px-8 flex flex-col md:flex-row justify-between items-center">
        <a href="index.html" class="flex-shrink-0 mb-4 md:mb-0">
            <img src="https://independent.checkmynewsite.com/wp-content/uploads/2026/02/Independent_new-logo2.png" alt="IndepenDent Logo" class="h-20">
        </a>
        <nav>
            <ul class="flex flex-wrap justify-center space-x-6 text-sm font-bold tracking-wider uppercase">
                <li><a href="index.html" class="text-lime-400 hover:text-white transition drop-shadow-md">Home</a></li>
                <li><a href="about.html" class="hover:text-lime-400 transition drop-shadow-md">About</a></li>
                <li><a href="services.html" class="hover:text-lime-400 transition drop-shadow-md">Services</a></li>
                <li><a href="gallery.html" class="hover:text-lime-400 transition drop-shadow-md">Gallery</a></li>
                <li><a href="contacts.html" class="hover:text-lime-400 transition drop-shadow-md">Contact</a></li>
                <li><a href="https://independent.checkmynewsite.com/wp-content/uploads/2026/01/Independent-Technician-References-List.pdf" target="_blank" class="hover:text-lime-400 transition drop-shadow-md">Tech Reference</a></li>
            </ul>
        </nav>
    </header>

    <main class="relative z-10 flex flex-col items-center justify-center min-h-[75vh] text-center px-4">
        
        <h3 class="text-lime-400 text-xl md:text-2xl font-bold italic mb-4 drop-shadow-lg">
            Trade-Only PDR Services. Reliable. Precise. Fast Turnaround.
        </h3>
        
        <h1 class="text-white text-5xl md:text-7xl font-extrabold uppercase leading-tight max-w-6xl text-heavy-shadow mb-10 tracking-tight">
            Paintless Dent Repair for Body Shops, Dealers & Wholesale Accounts.
        </h1>
        
        <div class="flex flex-col items-center space-y-6">
            <a href="contacts.html" class="bg-[#f58220] hover:bg-orange-500 text-white font-extrabold py-3 px-10 rounded-lg text-xl transition transform hover:scale-105 shadow-lg border border-orange-400">
                Call Now!
            </a>
            <h2 class="text-lime-400 text-3xl md:text-4xl font-bold italic glow-text mt-4">
                Licensed and Insured
            </h2>
        </div>

    </main>

</body>
</html>
"""

if __name__ == "__main__":
    # Run the generator
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("✅ index.html has been completely rebuilt.")