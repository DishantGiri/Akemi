import os

directory = r'c:\Akemi'
target_text = 'https://secureofficialsite.store/buy-akemi'
replacement_text = 'https://secureofficialsite.store/buy-akemi-hair-glow'

# We should also check for variations without the trailing slash or with it.
# The user provided: https://secureofficialsite.store/buy-akemi-hair-glow

for filename in os.listdir(directory):
    if filename.endswith('.html'):
        path = os.path.join(directory, filename)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if target_text in content:
            # Be careful not to replace it if it's already the long version
            # But the long version includes the short version as a prefix.
            # So we should replace only exact matches or handle it.
            # Replace 'buy-akemi' but NOT 'buy-akemi-hair-glow'
            
            # Use regex or simple replace if we know the old one is exactly 'buy-akemi'
            new_content = content.replace(target_text + '"', replacement_text + '"')
            new_content = new_content.replace(target_text + "'", replacement_text + "'")
            
            if new_content != content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filename}")

print("Done")
