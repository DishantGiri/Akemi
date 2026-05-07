import os

path = r'c:\Akemi\index.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# The specific block around line 1360
target = """      </div>

  <footer class="footer">"""

replacement = """      </div>
    </div>
  </section>

  <footer class="footer">"""

if target in content:
    new_content = content.replace(target, replacement)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Success")
else:
    # Try with CRLF just in case
    target_crlf = target.replace('\n', '\r\n')
    if target_crlf in content:
        replacement_crlf = replacement.replace('\n', '\r\n')
        new_content = content.replace(target_crlf, replacement_crlf)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Success (CRLF)")
    else:
        # Try to find the line by line content
        lines = content.splitlines(keepends=True)
        found = False
        for i in range(len(lines)-2):
            if '      </div>' in lines[i] and lines[i+1].strip() == '' and '  <footer class="footer">' in lines[i+2]:
                # Found the spot
                lines[i] = lines[i] + '    </div>\n  </section>\n'
                found = True
                break
        if found:
            with open(path, 'w', encoding='utf-8') as f:
                f.writelines(lines)
            print("Success (Line search)")
        else:
            print("Target not found")
