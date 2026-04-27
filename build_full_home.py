import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home | IndepenDent Technician</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        .text-heavy-shadow { text-shadow: 2px 2px 6px rgba(0,0,0,0.9); }
        .glow-text { text-shadow: 0 0 12px rgba(163, 230, 53, 0.6); }
        /* Smooth scrolling for the whole page */
        html { scroll-behavior: smooth; }
    </style>
</head>
<body class="bg-gray-900 text-gray-800 font-sans antialiased overflow-x-hidden">

    <div class="relative w-full h-screen flex flex-col">
        <video autoplay loop muted playsinline class="absolute top-0 left-0 w-full h-full object-cover z-0">
            <source src="assets/asset_cd0f89fe.mp4" type="video/mp4">
        </video>
        
        <div class="absolute top-0 left-0 w-full h-full bg-black/60 z-0"></div>

        <header class="relative z-50 w-full py-6 px-8 flex flex-col md:flex-row justify-between items-center border-b border-gray-500/30">
            <a href="index.html" class="flex-shrink-0 mb-4 md:mb-0">
                <img src="https://independent.checkmynewsite.com/wp-content/uploads/2026/02/Independent_new-logo2.png" alt="IndepenDent Logo" class="h-16 md:h-20">
            </a>
            <nav>
                <ul class="flex flex-wrap justify-center space-x-6 text-sm font-bold tracking-wider uppercase">
                    <li><a href="index.html" class="text-lime-400 hover:text-white transition drop-shadow-md">Home</a></li>
                    <li><a href="about.html" class="text-white hover:text-lime-400 transition drop-shadow-md">About</a></li>
                    <li><a href="services.html" class="text-white hover:text-lime-400 transition drop-shadow-md">Services</a></li>
                    <li><a href="gallery.html" class="text-white hover:text-lime-400 transition drop-shadow-md">Gallery</a></li>
                    <li><a href="contacts.html" class="text-white hover:text-lime-400 transition drop-shadow-md">Contact</a></li>
                    <li><a href="https://independent.checkmynewsite.com/wp-content/uploads/2026/01/Independent-Technician-References-List.pdf" target="_blank" class="text-white hover:text-lime-400 transition drop-shadow-md">Tech Reference</a></li>
                </ul>
            </nav>
        </header>

        <main class="relative z-10 flex-grow flex flex-col items-center justify-center text-center px-4">
            <h3 class="text-lime-400 text-xl md:text-2xl font-bold italic mb-4 drop-shadow-lg">
                Trade-Only PDR Services. Reliable. Precise. Fast Turnaround.
            </h3>
            <h1 class="text-white text-4xl md:text-6xl lg:text-7xl font-extrabold uppercase leading-tight max-w-6xl text-heavy-shadow mb-10 tracking-tight">
                Paintless Dent Repair for Body Shops, Dealers & Wholesale Accounts.
            </h1>
            <div class="flex flex-col items-center space-y-6">
                <a href="contacts.html" class="bg-[#f58220] hover:bg-orange-500 text-white font-extrabold py-3 px-10 rounded-lg text-xl transition transform hover:scale-105 shadow-lg border border-orange-400">
                    Call Now!
                </a>
                <h2 class="text-lime-400 text-2xl md:text-4xl font-bold italic glow-text mt-4">
                    Licensed and Insured
                </h2>
            </div>
        </main>
    </div>

    <div class="relative z-20 bg-white shadow-[0_-20px_50px_rgba(0,0,0,0.5)]">

        <section class="py-16 container mx-auto px-6">
            <div class="flex justify-center mb-12">
                <img src="https://independent.checkmynewsite.com/wp-content/uploads/2025/07/arc_certified1.png" alt="ARC Certified" class="h-40 mx-4 drop-shadow-lg">
                <img src="https://independent.checkmynewsite.com/wp-content/uploads/2025/07/arc_certified2.png" alt="ARC Master Tech" class="h-40 mx-4 drop-shadow-lg">
                <img src="https://independent.checkmynewsite.com/wp-content/uploads/2025/07/napdrt1.png" alt="NAPDRT Member" class="h-40 mx-4 drop-shadow-lg">
                <img src="https://independent.checkmynewsite.com/wp-content/uploads/2025/07/30years.png" alt="30 Years" class="h-40 mx-4 drop-shadow-lg">
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-5 gap-6 text-sm text-gray-700">
                <div class="p-6 border border-gray-200 rounded-lg bg-blue-50/50 shadow-sm">
                    <h4 class="font-bold text-blue-900 text-lg mb-2 italic">30+ Years of Industry Experience</h4>
                    <p>Over three decades of hands-on hail damage and paintless dent repair experience in active auto body shop environments.</p>
                </div>
                <div class="p-6 border border-gray-200 rounded-lg bg-orange-50/50 shadow-sm">
                    <h4 class="font-bold text-orange-800 text-lg mb-2 italic">ARC CERTIFIED</h4>
                    <p>ARC certification demonstrates advanced technical skill and professional competency in paintless dent repair.</p>
                </div>
                <div class="p-6 border border-gray-200 rounded-lg bg-green-50/50 shadow-sm">
                    <h4 class="font-bold text-green-800 text-lg mb-2 italic">I-CAR CERTIFIED</h4>
                    <p>I-Car certification ensures all repairs meet current industry standards, safety practices, and proper repair procedures.</p>
                </div>
                <div class="p-6 border border-gray-200 rounded-lg bg-purple-50/50 shadow-sm">
                    <h4 class="font-bold text-purple-900 text-lg mb-2 italic">Mobile Tech Experienced</h4>
                    <p>All estimates are written using Mobile Tech RX and follow shop-approved, DRP-compliant estimating procedures.</p>
                </div>
                <div class="p-6 border border-gray-200 rounded-lg bg-gray-50 shadow-sm">
                    <h4 class="font-bold text-gray-900 text-lg mb-2 italic">Fully Insured</h4>
                    <p>$1,000,000 Garage Keepers Limited Liability coverage, providing protection and peace of mind for our body shop partners.</p>
                </div>
            </div>
        </section>

        <section class="py-16 bg-white container mx-auto px-6">
            <div class="flex flex-col md:flex-row items-center gap-12">
                <div class="md:w-1/2">
                    <h3 class="text-blue-600 font-bold italic text-xl mb-2">Who We Work With</h3>
                    <h2 class="text-4xl font-black uppercase text-gray-900 mb-8 leading-tight italic">We Partner With The Professionals Who Keep Vehicles Moving</h2>
                    <ul class="space-y-4 text-lg text-gray-700 mb-8 font-medium">
                        <li class="flex items-center"><span class="text-lime-500 mr-3 text-2xl">✓</span> Collision Shops & Body Shops</li>
                        <li class="flex items-center"><span class="text-lime-500 mr-3 text-2xl">✓</span> Dealerships — New & Pre-Owned Inventory</li>
                        <li class="flex items-center"><span class="text-lime-500 mr-3 text-2xl">✓</span> Fleet Management Companies</li>
                        <li class="flex items-center"><span class="text-lime-500 mr-3 text-2xl">✓</span> Wholesale Buyers & Auto Auctions</li>
                        <li class="flex items-center"><span class="text-lime-500 mr-3 text-2xl">✓</span> Independent PDR Technicians — Subcontracting Available</li>
                    </ul>
                    <p class="text-gray-600 mb-8">If you're part of the general public, we appreciate your interest, but our services are exclusively for trade partners.</p>
                    <a href="contacts.html" class="inline-block bg-[#0071ba] hover:bg-blue-700 text-white font-bold py-3 px-8 rounded-lg transition shadow-md">Call Now!</a>
                </div>
                <div class="md:w-1/2">
                    <img src="https://independent.checkmynewsite.com/wp-content/uploads/2026/01/pdr_repair1.jpg" alt="PDR Repair" class="rounded-2xl shadow-xl w-full object-cover h-[500px]">
                </div>
            </div>
        </section>

        <section class="py-20 bg-gray-900 text-white relative border-t-4 border-blue-600">
            <div class="container mx-auto px-6 relative z-10">
                <h2 class="text-4xl font-black uppercase italic mb-12 text-center text-white drop-shadow-md">Estimating & DRP Compatibility</h2>
                
                <div class="max-w-4xl mx-auto space-y-8">
                    <div>
                        <h3 class="text-2xl font-bold text-blue-400 italic mb-2">Do you write estimates for DRP body shops?</h3>
                        <p class="text-gray-300">Yes. INDEPENDENT is experienced in estimating hail damage using Mobile Tech RX and can support DRP body shops by working within established estimating guidelines and shop processes.</p>
                    </div>
                    <hr class="border-gray-700">
                    <div>
                        <h3 class="text-2xl font-bold text-blue-400 italic mb-2">How does estimating work?</h3>
                        <ul class="list-disc pl-5 text-gray-300 space-y-1">
                            <li>Estimates are written using Mobile Tech RX</li>
                            <li>All estimates follow shop-approved and DRP-compliant procedures</li>
                            <li>We work in coordination with shop management and insurance requirements</li>
                            <li>Final approval and customer communication remain with the shop</li>
                        </ul>
                    </div>
                    <hr class="border-gray-700">
                    <div>
                        <h3 class="text-2xl font-bold text-blue-400 italic mb-2">Will this interfere with our DRP relationship?</h3>
                        <p class="text-gray-300">No. Our role is supportive and compliant, not disruptive. We work strictly within your shop's DRP structure and never operate independently of your processes.</p>
                    </div>
                </div>
            </div>
        </section>

        <section class="py-20 bg-gray-50 container mx-auto px-6">
            <div class="flex flex-col md:flex-row items-center gap-12">
                <div class="md:w-1/2">
                    <h3 class="text-blue-600 font-bold italic text-xl mb-2">Reliable Auto Hail Repair Support for Body Shops</h3>
                    <h2 class="text-4xl font-black uppercase text-gray-900 mb-6 leading-tight italic">When Hail Hits, Your Shop Needs Support You Can Trust</h2>
                    <p class="text-gray-700 mb-6">Hail storms create instant volume—and instant pressure. Without the right support, jobs stack up, customers wait, and revenue slows.</p>
                    <p class="text-gray-700 font-bold mb-6">INDEPENDENT provides experienced hail repair solutions that integrate seamlessly with your shop, so you can keep operations running smoothly during peak demand.</p>
                    <ul class="space-y-4 text-gray-700">
                        <li><span class="text-lime-500 font-bold text-xl mr-2">✓</span> <strong>Hail Damage Repair Support</strong><br>Skilled technician ready to assist with high-volume hail repair work.</li>
                        <li><span class="text-lime-500 font-bold text-xl mr-2">✓</span> <strong>Professional Shop Integration</strong><br>Working under your standards, processes, and timelines—no disruption.</li>
                    </ul>
                </div>
                <div class="md:w-1/2">
                    <img src="https://independent.checkmynewsite.com/wp-content/uploads/2025/06/pdr_repair-1.jpg" alt="Dent Repair Technician" class="rounded-2xl shadow-xl w-full">
                </div>
            </div>
        </section>

        <section class="py-16 bg-white container mx-auto px-6 text-center">
            <h2 class="text-4xl font-black uppercase text-gray-900 mb-8 italic">Why Body Shops Choose INDEPENDENT</h2>
            <div class="max-w-2xl mx-auto text-left space-y-3 text-lg text-gray-700 mb-12">
                <p><span class="text-lime-500 font-bold mr-2">✓</span> Experienced hail repair technician</p>
                <p><span class="text-lime-500 font-bold mr-2">✓</span> Fast response during storm events</p>
                <p><span class="text-lime-500 font-bold mr-2">✓</span> Clean, professional workmanship</p>
                <p><span class="text-lime-500 font-bold mr-2">✓</span> Reliable communication and scheduling</p>
                <p><span class="text-lime-500 font-bold mr-2">✓</span> Focused on protecting your reputation</p>
            </div>
            
            <h3 class="text-3xl font-black uppercase text-gray-900 italic mb-8">INDEPENDENT UNDERSTANDS THAT YOUR NAME IS ON EVERY VEHICLE. IT'S TREATED THAT WAY.</h3>
            
            <a href="contacts.html" class="inline-block bg-[#0071ba] hover:bg-blue-700 text-white font-bold py-4 px-10 rounded-lg transition shadow-md text-xl">Contact INDEPENDENT Today</a>
        </section>

        <footer class="bg-black py-8 mt-auto">
            <div class="container mx-auto px-6 text-center text-gray-400 text-sm">
                <p class="mb-2">PDR Technician | Serving: Phoenix AZ | Trade Accounts Only</p>
                <p>&copy; 2026 IndepenDent Technician. All rights reserved.</p>
            </div>
        </footer>

    </div>

</body>
</html>
"""

if __name__ == "__main__":
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("✅ The COMPLETE homepage has been built, including all scrolling sections!")