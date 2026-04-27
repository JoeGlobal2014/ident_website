import os

def generate_page(filename, title, heading, content):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | IndepenDent Technician</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        .text-heavy-shadow {{ text-shadow: 2px 2px 6px rgba(0,0,0,0.9); }}
    </style>
</head>
<body class="bg-gray-900 text-white font-sans antialiased flex flex-col min-h-screen">

    <header class="relative z-50 w-full py-6 px-8 flex flex-col md:flex-row justify-between items-center bg-black border-b border-gray-800 shadow-lg">
        <a href="index.html" class="flex-shrink-0 mb-4 md:mb-0">
            <img src="https://independent.checkmynewsite.com/wp-content/uploads/2026/02/Independent_new-logo2.png" alt="IndepenDent Logo" class="h-20">
        </a>
        <nav>
            <ul class="flex flex-wrap justify-center space-x-6 text-sm font-bold tracking-wider uppercase">
                <li><a href="index.html" class="hover:text-lime-400 transition drop-shadow-md">Home</a></li>
                <li><a href="about.html" class="hover:text-lime-400 transition drop-shadow-md">About</a></li>
                <li><a href="services.html" class="hover:text-lime-400 transition drop-shadow-md">Services</a></li>
                <li><a href="gallery.html" class="hover:text-lime-400 transition drop-shadow-md">Gallery</a></li>
                <li><a href="contacts.html" class="hover:text-lime-400 transition drop-shadow-md">Contact</a></li>
                <li><a href="https://independent.checkmynewsite.com/wp-content/uploads/2026/01/Independent-Technician-References-List.pdf" target="_blank" class="hover:text-lime-400 transition drop-shadow-md">Tech Reference</a></li>
            </ul>
        </nav>
    </header>

    <main class="flex-grow container mx-auto px-6 py-16 max-w-5xl">
        <h1 class="text-4xl md:text-5xl font-extrabold text-lime-400 uppercase tracking-tight mb-8 border-b border-gray-700 pb-4">
            {heading}
        </h1>
        <div class="text-gray-300 text-lg leading-relaxed space-y-6">
            {content}
        </div>
    </main>

    <footer class="bg-black border-t border-gray-800 py-8 mt-auto">
        <div class="container mx-auto px-6 text-center text-gray-500 text-sm">
            <p>&copy; 2026 IndepenDent Technician. All rights reserved. | <a href="contacts.html" class="hover:text-lime-400">Trade Accounts Only</a></p>
        </div>
    </footer>

</body>
</html>
"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✅ Rebuilt pure HTML for: {filename}")

if __name__ == "__main__":
    print("Rebuilding remaining pages to match the new architecture...\\n")
    
    # 1. About Page
    generate_page("about.html", "About", "About IndepenDent", 
        """
        <p>Over three decades of hands-on hail damage and paintless dent repair experience in active auto body shop environments.</p>
        <p>We specialize in maintaining the factory finish of your vehicle while removing unsightly dents and dings. Whether you are handling a local hail event or a large catastrophe, INDEPENDENT helps you scale without sacrificing quality or customer satisfaction.</p>
        """)
    
    # 2. Services Page
    generate_page("services.html", "Services", "Our Services", 
        """
        <ul class="list-disc pl-6 space-y-4">
            <li><strong class="text-white">Hail Damage Repair Support:</strong> Skilled technician ready to assist with high-volume hail repair work.</li>
            <li><strong class="text-white">Paintless Dent Repair (PDR):</strong> Efficient, cost-effective repairs that preserve factory finishes whenever possible.</li>
            <li><strong class="text-white">Overflow & Catastrophe Support:</strong> Scalable assistance when storms overwhelm your in-house capacity.</li>
            <li><strong class="text-white">Professional Shop Integration:</strong> Working under your standards, processes, and timelines—no disruption.</li>
        </ul>
        """)
    
    # 3. Gallery Page
    generate_page("gallery.html", "Gallery", "Before & After Gallery", 
        """
        <p class="mb-8">Check out our recent repairs below.</p>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div class="bg-gray-800 rounded-lg p-4 border border-gray-700 text-center text-gray-500">
                <p class="py-12">[ Insert Before Image ]</p>
            </div>
            <div class="bg-gray-800 rounded-lg p-4 border border-gray-700 text-center text-gray-500">
                <p class="py-12">[ Insert After Image ]</p>
            </div>
        </div>
        """)
    
    # 4. Contacts Page
    generate_page("contacts.html", "Contact", "Trade Inquiries Only — Let's Connect", 
        """
        <p class="text-2xl font-bold text-white mb-4">PDR Technician | Serving: Phoenix AZ</p>
        <div class="bg-gray-800 p-8 rounded-lg border border-gray-700 inline-block">
            <p class="mb-2"><strong class="text-lime-400">Tel:</strong> <a href="tel:1234567890" class="hover:text-white transition">123.456.7890</a></p>
            <p><strong class="text-lime-400">Email:</strong> <a href="mailto:Info@IndepenDentTech.com" class="hover:text-white transition">Info@IndepenDentTech.com</a></p>
        </div>
        """)

    print("\\nDone! Your entire site is now running on a clean, unified architecture.")