import os

output_path = r'C:\Users\moham\portfolio-projects\my-agency\index.html'

# Read the original content that we know was there (from earlier reading)
# We have the original index.html content from the very first read_file call
# But since that was corrupted, we'll build a complete new version

html_content = '''<!DOCTYPE html>
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
'''

# Continue building the rest of the HTML body
print("Part 1 generated")

# Write part 1 to file first
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Part 1 written to file")
