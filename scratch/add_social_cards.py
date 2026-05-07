import os

directory = r'c:\Akemi'
files = {
    'index.html': {
        'title': 'Akemi Hair Glow – Hair Growth Spray for Thicker-Looking, Stronger Hair',
        'desc': 'Akemi Hair Glow is a leave-in topical scalp spray for men with visible thinning. Rated 4.8 by 3,758 customers.',
        'url': 'https://www.akemihairglowofficial.com/'
    },
    'about.html': {
        'title': 'About Us | Akemi Hair Glow Official',
        'desc': 'Learn more about AkemiHairGlowOfficial.com, our mission to simplify hair care for men, and our commitment to clarity.',
        'url': 'https://www.akemihairglowofficial.com/about.html'
    },
    'privacy-policy.html': {
        'title': 'Privacy Policy | Akemi Hair Glow Official',
        'desc': 'Privacy Policy for AkemiHairGlowOfficial.com. Learn how we collect, use, and protect your information.',
        'url': 'https://www.akemihairglowofficial.com/privacy-policy.html'
    },
    'shipping-returns.html': {
        'title': 'Shipping & Returns | Akemi Hair Glow Official',
        'desc': 'Review the return and refund guidelines for Akemi Hair Glow. Learn about our 30-day return policy.',
        'url': 'https://www.akemihairglowofficial.com/shipping-returns.html'
    },
    'terms-of-use.html': {
        'title': 'Terms of Use | Akemi Hair Glow Official',
        'desc': 'Terms of Use for AkemiHairGlowOfficial.com. Learn about the rules and guidelines for using our website.',
        'url': 'https://www.akemihairglowofficial.com/terms-of-use.html'
    },
    'disclosure.html': {
        'title': 'Advertising Disclosure | Akemi Hair Glow Official',
        'desc': 'Advertising Disclosure for AkemiHairGlowOfficial.com. Learn about our affiliate relations and commercial positioning.',
        'url': 'https://www.akemihairglowofficial.com/disclosure.html'
    },
    'contact.html': {
        'title': 'Contact Us | Akemi Hair Glow Official',
        'desc': 'Contact Akemi Hair Glow for any questions regarding our website, product information, or your experience.',
        'url': 'https://www.akemihairglowofficial.com/contact.html'
    },
    'write-for-us.html': {
        'title': 'Write For Us | Akemi Hair Glow Official',
        'desc': 'Contribute to Akemi Hair Glow. We invite knowledgeable writers to share practical insights on hair care.',
        'url': 'https://www.akemihairglowofficial.com/write-for-us.html'
    }
}

og_image = "https://www.akemihairglowofficial.com/public/hero-main.webp"

for filename, data in files.items():
    path = os.path.join(directory, filename)
    if not os.path.exists(path):
        continue
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'og:title' in content:
        print(f"Skipping {filename} (already has social cards)")
        continue
    
    # Generate the tags
    tags = f"""  <link rel="canonical" href="{data['url']}" />
  
  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{data['url']}" />
  <meta property="og:title" content="{data['title']}" />
  <meta property="og:description" content="{data['desc']}" />
  <meta property="og:image" content="{og_image}" />

  <!-- Twitter -->
  <meta property="twitter:card" content="summary_large_image" />
  <meta property="twitter:url" content="{data['url']}" />
  <meta property="twitter:title" content="{data['title']}" />
  <meta property="twitter:description" content="{data['desc']}" />
  <meta property="twitter:image" content="{og_image}" />
"""
    
    # Insert before </head>
    if '</head>' in content:
        new_content = content.replace('</head>', tags + '</head>')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        print(f"</head> not found in {filename}")

print("Done")
