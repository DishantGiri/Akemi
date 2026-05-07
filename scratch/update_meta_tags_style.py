import os

directory = r'c:\Akemi'
files = {
    'index.html': {
        'title': 'Akemi Hair Glow | 67% OFF | Hair Growth Spray for Thicker-Looking Hair',
        'meta_title': 'Akemi Hair Glow | Hair Growth Spray for Thicker-Looking, Stronger Hair',
        'desc': 'Akemi Hair Glow | Premium leave-in topical scalp spray for men with visible thinning. Rated 4.8 by 3,758 customers. 30-day money-back guarantee.',
        'url': 'https://www.akemihairglowofficial.com/'
    },
    'about.html': {
        'title': 'About Us | Akemi Hair Glow Official',
        'meta_title': 'About Us | Akemi Hair Glow Official',
        'desc': 'Learn more about AkemiHairGlowOfficial.com, our mission to simplify hair care for men, and our commitment to clarity.',
        'url': 'https://www.akemihairglowofficial.com/about.html'
    },
    'privacy-policy.html': {
        'title': 'Privacy Policy | Akemi Hair Glow Official',
        'meta_title': 'Privacy Policy | Akemi Hair Glow Official',
        'desc': 'Privacy Policy for AkemiHairGlowOfficial.com. Learn how we collect, use, and protect your information.',
        'url': 'https://www.akemihairglowofficial.com/privacy-policy.html'
    },
    'shipping-returns.html': {
        'title': 'Shipping & Returns | Akemi Hair Glow Official',
        'meta_title': 'Shipping & Returns | Akemi Hair Glow Official',
        'desc': 'Review the return and refund guidelines for Akemi Hair Glow. Learn about our 30-day return policy.',
        'url': 'https://www.akemihairglowofficial.com/shipping-returns.html'
    },
    'terms-of-use.html': {
        'title': 'Terms of Use | Akemi Hair Glow Official',
        'meta_title': 'Terms of Use | Akemi Hair Glow Official',
        'desc': 'Terms of Use for AkemiHairGlowOfficial.com. Learn about the rules and guidelines for using our website.',
        'url': 'https://www.akemihairglowofficial.com/terms-of-use.html'
    },
    'disclosure.html': {
        'title': 'Advertising Disclosure | Akemi Hair Glow Official',
        'meta_title': 'Advertising Disclosure | Akemi Hair Glow Official',
        'desc': 'Advertising Disclosure for AkemiHairGlowOfficial.com. Learn about our affiliate relations and commercial positioning.',
        'url': 'https://www.akemihairglowofficial.com/disclosure.html'
    },
    'contact.html': {
        'title': 'Contact Us | Akemi Hair Glow Official',
        'meta_title': 'Contact Us | Akemi Hair Glow Official',
        'desc': 'Contact Akemi Hair Glow for any questions regarding our website, product information, or your experience.',
        'url': 'https://www.akemihairglowofficial.com/contact.html'
    },
    'write-for-us.html': {
        'title': 'Write For Us | Akemi Hair Glow Official',
        'meta_title': 'Write For Us | Akemi Hair Glow Official',
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
    
    # We want to replace everything from <title> down to the first <link rel="stylesheet">
    # Actually, it's safer to just construct the whole head section we want to replace or update.
    
    # Construct the new block
    head_block = f"""    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="title" content="{data['meta_title']}">
    <meta name="description" content="{data['desc']}">
    <title>{data['title']}</title>

    <!-- Open Graph Meta Tags -->
    <meta property="og:title" content="{data['meta_title']}">
    <meta property="og:description" content="{data['desc']}">
    <meta property="og:url" content="{data['url']}">
    <meta property="og:image" content="{og_image}">
    <meta property="og:type" content="website">

    <!-- Twitter Card Meta Tags -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{data['meta_title']}">
    <meta name="twitter:description" content="{data['desc']}">
    <meta name="twitter:image" content="{og_image}">

    <link rel="canonical" href="{data['url']}">
    <link rel="icon" type="image/x-icon" href="favicon.ico?v=2">
    <link rel="shortcut icon" href="favicon.ico?v=2">
    <link rel="stylesheet" href="style.css">"""

    # We'll find the section between <meta charset="UTF-8" /> and <link rel="stylesheet" href="style.css" />
    import re
    # Match from <meta charset to <link rel="stylesheet" href="style.css" />
    pattern = re.compile(r'<meta charset="UTF-8".*?<link rel="stylesheet" href="style.css" />', re.DOTALL | re.IGNORECASE)
    
    if pattern.search(content):
        new_content = pattern.sub(head_block, content)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        # Fallback if pattern doesn't match perfectly
        print(f"Pattern not found in {filename}, trying alternative...")
        # Just insert after <head>
        if '<head>' in content:
             # This is a bit risky if we don't remove old tags, but let's try to be precise.
             print(f"Could not precisely replace head tags in {filename}")

print("Done")
