import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Reviews section
reviews_new = """      <div class="reviews__grid">
        <!-- Review 1 -->
        <div class="reviews__card">
          <div class="reviews__card-header">
            <div class="reviews__avatar-container">
              <img src="public/review_avatar_1.png" alt="Jason Miller" class="reviews__avatar-img" />
            </div>
            <div class="reviews__user-info">
              <span class="reviews__user-name">Jason Miller, 34</span>
              <span class="reviews__user-verify">Austin, USA</span>
            </div>
          </div>
          <p class="reviews__card-text">
            "I started noticing my crown thinning last year, especially under bright light. A friend suggested Akemi Hair Glow, and honestly, I didn't expect much. But after a few weeks of using the akemi hair glow spray, my hair started looking fuller. Not dramatic overnight, but enough that I stopped worrying every time I checked the mirror."
          </p>
        </div>

        <!-- Review 2 -->
        <div class="reviews__card">
          <div class="reviews__card-header">
            <div class="reviews__avatar-container">
              <img src="public/review_avatar_2.png" alt="Daniel Brooks" class="reviews__avatar-img" />
            </div>
            <div class="reviews__user-info">
              <span class="reviews__user-name">Daniel Brooks, 41</span>
              <span class="reviews__user-verify">Manchester, UK</span>
            </div>
          </div>
          <p class="reviews__card-text">
            "I've tried oils, supplements, even random shampoos… nothing really stuck. What I liked about Akemi hair growth spray is how easy it fits into my routine. Spray, massage, done. My hair doesn't feel greasy anymore, and I've noticed less hair fall in the shower. It just feels like my hair is getting stronger again."
          </p>
        </div>

        <!-- Review 3 -->
        <div class="reviews__card">
          <div class="reviews__card-header">
            <div class="reviews__avatar-container">
              <img src="public/review_avatar_3.png" alt="Liam O'Connor" class="reviews__avatar-img" />
            </div>
            <div class="reviews__user-info">
              <span class="reviews__user-name">Liam O'Connor, 37</span>
              <span class="reviews__user-verify">Dublin, Ireland</span>
            </div>
          </div>
          <p class="reviews__card-text">
            "Didn't even plan to buy this at first I was just going through akemi hair glow reviews late one night. Ended up ordering it anyway. After about a month, I noticed my hairline didn't look as bad as before. Not perfect, but definitely better. My wife even pointed it out, which says a lot."
          </p>
        </div>

        <!-- Review 4 -->
        <div class="reviews__card">
          <div class="reviews__card-header">
            <div class="reviews__avatar-container">
              <img src="public/review_avatar_4.png" alt="Ethan Carter" class="reviews__avatar-img" />
            </div>
            <div class="reviews__user-info">
              <span class="reviews__user-name">Ethan Carter, 29</span>
              <span class="reviews__user-verify">Toronto, Canada</span>
            </div>
          </div>
          <p class="reviews__card-text">
            "For me, it started with seeing too much hair on my pillow every morning. I switched my routine completely and added this akemi hair growth serum. It doesn't feel heavy like oil, which I like. My hair looks healthier now, especially around the front. It's subtle, but I feel way more confident going out."
          </p>
        </div>
        
        <!-- Review 5 -->
        <div class="reviews__card">
          <div class="reviews__card-header">
            <div class="reviews__avatar-container">
              <img src="public/review_avatar_1.png" alt="Oliver Hayes" class="reviews__avatar-img" />
            </div>
            <div class="reviews__user-info">
              <span class="reviews__user-name">Oliver Hayes, 45</span>
              <span class="reviews__user-verify">Sydney, AU</span>
            </div>
          </div>
          <p class="reviews__card-text">
            "I kept searching best hair growth product hoping to see something realistic, not overhyped stuff. Gave it a shot anyway. After a couple months, my hair just looks… less tired. Thicker in some spots. It's not magic, but it feels like progress, which is honestly all I wanted."
          </p>
        </div>

        <!-- Review 6 -->
        <div class="reviews__card">
          <div class="reviews__card-header">
            <div class="reviews__avatar-container">
              <img src="public/review_avatar_2.png" alt="Noah Williams" class="reviews__avatar-img" />
            </div>
            <div class="reviews__user-info">
              <span class="reviews__user-name">Noah Williams, 32</span>
              <span class="reviews__user-verify">Auckland, NZ</span>
            </div>
          </div>
          <p class="reviews__card-text">
            "I'm someone who hates complicated routines. That's why I avoided most akemi hair products at first. But this one's different just spray and go. Been using it before work daily, and my hair doesn't look as flat anymore. Even my barber mentioned it last time. That was enough validation for me."
          </p>
        </div>
      </div>"""
html = re.sub(r'<div class="reviews__grid">.*?</div>\s*<div class="reviews__note-box">', reviews_new + '\n\n      <div class="reviews__note-box">', html, flags=re.DOTALL)

# 2. Update Footer
footer_new = """  <!-- ── Footer ────────────────────────────────────────── -->
  <footer class="footer">
    <div class="footer__container">
      <div class="footer__content">
        <h3 class="footer__brand">Akemi Hair Glow</h3>
        <p class="footer__text">
          Targeted root support for a healthier-looking scalp and fuller-feeling hair.
        </p>
      </div>

      <div class="footer__links">
        <div class="footer__col">
          <h4 class="footer__col-title">Support</h4>
          <ul class="footer__nav">
            <li><a href="#contact">Contact Support</a></li>
            <li><a href="#shipping">Shipping Policy</a></li>
            <li><a href="#returns">Refund Policy</a></li>
          </ul>
        </div>
        <div class="footer__col">
          <h4 class="footer__col-title">Legal</h4>
          <ul class="footer__nav">
            <li><a href="#terms">Terms of Use</a></li>
            <li><a href="#privacy">Privacy Policy</a></li>
          </ul>
        </div>
      </div>
    </div>
    <div class="footer__bottom">
      <p>&copy; 2026 Akemi Hair Glow. All rights reserved.</p>
      <p style="font-size: 0.8rem; margin-top: 5px; color: #888;">This Akemi Hair Glow official product page was last updated in April 2026 to reflect current product positioning, bundle offer details, buyer questions, and checkout trust information.</p>
    </div>
  </footer>"""
html = re.sub(r'<!-- ── Footer ────────────────────────────────────────── -->.*?</footer>', footer_new, html, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
