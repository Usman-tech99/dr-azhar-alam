import re
import glob

files = glob.glob("*.html")
# don't process dr-azhar-alam.html if it's there
files = [f for f in files if f in ["index.html", "about.html", "reviews.html", "contact.html"]]

nav_replacement = """      <div class="nav-links">
        <a href="index.html">Home</a>
        <a href="about.html">About & Why Choose</a>
        <a href="reviews.html">Reviews</a>
        <a href="contact.html">Contact</a>
        <a href="tel:+923320761997" class="nav-cta"><i class="fa fa-phone"></i> Book Now</a>
      </div>"""

mobile_replacement = """  <div class="mobile-menu" id="mobileMenu">
    <a href="index.html"><i class="fa fa-home"
        style="margin-right:10px;color:var(--gold)"></i>Home</a>
    <a href="about.html"><i class="fa fa-user-md"
        style="margin-right:10px;color:var(--gold)"></i>About</a>
    <a href="reviews.html"><i class="fa fa-comments"
        style="margin-right:10px;color:var(--gold)"></i>Reviews</a>
    <a href="contact.html"><i class="fa fa-map-marker-alt"
        style="margin-right:10px;color:var(--gold)"></i>Contact</a>
    <a href="tel:+923320761997" style="color:var(--gold-light);font-weight:600;margin-top:10px;"><i class="fa fa-phone"
        style="margin-right:10px;"></i>Call Now: +92 332 0761997</a>
  </div>"""

footer_quick_links = """        <div class="footer-col">
          <h4>Quick Links</h4>
          <a href="index.html">Home</a>
          <a href="about.html">About Dr. Azhar Alam</a>
          <a href="about.html">Why Choose Us</a>
          <a href="reviews.html">Patient Reviews</a>
          <a href="contact.html">Contact & Location</a>
        </div>

        <div class="footer-col">
          <h4>Specialties</h4>
          <a href="about.html">Bariatric Surgery</a>
          <a href="about.html">Laparoscopic Surgery</a>
          <a href="about.html">Laser Piles Surgery</a>
          <a href="about.html">Gallbladder Surgery</a>
          <a href="about.html">Hernia Surgery</a>
        </div>"""

for f in files:
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()
    
    # Replace Nav links
    content = re.sub(r'<div class="nav-links">.*?</div>', nav_replacement, content, flags=re.DOTALL)
    
    # Replace mobile menu
    content = re.sub(r'<div class="mobile-menu" id="mobileMenu">.*?</div>', mobile_replacement, content, flags=re.DOTALL)

    # Replace footer links
    content = re.sub(r'<div class="footer-col">\s*<h4>Quick Links</h4>.*?</div>\s*</div>', footer_quick_links + '\n      </div>', content, flags=re.DOTALL)

    with open(f, "w", encoding="utf-8") as file:
        file.write(content)
        
print("Updated navigation in all HTML files.")
