import os

directory = r'c:\Akemi'
files = [
    'index.html', 'about.html', 'privacy-policy.html', 
    'shipping-returns.html', 'terms-of-use.html', 
    'disclosure.html', 'contact.html'
]

target_text = '<li><a href="about.html">About Us</a></li>'
# Check if it has index.html prefix (for index.html it might not, but for others it might)
# Actually, looking at previous views:
# index.html has: <li><a href="about.html">About Us</a></li>
# about.html has: <li><a href="about.html">About Us</a></li>
# privacy-policy.html has: <li><a href="about.html">About Us</a></li>

replacement_text = '<li><a href="about.html">About Us</a></li>\n            <li><a href="write-for-us.html">Write For Us</a></li>'

for filename in files:
    path = os.path.join(directory, filename)
    if not os.path.exists(path):
        continue
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'write-for-us.html' in content:
        print(f"Skipping {filename} (already has link)")
        continue
        
    if target_text in content:
        new_content = content.replace(target_text, replacement_text)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        # Try with variations if needed
        print(f"Target not found in {filename}")

print("Done")
