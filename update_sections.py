import re

with open("c:\\Akemi\\index.html", "r", encoding="utf-8") as f:
    html = f.read()

new_sections_html = """
  <!-- ── Section: Formula, Ingredients & Scalp Delivery ──────────────────────── -->
  <section class="formula" id="formula" style="padding: 4rem 1rem; background: var(--c-bg);">
    <div style="max-width: 1200px; margin: 0 auto;">
      <h2 style="font-size: clamp(2rem, 3vw, 2.5rem); margin-bottom: 1rem; text-align: center;">Formula, Ingredients & <span style="color: var(--c-primary);">Scalp Delivery System</span></h2>
      <p style="text-align: center; max-width: 800px; margin: 0 auto 2rem; color: var(--c-text-muted);">Akemi Hair Glow is built around a direct scalp delivery format. The spray design helps users apply the formula where it matters most, instead of wasting product on the outer hair strands.</p>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; align-items: center;">
        <div>
          <h3 style="font-size: 1.5rem; margin-bottom: 1rem;">Formula Style</h3>
          <ul style="list-style: none; padding: 0;">
            <li style="margin-bottom: 0.5rem;">&#10003; Lightweight topical spray</li>
            <li style="margin-bottom: 0.5rem;">&#10003; Fast-absorbing scalp application</li>
            <li style="margin-bottom: 0.5rem;">&#10003; Non-greasy finish</li>
            <li style="margin-bottom: 0.5rem;">&#10003; Leave-in daily-use format</li>
            <li style="margin-bottom: 0.5rem;">&#10003; Made for targeted root support</li>
          </ul>
        </div>
        <div style="text-align: center;">
           <img src="public/who-should-buy.webp" alt="akemi hair glow ingredients biotin caffeine ginger root" style="max-width: 100%; border-radius: 8px;" />
        </div>
        <div>
          <h3 style="font-size: 1.5rem; margin-bottom: 1rem;">Ingredient Direction</h3>
          <p style="color: var(--c-text-muted); line-height: 1.6;">The Akemi Hair Glow ingredients include commonly used hair-support components such as biotin, caffeine, castor oil, ginger root extract, Fo-Ti, and aminexil. These ingredients are positioned to support scalp freshness, root strength, and fuller-looking hair appearance.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ── Section: Ingredient Support ──────────────────────── -->
  <section class="ingredient-support" id="ingredient-support" style="padding: 4rem 1rem; background: #fff;">
    <div style="max-width: 1000px; margin: 0 auto;">
      <h2 style="font-size: clamp(2rem, 3vw, 2.5rem); margin-bottom: 1rem; text-align: center;">Ingredient Support, <span style="color: var(--c-primary);">What Each Component Does</span></h2>
      <p style="text-align: center; margin-bottom: 3rem; color: var(--c-text-muted);">The Akemi Hair Glow formula is built around a combination of ingredients commonly used in scalp and hair-support routines. Each one plays a role in supporting how hair looks and feels over time.</p>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
        <div style="background: var(--c-bg); padding: 1.5rem; border-radius: 8px;">
          <h4 style="font-size: 1.25rem; margin-bottom: 0.5rem; color: var(--c-primary);">Biotin (Vitamin B7)</h4>
          <p style="color: var(--c-text-muted);">Often associated with keratin support, biotin is commonly used in hair care to help improve the appearance of stronger, more resilient strands.</p>
        </div>
        <div style="background: var(--c-bg); padding: 1.5rem; border-radius: 8px;">
          <h4 style="font-size: 1.25rem; margin-bottom: 0.5rem; color: var(--c-primary);">Caffeine</h4>
          <p style="color: var(--c-text-muted);">Widely used in scalp-focused formulas, caffeine is included to support the look of energized roots and a refreshed scalp environment.</p>
        </div>
        <div style="background: var(--c-bg); padding: 1.5rem; border-radius: 8px;">
          <h4 style="font-size: 1.25rem; margin-bottom: 0.5rem; color: var(--c-primary);">Aminexil</h4>
          <p style="color: var(--c-text-muted);">Positioned in many hair routines to help maintain the flexibility of hair roots, which may contribute to better overall support at the scalp level.</p>
        </div>
        <div style="background: var(--c-bg); padding: 1.5rem; border-radius: 8px;">
          <h4 style="font-size: 1.25rem; margin-bottom: 0.5rem; color: var(--c-primary);">Castor Oil</h4>
          <p style="color: var(--c-text-muted);">A traditional ingredient known for conditioning properties, helping hair feel smoother while supporting scalp moisture balance.</p>
        </div>
        <div style="background: var(--c-bg); padding: 1.5rem; border-radius: 8px;">
          <h4 style="font-size: 1.25rem; margin-bottom: 0.5rem; color: var(--c-primary);">Ginger Root Extract</h4>
          <p style="color: var(--c-text-muted);">Commonly used in cosmetic formulations to support scalp freshness and circulation-related appearance.</p>
        </div>
        <div style="background: var(--c-bg); padding: 1.5rem; border-radius: 8px;">
          <h4 style="font-size: 1.25rem; margin-bottom: 0.5rem; color: var(--c-primary);">Fo-Ti (He Shou Wu)</h4>
          <p style="color: var(--c-text-muted);">A botanical ingredient with a long history in hair traditions, often associated with supporting overall hair vitality.</p>
        </div>
      </div>
      <p style="text-align: center; margin-top: 2rem; font-weight: 500;">Together, these ingredients are positioned to support a healthier-looking scalp environment, which plays a key role in how hair appears over time.</p>
    </div>
  </section>

  <!-- ── Section: What to Expect Over Time ──────────────────────── -->
  <section class="expectations" style="padding: 4rem 1rem; background: var(--c-bg);">
    <div style="max-width: 800px; margin: 0 auto; text-align: center;">
      <h2 style="font-size: clamp(2rem, 3vw, 2.5rem); margin-bottom: 1rem;">What to <span style="color: var(--c-primary);">Expect Over Time</span></h2>
      <p style="color: var(--c-text-muted); margin-bottom: 2rem;">Hair routines require consistency, and visible changes usually happen gradually, not instantly. Here’s what many users typically notice when using a daily scalp spray consistently:</p>
      
      <div style="text-align: left; background: #fff; padding: 2rem; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
        <p style="margin-bottom: 1rem;"><strong>First few weeks:</strong> Hair may feel cleaner at the roots, with reduced visible buildup and improved manageability.</p>
        <p style="margin-bottom: 1rem;"><strong>Weeks 3–6:</strong> Less noticeable shedding appearance and improved overall hair feel.</p>
        <p style="margin-bottom: 1rem;"><strong>Weeks 6–12:</strong> Fuller-looking coverage, especially in areas like the crown or hairline.</p>
        <hr style="border: 0; border-top: 1px solid #eee; margin: 1.5rem 0;" />
        <p style="color: var(--c-text-muted); font-size: 0.95rem;">Because every scalp and hair condition is different, results can vary. What matters most is staying consistent with daily use and giving your routine enough time to work.</p>
      </div>
    </div>
  </section>

  <!-- ── Section: Size Guide & Fit ──────────────────────── -->
  <section class="size-guide" style="padding: 4rem 1rem; background: #fff;">
    <div style="max-width: 1000px; margin: 0 auto; display: flex; flex-wrap: wrap; gap: 2rem; align-items: center;">
      <div style="flex: 1; min-width: 300px;">
        <h2 style="font-size: clamp(2rem, 3vw, 2.5rem); margin-bottom: 1rem;">Size Guide / <span style="color: var(--c-primary);">Fit / Color Options</span></h2>
        <p style="color: var(--c-text-muted); margin-bottom: 1rem;">Akemi Hair Glow does not require a size guide because it is a topical scalp spray. The product is designed for different hair lengths, textures, and thinning patterns.</p>
        <h3 style="font-size: 1.2rem; margin-bottom: 0.5rem;">Best Application Areas:</h3>
        <ul style="list-style: none; padding: 0; color: var(--c-text-muted);">
          <li>&#10003; Crown thinning</li>
          <li>&#10003; Hairline support</li>
          <li>&#10003; Sparse-looking patches</li>
          <li>&#10003; Part line visibility</li>
          <li>&#10003; Weak-looking roots</li>
        </ul>
        <p style="margin-top: 1rem; font-size: 0.95rem;">Whether the buyer searches Akemi hair care, Akemi hair serum, or Akemi hair therapy, the main fit factor is not hair length. It is consistent scalp application.</p>
      </div>
      <div style="flex: 1; min-width: 300px; text-align: center;">
        <img src="public/how-it-works.webp" alt="akemi hair glow spray for crown and hairline thinning" style="max-width: 100%; border-radius: 8px;" />
      </div>
    </div>
  </section>

  <!-- ── Section: Who It's For ──────────────────────── -->
  <section class="who-its-for" style="padding: 4rem 1rem; background: var(--c-bg);">
    <div style="max-width: 1000px; margin: 0 auto;">
      <h2 style="font-size: clamp(2rem, 3vw, 2.5rem); margin-bottom: 2rem; text-align: center;">Who It’s For <span style="color: var(--c-primary);">And Who It’s Not</span></h2>
      <p style="text-align: center; max-width: 800px; margin: 0 auto 3rem;">Akemi Hair Glow is designed for men who want a simple, direct approach to improving the look of thinning hair.</p>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
        <div style="background: #fff; padding: 2rem; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
          <h3 style="color: #28a745; margin-bottom: 1rem; display: flex; align-items: center; gap: 0.5rem;"><span style="font-size: 1.5rem;">&#10004;</span> Good Fit For:</h3>
          <ul style="list-style: none; padding: 0; line-height: 1.8;">
            <li>Early-stage thinning</li>
            <li>Crown or hairline visibility</li>
            <li>Increased hair fall in daily routine</li>
            <li>Users who prefer non-greasy solutions</li>
            <li>Men looking for a simple daily spray routine</li>
          </ul>
        </div>
        <div style="background: #fff; padding: 2rem; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
          <h3 style="color: #dc3545; margin-bottom: 1rem; display: flex; align-items: center; gap: 0.5rem;"><span style="font-size: 1.5rem;">&#10006;</span> May Not Be Ideal For:</h3>
          <ul style="list-style: none; padding: 0; line-height: 1.8;">
            <li>Completely bald areas</li>
            <li>Medically diagnosed hair loss conditions</li>
            <li>Those expecting immediate or overnight changes</li>
            <li>Untreated scalp conditions requiring medical care</li>
          </ul>
        </div>
      </div>
      <p style="text-align: center; margin-top: 2rem; font-weight: 500;">Being clear about fit helps users choose confidently, and get the most out of their routine.</p>
    </div>
  </section>

  <!-- ── Section: Safety & Usage Considerations ──────────────────────── -->
  <section class="safety-usage" style="padding: 4rem 1rem; background: #fff;">
    <div style="max-width: 1000px; margin: 0 auto; display: flex; flex-wrap: wrap; gap: 2rem;">
      <div style="flex: 1; min-width: 300px;">
        <h2 style="font-size: 2rem; margin-bottom: 1rem;">Safety & <span style="color: var(--c-primary);">Usage Considerations</span></h2>
        <p style="margin-bottom: 1rem;">Akemi Hair Glow is designed for external use as part of a daily scalp routine.</p>
        <p style="margin-bottom: 0.5rem; font-weight: 600;">To ensure the best experience:</p>
        <ul style="list-style: disc; padding-left: 1.5rem; margin-bottom: 1rem; color: var(--c-text-muted); line-height: 1.6;">
          <li>Apply only to a clean, dry, or slightly damp scalp</li>
          <li>Avoid use on irritated or damaged skin</li>
          <li>Perform a patch test before first use</li>
          <li>Discontinue use if irritation occurs</li>
        </ul>
        <p style="font-size: 0.95rem; color: var(--c-text-muted);">If you have existing scalp conditions or concerns, it’s always a good idea to consult a qualified professional before starting any new product.</p>
      </div>
      
      <div style="flex: 1; min-width: 300px;">
        <h2 style="font-size: 2rem; margin-bottom: 1rem;">Pros & <span style="color: var(--c-primary);">Considerations</span></h2>
        <p style="margin-bottom: 1rem;">No product is one-size-fits-all, and understanding both sides helps you make a more confident decision.</p>
        
        <h3 style="font-size: 1.1rem; color: #28a745; margin-bottom: 0.5rem;">&#10004; What Users Like:</h3>
        <ul style="list-style: none; padding: 0; margin-bottom: 1rem; font-size: 0.95rem;">
          <li>Lightweight, non-greasy finish</li>
          <li>Simple spray-and-massage routine</li>
          <li>Targets scalp directly</li>
          <li>Easy to fit into daily life</li>
          <li>No complicated systems or multiple steps</li>
        </ul>
        
        <h3 style="font-size: 1.1rem; color: #dc3545; margin-bottom: 0.5rem;">&#9888; What to Keep in Mind:</h3>
        <ul style="list-style: none; padding: 0; margin-bottom: 1rem; font-size: 0.95rem;">
          <li>Requires consistent daily use</li>
          <li>Results vary depending on individual hair condition</li>
          <li>Not intended as a medical treatment</li>
        </ul>
      </div>
    </div>
  </section>

  <!-- ── Section: Comparison Table ──────────────────────── -->
  <section class="comparison" style="padding: 4rem 1rem; background: var(--c-bg);">
    <div style="max-width: 1000px; margin: 0 auto;">
      <h2 style="font-size: clamp(2rem, 3vw, 2.5rem); margin-bottom: 2rem; text-align: center;">Akemi Hair Glow vs <span style="color: var(--c-primary);">Other Hair Products</span></h2>
      
      <div style="overflow-x: auto;">
        <table style="width: 100%; border-collapse: collapse; background: #fff; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
          <thead>
            <tr style="background: var(--c-primary); color: #fff;">
              <th style="padding: 1rem; text-align: left;">Feature</th>
              <th style="padding: 1rem; text-align: center;">Akemi Hair Glow</th>
              <th style="padding: 1rem; text-align: center;">Hair Oils</th>
              <th style="padding: 1rem; text-align: center;">Pills</th>
              <th style="padding: 1rem; text-align: center;">Shampoos</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom: 1px solid #eee;">
              <td style="padding: 1rem; font-weight: 500;">Direct scalp targeting</td>
              <td style="padding: 1rem; text-align: center; color: #28a745;">Yes</td>
              <td style="padding: 1rem; text-align: center;">Sometimes</td>
              <td style="padding: 1rem; text-align: center; color: #dc3545;">No</td>
              <td style="padding: 1rem; text-align: center;">Limited</td>
            </tr>
            <tr style="border-bottom: 1px solid #eee;">
              <td style="padding: 1rem; font-weight: 500;">Non-greasy feel</td>
              <td style="padding: 1rem; text-align: center; color: #28a745;">Yes</td>
              <td style="padding: 1rem; text-align: center; color: #dc3545;">Often no</td>
              <td style="padding: 1rem; text-align: center; color: #28a745;">Yes</td>
              <td style="padding: 1rem; text-align: center; color: #28a745;">Yes</td>
            </tr>
            <tr style="border-bottom: 1px solid #eee;">
              <td style="padding: 1rem; font-weight: 500;">Easy daily use</td>
              <td style="padding: 1rem; text-align: center; color: #28a745;">Yes</td>
              <td style="padding: 1rem; text-align: center;">Medium</td>
              <td style="padding: 1rem; text-align: center; color: #28a745;">Yes</td>
              <td style="padding: 1rem; text-align: center;">Medium</td>
            </tr>
            <tr style="border-bottom: 1px solid #eee;">
              <td style="padding: 1rem; font-weight: 500;">Supports root area</td>
              <td style="padding: 1rem; text-align: center; color: #28a745;">Yes</td>
              <td style="padding: 1rem; text-align: center;">Limited</td>
              <td style="padding: 1rem; text-align: center;">Indirect</td>
              <td style="padding: 1rem; text-align: center;">Limited</td>
            </tr>
            <tr style="border-bottom: 1px solid #eee;">
              <td style="padding: 1rem; font-weight: 500;">Leave-in convenience</td>
              <td style="padding: 1rem; text-align: center; color: #28a745;">Yes</td>
              <td style="padding: 1rem; text-align: center;">Sometimes heavy</td>
              <td style="padding: 1rem; text-align: center; color: #dc3545;">Not topical</td>
              <td style="padding: 1rem; text-align: center; color: #dc3545;">Rinse-off</td>
            </tr>
            <tr>
              <td style="padding: 1rem; font-weight: 500;">Good for styling</td>
              <td style="padding: 1rem; text-align: center; color: #28a745;">Yes</td>
              <td style="padding: 1rem; text-align: center; color: #dc3545;">Often difficult</td>
              <td style="padding: 1rem; text-align: center; color: #28a745;">Yes</td>
              <td style="padding: 1rem; text-align: center; color: #28a745;">Yes</td>
            </tr>
          </tbody>
        </table>
      </div>
      
      <p style="text-align: center; margin-top: 2rem;">Akemi Hair Glow spray stands out because it targets the scalp directly while keeping the routine clean and simple.</p>
    </div>
  </section>

  <!-- ── Section: Shipping & Guarantee ──────────────────────── -->
  <section class="shipping-guarantee" style="padding: 4rem 1rem; background: #fff;">
    <div style="max-width: 1000px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 3rem;">
      <div>
        <h2 style="font-size: 2rem; margin-bottom: 1rem;">Shipping & <span style="color: var(--c-primary);">Returns</span></h2>
        <p style="margin-bottom: 1rem;">Orders placed through the official Akemi Hair Glow checkout are processed with shipping details confirmed during checkout. The page also notes that shipping and tax are settled during checkout confirmation.</p>
        <h3 style="font-size: 1.2rem; margin-bottom: 0.5rem;">Shipping Highlights:</h3>
        <ul style="list-style: disc; padding-left: 1.5rem; margin-bottom: 1rem; color: var(--c-text-muted);">
          <li>Secure online checkout</li>
          <li>Shipping cost shown before confirmation</li>
          <li>Bundle orders available</li>
          <li>Package protection option available</li>
          <li>Support access for order questions</li>
        </ul>
        <p style="font-size: 0.95rem;">For buyers searching Akemi Hair Glow where to buy, the safest option is the official checkout page to avoid fake listings, expired offers, or unsupported sellers.</p>
      </div>
      
      <div>
        <h2 style="font-size: 2rem; margin-bottom: 1rem;">Money-Back <span style="color: var(--c-primary);">Guarantee</span></h2>
        <p style="margin-bottom: 1rem;">Akemi Hair Glow includes a 30-day money-back guarantee. This gives buyers time to try the spray and decide whether it fits their routine.</p>
        <h3 style="font-size: 1.2rem; margin-bottom: 0.5rem;">How It Works:</h3>
        <p style="color: var(--c-text-muted); margin-bottom: 1rem;">Use Akemi Hair Glow consistently, monitor how your scalp and hair feel, and contact support within the guarantee window if you are not satisfied.</p>
        <div style="background: rgba(184, 115, 51, 0.05); border-left: 3px solid var(--c-accent); padding: 1rem; border-radius: 4px;">
          <p style="font-size: 0.95rem;">Akemi Hair Glow offers a 30-day money-back guarantee, allowing customers to try the product with less risk. Buyers should order from the official site and follow the return instructions provided by customer support.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ── Section: Simple Habits ──────────────────────── -->
  <section class="simple-habits" style="padding: 4rem 1rem; background: var(--c-bg);">
    <div style="max-width: 800px; margin: 0 auto; text-align: center;">
      <h2 style="font-size: clamp(2rem, 3vw, 2.5rem); margin-bottom: 1rem;">Simple Habits That Support <span style="color: var(--c-primary);">Better Hair Appearance</span></h2>
      <p style="color: var(--c-text-muted); margin-bottom: 2rem;">While a product can support your routine, daily habits also play a role in how your hair looks and feels. A few simple practices can make a difference:</p>
      
      <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 1rem;">
        <span style="background: #fff; padding: 0.75rem 1.5rem; border-radius: 50px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">Maintain a balanced diet</span>
        <span style="background: #fff; padding: 0.75rem 1.5rem; border-radius: 50px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">Avoid excessive heat styling</span>
        <span style="background: #fff; padding: 0.75rem 1.5rem; border-radius: 50px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">Keep scalp clean & buildup-free</span>
        <span style="background: #fff; padding: 0.75rem 1.5rem; border-radius: 50px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">Manage stress levels</span>
        <span style="background: #fff; padding: 0.75rem 1.5rem; border-radius: 50px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">Stay consistent with routine</span>
      </div>
      
      <p style="margin-top: 2rem; font-weight: 500;">These small habits, combined with a targeted scalp approach, can help improve overall hair appearance over time.</p>
    </div>
  </section>
"""

# Insert right before <!-- ── Section: Security
if '<!-- ── Section: Security' in html:
    html = html.replace('<!-- ── Section: Security', new_sections_html + '\n  <!-- ── Section: Security')
else:
    html += new_sections_html

# Update Footer "Last Updated April 2026"
html = re.sub(r'Last updated \d{4}', 'Last updated April 2026', html)

with open("c:\\Akemi\\index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Updated successfully")
