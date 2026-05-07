import os

directory = r'c:\Akemi'
files = [
    'about.html', 'privacy-policy.html', 
    'shipping-returns.html', 'terms-of-use.html', 
    'disclosure.html', 'contact.html', 'write-for-us.html'
]

target_text = '<link rel="stylesheet" href="style.css" />'
replacement_text = '<link rel="icon" type="image/x-icon" href="favicon.ico">\n  <link rel="stylesheet" href="style.css" />'

for filename in files:
    path = os.path.join(directory, filename)
    if not os.path.exists(path):
        continue
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'favicon.ico' in content:
        print(f"Skipping {filename} (already has favicon)")
        continue
        
    if target_text in content:
        new_content = content.replace(target_text, replacement_text)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        print(f"Target not found in {filename}")

print("Done")
