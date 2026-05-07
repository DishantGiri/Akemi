import os

directory = r'c:\Akemi'
files = [
    'index.html', 'about.html', 'privacy-policy.html', 
    'shipping-returns.html', 'terms-of-use.html', 
    'disclosure.html', 'contact.html', 'write-for-us.html'
]

target_text_1 = '<link rel="icon" type="image/x-icon" href="favicon.ico?v=2">'
replacement_text_1 = '<link rel="icon" type="image/png" href="favicon.png?v=3">'

target_text_2 = '<link rel="shortcut icon" href="favicon.ico?v=2">'
replacement_text_2 = '<link rel="shortcut icon" href="favicon.png?v=3">'

for filename in files:
    path = os.path.join(directory, filename)
    if not os.path.exists(path):
        continue
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace(target_text_1, replacement_text_1)
    content = content.replace(target_text_2, replacement_text_2)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")

print("Done")
