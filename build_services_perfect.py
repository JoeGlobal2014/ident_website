import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Services | IndepenDent Technician</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Archivo+Black&display=swap');
        .font-heavy { font-family: 'Archivo Black', sans-serif; }
        .text-heavy-shadow { text-shadow: 3px 3px 10px rgba(0,0,0,0.9); }
        .hero-banner {
            background: linear-gradient(rgba(0,0,0,0.65), rgba(0,0,0,0.65)), url('assets/asset_ba339ac1.jpg');
            background-size: cover; background-position: center;
        }
    </style>
</head>
<body class="bg-white text-gray-900 font-sans antialiased">

    <div class="relative w-full bg-[#0a0f16] border-b border-blue-900/30">
        <video autoplay loop muted playsinline class="absolute top-0 left-0 w-full h-full object-cover z-0 opacity-40">
            <source src="assets/asset_cd0f89fe.mp4" type="video/mp4">
        </video>
        <header class="relative z-50 w-full py-6 px-8 flex justify-between items-center max-w-7xl mx-auto">
            <a href="index.html"><img src="https://independent.checkmynewsite.com/wp-content/uploads/2026/02/Independent_new-logo2.png" alt="Logo" class="h-20"></a>
            <nav>
                <ul class="flex space-x-6 text-sm font-bold tracking-wider uppercase text-white">
                    <li><a href="index.html" class="hover:text-lime-400">Home</a></li>
                    <li><a href="about.html" class="hover:text-lime-400">About</a></li>
                    <li><a href="services.html" class="text-lime-400">Services</a></li>
                    <li><a href="gallery.html" class="hover:text-lime-400">Gallery</a></li>
                    <li><a href="contacts.html" class="hover:text-lime-400">Contact</a></li>
                </ul>
            </nav>
        </header>
    </div>

    <div class="hero-banner h-[380px] relative flex items-center justify-center">
        <h1 class="text-white text-7xl md:text-8xl font-heavy italic uppercase tracking-tighter text-heavy-shadow z-10">SERVICES</h1>
        <div class="absolute bottom-0 left-0 w-full leading-none z-20">
            <svg viewBox="0 0 1440 120" fill="none" class="w-full h-auto"><path d="M0 120L1440 120L1440 0C1440 0 1140 120 720 120C300 120 0 0 0 0L0 120Z" fill="white"/></svg>
        </div>
    </div>

    <section class="bg-white py-24">
        <div class="container mx-auto px-6 max-w-7xl flex flex-col md:flex-row items-center gap-16">
            
            <div class="md:w-5/12">
                <img src="assets/asset_dfeb863f.jpg" class="rounded-3xl shadow-2xl border-8 border-white" alt="PDR Repair on Red Car">
            </div>

            <div class="md:w-7/12">
                <h3 class="text-[#0071ba] font-bold italic text-2xl mb-4">I Work With:</h3>
                <div class="space-y-10">
                    <div>
                        <h2 class="text-6xl font-heavy uppercase italic text-gray-900 leading-[0.9]">BODY SHOPS:</h2>
                        <p class="text-xl text-gray-600 font-bold italic mt-2">Expand your capacity and keep work flowing without sacrificing quality.</p>
                    </div>
                    <div>
                        <h2 class="text-6xl font-heavy uppercase italic text-gray-900 leading-[0.9]">DEALERSHIPS:</h2>
                        <p class="text-xl text-gray-600 font-bold italic mt-2">Get your fleet back to pre-loss condition quickly and easily, and profitably.</p>
                    </div>
                    <div>
                        <h2 class="text-6xl font-heavy uppercase italic text-gray-900 leading-[0.9]">DENT REPAIR SHOPS:</h2>
                        <p class="text-xl text-gray-600 font-bold italic mt-2">A hail storm can be a disaster or it can be your winning lottery ticket!</p>
                    </div>
                </div>
                
                <div class="mt-12">
                    <h4 class="font-bold text-gray-900 text-lg mb-4">Why Partner With Me?</h4>
                    <ul class="space-y-2 text-gray-700">
                        <li class="flex items-center"><span class="text-lime-500 font-bold mr-2">✓</span> 30+ Years of PDR Experience</li>
                        <li class="flex items-center"><span class="text-lime-500 font-bold mr-2">✓</span> Certified, Insured, and Professional</li>
                        <li class="flex items-center"><span class="text-lime-500 font-bold mr-2">✓</span> High-Quality, No-Drama Repairs</li>
                        <li class="flex items-center"><span class="text-lime-500 font-bold mr-2">✓</span> Sublet Work — You Keep a Percentage</li>
                        <li class="flex items-center"><span class="text-lime-500 font-bold mr-2">✓</span> Nationwide, Storm-Driven Availability</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <footer class="bg-[#0a0f16] py-20 border-t border-gray-800">
        <div class="container mx-auto px-6 max-w-7xl flex flex-col md:flex-row justify-between items-end">
            <div class="text-gray-400">
                <p class="text-white font-heavy italic text-2xl mb-4">PDR Technician | Serving: Phoenix AZ</p>
                <p class="text-sm">Copyright © 2026, IndepenDent Technician – All Rights Reserved.</p>
            </div>
            <img src="https://independent.checkmynewsite.com/wp-content/uploads/2026/02/Independent_new-logo2.png" class="h-28 opacity-60">
        </div>
    </footer>

</body>
</html>
"""

with open('services.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
print("✅ services.html rebuilt using local asset_dfeb863f.jpg!")