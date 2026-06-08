import os
import sys

output_path = r'C:\Users\moham\portfolio-projects\my-agency\index.html'

# Complete rebuilt website with all enhancements
html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mo Digital | Web Design That Converts</title>
    <meta name="description" content="Custom web design for modern businesses. Landing pages, business websites, and SaaS dashboards that convert visitors into customers.">
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Archivo:wght@300;400;500;600;700&family=Space+Grotesk:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        primary: '#0F0F11',
                        secondary: '#1A1A1E',
                        cta: '#3B82F6',
                        accent: '#8B5CF6',
                        background: '#050505',
                        surface: '#121214',
                        text: '#FAFAFA',
                        muted: '#A1A1AA',
                    },
                    fontFamily: {
                        heading: ['Archivo', 'sans-serif'],
                        body: ['Space Grotesk', 'sans-serif'],
                    }
                }
            }
        }
    </script>
    <style>
        html { scroll-behavior: smooth; scroll-padding-top: 100px; }
        .gradient-text {
            background: linear-gradient(135deg, #FAFAFA 0%, #3B82F6 50%, #8B5CF6 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .glass-card {
            background: rgba(18, 18, 20, 0.8);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.08);
        }
        .btn-primary {
            background: linear-gradient(135deg, #3B82F6 0%, #2563EB 100%);
            transition: all 0.3s ease;
            box-shadow: 0 4px 20px rgba(59, 130, 246, 0.3);
        }
        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 40px -10px rgba(59, 130, 246, 0.6);
        }
        .reveal {
            opacity: 0;
            transform: translateY(50px);
            transition: all 0.8s cubic-bezier(0.4, 0, 0.2, 1);
        }
        .reveal.active {
            opacity: 1;
            transform: translateY(0);
        }
        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-20px); }
        }
        .animate-float { animation: float 6s ease-in-out infinite; }
        #loader {
            position: fixed;
            inset: 0;
            z-index: 9999;
            background: #050505;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            transition: opacity 0.8s, visibility 0.8s;
        }
        #loader.fade-out { opacity: 0; visibility: hidden; pointer-events: none; }
        .back-to-top {
            position: fixed;
            bottom: 30px;
            right: 30px;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background: linear-gradient(135deg, #3B82F6 0%, #2563EB 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            opacity: 0;
            transform: translateY(100px);
            transition: all 0.3s ease;
            z-index: 1000;
        }
        .back-to-top.visible { opacity: 1; transform: translateY(0); }
    </style>
</head>
<body class="bg-background font-body text-text antialiased">

    <!-- Loading Experience -->
    <div id="loader">
        <div class="w-20 h-20 rounded-2xl bg-gradient-to-br from-cta to-accent flex items-center justify-center">
            <svg class="w-10 h-10 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21a4 4 0 01-4-4V5a2 2 0 012-2h4a2 2 0 012 2v12a4 4 0 01-4 4zm0 0h12a2 2 0 002-2v-4a2 2 0 00-2-2h-2.343M11 7.343l1.657-1.657a2 2 0 012.828 0l2.829 2.829a2 2 0 010 2.828l-8.486 8.485M7 17h.01"/>
            </svg>
        </div>
        <div class="mt-6 font-heading text-2xl font-bold gradient-text">Loading...</div>
    </div>

    <!-- Navigation -->
    <nav id="main-nav" class="fixed w-full z-50 bg-surface/80 backdrop-blur-xl border-b border-white/5 transition-all duration-300">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-16 md:h-20">
                <div class="flex items-center gap-2">
                    <div class="w-8 h-8 md:w-10 md:h-10 rounded-xl bg-gradient-to-br from-cta to-accent flex items-center justify-center">
                        <svg class="w-5 h-5 md:w-6 md:h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21a4 4 0 01-4-4V5a2 2 0 012-2h4a2 2 0 012 2v12a4 4 0 01-4 4zm0 0h12a2 2 0 002-2v-4a2 2 0 00-2-2h-2.343M11 7.343l1.657-1.657a2 2 0 012.828 0l2.829 2.829a2 2 0 010 2.828l-8.486 8.485M7 17h.01"/>
                        </svg>
                    </div>
                    <span class="font-heading text-lg md:text-xl font-bold tracking-tight">Mo<span class="text-cta">Digital</span></span>
                </div>
                <div class="hidden md:flex items-center gap-6 lg:gap-8">
                    <a href="#portfolio" class="text-muted hover:text-text transition-colors font-medium">Portfolio</a>
                    <a href="#services" class="text-muted hover:text-text transition-colors font-medium">Services</a>
                    <a href="#process" class="text-muted hover:text-text transition-colors font-medium">Process</a>
                    <a href="#contact" class="text-muted hover:text-text transition-colors font-medium">Contact</a>
                </div>
                <a href="#contact" class="hidden sm:inline-flex bg-cta text-white px-4 py-2 md:px-6 md:py-3 rounded-full font-medium hover:bg-cta/90 transition-all">Start Project</a>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="relative min-h-screen flex items-center pt-20 overflow-hidden">
        <div class="absolute top-20 right-0 w-3/4 md:w-1/2 h-1/2 bg-cta/20 rounded-full blur-3xl animate-float"></div>
        <div class="absolute bottom-0 left-0 w-1/2 md:w-1/3 h-1/3 bg-accent/10 rounded-full blur-3xl animate-float"></div>
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 md:py-20 relative z-10">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-10 lg:gap-16 items-center">
                <div class="space-y-6 md:space-y-8 reveal">
                    <div class="inline-flex items-center gap-2 px-3 py-1.5 md:px-4 md:py-2 rounded-full bg-cta/20 border border-cta/30">
                        <span class="w-2 h-2 rounded-full bg-cta animate-pulse"></span>
                        <span class="text-text font-medium text-xs md:text-sm">Available for New Projects</span>
                    </div>
                    <h1 class="font-heading text-3xl sm:text-4xl md:text-5xl lg:text-6xl xl:text-7xl font-bold leading-tight">
                        Web Design That <br>
                        <span class="gradient-text">Converts Visitors</span><br>
                        Into Customers
                    </h1>
                    <p class="text-base md:text-lg text-muted max-w-lg leading-relaxed">
                        Custom websites built with research-backed design systems.
                        No templates. No shortcuts. Just results-driven design that grows your business.
                    </p>
                    <div class="flex flex-col sm:flex-row gap-3 sm:gap-4">
                        <a href="#contact" class="btn-primary text-white px-6 py-3 md:px-8 md:py-4 rounded-full font-semibold inline-flex items-center justify-center gap-2 text-center">
                            Get Free Quote
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
                            </svg>
                        </a>
                        <a href="#portfolio" class="border-2 border-white/10 text-muted px-6 py-3 md:px-8 md:py-4 rounded-full font-medium hover:border-cta hover:text-text transition-all text-center">View Portfolio</a>
                    </div>
                </div>
                <div class="relative reveal">
                    <div class="absolute -inset-4 bg-gradient-to-r from-cta/20 to-accent/20 rounded-3xl blur-2xl"></div>
                    <div class="relative bg-white rounded-2xl md:rounded-3xl p-2 shadow-2xl">
                        <div class="bg-gradient-to-br from-gray-50 to-white rounded-xl overflow-hidden">
                            <div class="h-8 bg-gray-100 flex items-center px-4 gap-2">
                                <div class="w-3 h-3 rounded-full bg-red-400"></div>
                                <div class="w-3 h-3 rounded-full bg-yellow-400"></div>
                                <div class="w-3 h-3 rounded-full bg-green-400"></div>
                            </div>
                            <div class="p-6 space-y-4">
                                <div class="h-4 bg-gray-200 rounded w-3/4"></div>
                                <div class="h-32 bg-gradient-to-br from-cta/20 to-cta/5 rounded-xl flex items-center justify-center">
                                    <span class="text-cta font-heading font-bold text-2xl">Your New Website</span>
                                </div>
                                <div class="grid grid-cols-3 gap-2">
                                    <div class="h-16 bg-gray-100 rounded-lg"></div>
                                    <div class="h-16 bg-gray-100 rounded-lg"></div>
                                    <div class="h-16 bg-gray-100 rounded-lg"></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Services Section -->
    <section id="services" class="py-24 bg-surface relative">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-12 md:mb-16 reveal">
                <span class="text-cta font-medium text-xs uppercase tracking-wider">Services</span>
                <h2 class="font-heading text-3xl md:text-4xl lg:text-5xl font-bold mt-2 mb-4">What I Build</h2>
                <p class="text-base md:text-lg text-muted max-w-2xl mx-auto">From landing pages to full business websites, I create digital experiences that drive results.</p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 md:gap-8">
                <div class="glass-card rounded-2xl md:rounded-3xl p-6 md:p-8 reveal">
                    <div class="w-14 h-14 rounded-2xl bg-cta/10 flex items-center justify-center mb-6">
                        <svg class="w-7 h-7 text-cta" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 15l-2 5L9 9l11 4-5 2zm0 0l5 5M7.188 2.239l.777 2.897M5.136 7.965l-2.898-.777M13.95 4.05l-2.122 2.122m-5.657 5.656l-2.12 2.122"/>
                        </svg>
                    </div>
                    <h3 class="font-heading text-xl font-bold mb-3">Landing Pages</h3>
                    <p class="text-text/70 mb-4">High-converting single-page designs optimized for lead generation and sales.</p>
                    <ul class="space-y-2 text-sm text-text/60">
                        <li class="flex items-center gap-2"><svg class="w-4 h-4 text-cta" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>A/B tested layouts</li>
                        <li class="flex items-center gap-2"><svg class="w-4 h-4 text-cta" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>Conversion-focused CTAs</li>
                        <li class="flex items-center gap-2"><svg class="w-4 h-4 text-cta" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>Mobile-first design</li>
                    </ul>
                </div>
                <div class="glass-card rounded-2xl md:rounded-3xl p-6 md:p-8 reveal">
                    <div class="w-14 h-14 rounded-2xl bg-primary/10 flex items-center justify-center mb-6">
                        <svg class="w-7 h-7 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/>
                        </svg>
                    </div>
                    <h3 class="font-heading text-xl font-bold mb-3">Business Websites</h3>
                    <p class="text-text/70 mb-4">Multi-page professional websites that establish credibility and drive inquiries.</p>
                    <ul class="space-y-2 text-sm text-text/60">
                        <li class="flex items-center gap-2"><svg class="w-4 h-4 text-cta" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>3-5 page packages</li>
                        <li class="flex items-center gap-2"><svg class="w-4 h-4 text-cta" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>SEO optimization</li>
                        <li class="flex items-center gap-2"><svg class="w-4 h-4 text-cta" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>Contact forms & maps</li>
                    </ul>
                </div>
                <div class="glass-card rounded-2xl md:rounded-3xl p-6 md:p-8 reveal">
                    <div class="w-14 h-14 rounded-2xl bg-secondary/20 flex items-center justify-center mb-6">
                        <svg class="w-7 h-7 text-secondary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/>
                        </svg>
                    </div>
                    <h3 class="font-heading text-xl font-bold mb-3">SaaS Dashboards</h3>
                    <p class="text-text/70 mb-4">Clean, functional admin panels and analytics dashboards for tech companies.</p>
                    <ul class="space-y-2 text-sm text-text/60">
                        <li class="flex items-center gap-2"><svg class="w-4 h-4 text-cta" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>Data visualization</li>
                        <li class="flex items-center gap-2"><svg class="w-4 h-4 text-cta" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>User management UI</li>
                        <li class="flex items-center gap-2"><svg class="w-4 h-4 text-cta" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>Responsive tables</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- Portfolio Section -->
    <section id="portfolio" class="py-24 bg-background">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-12 md:mb-16 reveal">
                <span class="text-cta font-medium text-xs uppercase tracking-wider">Portfolio</span>
                <h2 class="font-heading text-3xl md:text-4xl lg:text-5xl font-bold mt-2 mb-4">Recent Projects</h2>
                <p class="text-base md:text-lg text-muted max-w-2xl mx-auto">A collection of personal projects I've designed and built.</p>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 md:gap-8">
'''

# Project cards
projects = [
    ('serenity-spa-screenshot.png', 'Serenity Spa', 'Luxury wellness landing page with booking functionality.', 'Landing Page', 'Beauty'),
    ('datadash-screenshot.png', 'DataDash Analytics', 'Modern analytics dashboard with data visualization.', 'Dashboard', 'SaaS'),
    ('bistro-locale-screenshot.png', 'Bistro Locale', 'Restaurant website with online reservation system.', 'Restaurant', 'Booking'),
    ('techstart-screenshot.png', 'TechStart', 'Modern SaaS landing page with features showcase.', 'SaaS', 'Tech'),
    ('artisan-screenshot.png', 'Artisan', 'Handcrafted goods e-commerce with product gallery.', 'E-commerce', 'Artisan'),
    ('horizon-screenshot.png', 'Horizon', 'Travel agency website with destination cards.', 'Travel', 'Booking'),
]

for img, title, desc, tag1, tag2 in projects:
    html += f'''
                <div class="glass-card rounded-2xl md:rounded-3xl overflow-hidden reveal">
                    <div class="aspect-[4/3] relative overflow-hidden">
                        <img src="{img}" alt="{title}" class="w-full h-full object-cover">
                    </div>
                    <div class="p-4 md:p-6">
                        <div class="flex flex-wrap gap-2 mb-2">
                            <span class="px-2 py-1 rounded-full bg-cta/10 text-cta text-xs font-medium">{tag1}</span>
                            <span class="px-2 py-1 rounded-full bg-white/5 text-text/60 text-xs font-medium">{tag2}</span>
                        </div>
                        <h3 class="font-heading text-lg font-bold mb-1">{title}</h3>
                        <p class="text-text/70 text-sm">{desc}</p>
                    </div>
                </div>
'''

html += '''
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="py-24 bg-surface">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-12 reveal">
                <span class="text-cta font-medium text-xs uppercase tracking-wider">Let's Work Together</span>
                <h2 class="font-heading text-3xl md:text-4xl lg:text-5xl font-bold mt-2 mb-4">Ready to Start Your Project?</h2>
                <p class="text-base md:text-lg text-muted">Tell me about your project and I'll get back to you within 24 hours.</p>
            </div>
            <div class="glass-card rounded-2xl md:rounded-3xl p-6 md:p-8 lg:p-12">
                <form id="contactForm" class="space-y-6">
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div>
                            <label class="block text-sm font-medium mb-2">Name</label>
                            <input type="text" placeholder="Your name" class="w-full px-4 py-3 rounded-xl border border-white/10 bg-surface/50 focus:border-cta focus:outline-none">
                        </div>
                        <div>
                            <label class="block text-sm font-medium mb-2">Email</label>
                            <input type="email" placeholder="your@email.com" class="w-full px-4 py-3 rounded-xl border border-white/10 bg-surface/50 focus:border-cta focus:outline-none">
                        </div>
                    </div>
                    <div>
                        <label class="block text-sm font-medium mb-2">What do you need?</label>
                        <textarea rows="4" placeholder="Describe your business, goals, timeline, and budget..." class="w-full px-4 py-3 rounded-xl border border-white/10 bg-surface/50 focus:border-cta focus:outline-none"></textarea>
                    </div>
                    <button type="submit" class="w-full btn-primary text-white py-4 rounded-xl font-semibold">
                        Send Message
                    </button>
                </form>
                <div class="mt-8 pt-8 border-t border-white/10 text-center">
                    <p class="text-text/60 mb-2">Prefer email?</p>
                    <a href="mailto:Modigital98@outlook.com" class="text-cta font-semibold hover:underline">Modigital98@outlook.com</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-background border-t border-white/5 py-8 md:py-12">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex flex-col md:flex-row justify-between items-center gap-4">
                <div class="flex items-center gap-2">
                    <div class="w-8 h-8 rounded-lg bg-cta flex items-center justify-center">
                        <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21a4 4 0 01-4-4V5a2 2 0 012-2h4a2 2 0 012 2v12a4 4 0 01-4 4zm0 0h12a2 2 0 002-2v-4a2 2 0 00-2-2h-2.343M11 7.343l1.657-1.657a2 2 0 012.828 0l2.829 2.829a2 2 0 010 2.828l-8.486 8.485M7 17h.01"/>
                        </svg>
                    </div>
                    <span class="font-heading font-bold">Mo<span class="text-cta">Digital</span></span>
                </div>
                <div class="flex items-center gap-6 text-sm text-white/60">
                    <a href="#portfolio" class="hover:text-white transition-colors">Portfolio</a>
                    <a href="#services" class="hover:text-white transition-colors">Services</a>
                    <a href="#contact" class="hover:text-white transition-colors">Contact</a>
                </div>
                <p class="text-sm text-white/40">© 2024 MoDigital. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <script>
        // Mobile menu toggle
        const mobileMenuBtn = document.getElementById('mobile-menu-btn');
        const mobileMenu = document.getElementById('mobile-menu');
        const menuIcon = document.getElementById('menu-icon');
        const closeIcon = document.getElementById('close-icon');

        if (mobileMenuBtn) {
            mobileMenuBtn.addEventListener('click', () => {
                mobileMenu.classList.toggle('hidden');
                menuIcon.classList.toggle('hidden');
                closeIcon.classList.toggle('hidden');
            });
        }

        // Nav scroll effect
        const mainNav = document.getElementById('main-nav');
        window.addEventListener('scroll', () => {
            if (mainNav) {
                if (window.scrollY > 50) {
                    mainNav.classList.add('nav-scrolled');
                } else {
                    mainNav.classList.remove('nav-scrolled');
                }
            }
        });

        // Scroll reveal animation
        const revealElements = document.querySelectorAll('.reveal');
        const revealOnScroll = () => {
            revealElements.forEach(element => {
                const elementTop = element.getBoundingClientRect().top;
                const elementVisible = 150;
                if (elementTop < window.innerHeight - elementVisible) {
                    element.classList.add('active');
                }
            });
        };
        window.addEventListener('scroll', revealOnScroll);
        revealOnScroll();

        // Back to top button
        const backToTopBtn = document.createElement('div');
        backToTopBtn.className = 'back-to-top';
        backToTopBtn.innerHTML = `
            <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18"/>
            </svg>
        `;
        backToTopBtn.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
        document.body.appendChild(backToTopBtn);

        window.addEventListener('scroll', () => {
            if (window.scrollY > 500) {
                backToTopBtn.classList.add('visible');
            } else {
                backToTopBtn.classList.remove('visible');
            }
        });

        // Loading screen
        window.addEventListener('load', () => {
            setTimeout(() => {
                const loader = document.getElementById('loader');
                if (loader) {
                    loader.classList.add('fade-out');
                    setTimeout(() => loader.style.display = 'none', 800);
                }
            }, 2000);
        });

        // Smooth scroll for anchor links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    const navHeight = document.querySelector('nav').offsetHeight;
                    const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - navHeight;
                    window.scrollTo({ top: targetPosition, behavior: 'smooth' });
                }
            });
        });

        // Form submission
        document.getElementById('contactForm')?.addEventListener('submit', (e) => {
            e.preventDefault();
            alert('Message sent! (This is a demo)');
        });
    </script>

</body>
</html>
'''

# Write the complete file
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Website rebuilt successfully!")
print(f"File size: {len(html)} characters")
print(f"Location: {output_path}")
