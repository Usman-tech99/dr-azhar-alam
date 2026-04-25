import re
import os

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Extract CSS
style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
if style_match:
    css_content = style_match.group(1).strip()
    with open("style.css", "w", encoding="utf-8") as f:
        f.write(css_content)

# 2. Prepare common parts (Head, Nav, Footer, Scripts)
# Extract head part (everything before <style> and up to </head>)
head_part_match = re.search(r'(<!DOCTYPE html>.*?</head>)', content, re.DOTALL)
head_part = content[:style_match.start()] + '  <link rel="stylesheet" href="style.css" />\n</head>'

# Extract Nav
nav_match = re.search(r'(<nav id="navbar">.*?</nav>\s*<div class="mobile-menu".*?</div>)', content, re.DOTALL)
nav_part = nav_match.group(1)

# Extract Footer
footer_match = re.search(r'(<footer>.*?</footer>)', content, re.DOTALL)
footer_part = footer_match.group(1)

# Extract Scripts and Whatsapp float
scripts_match = re.search(r'(<a href="https://wa\.me/923320761997".*?</html>)', content, re.DOTALL)
scripts_part = scripts_match.group(1)

# 3. Define sections to extract for separate pages
sections = {
    'index': r'(<section id="hero">.*?</section>)',
    'about': r'(<section id="about">.*?</section>\s*<!-- ═══════════════════════════════ WHY CHOOSE ═══════════════════════════════ -->\s*<section id="why">.*?</section>)',
    'reviews': r'(<section id="reviews">.*?</section>)',
    'contact': r'(<section id="contact">.*?</section>)'
}

# 4. Generate pages
for page_name, regex in sections.items():
    match = re.search(regex, content, re.DOTALL)
    if match:
        page_content = f"""{head_part}
<body>
{nav_part}

{match.group(1)}

{footer_part}

{scripts_part}"""
        
        # update nav links for this specific page if we want (optional, but good for multi-page)
        if page_name != 'index':
            # very basic replacement for relative links to absolute
            pass
            
        with open(f"{page_name}.html", "w", encoding="utf-8") as f:
            f.write(page_content)
    else:
        print(f"Could not find section for {page_name}")

print("Split completed successfully.")
