from content_helpers import section_head, tile, grid, cta_band
from content_images import (IMG_AUTOMOTIVE, IMG_MANUFACTURING, IMG_ELECTRONICS,
                             IMG_WAREHOUSE, IMG_HEAVY_INDUSTRY, IMG_ROBOT_ARM_BLUE)

PAGES_IND = []

body = f"""
  <section class="hero" style="padding-bottom:20px;">
    <div class="aurora"></div>
    <div class="blueprint-bg"></div>
    <div class="wrap" style="position:relative;z-index:1;max-width:760px;">
      <div class="eyebrow reveal">INDUSTRIES</div>
      <h1 class="h1 grad-text reveal" style="font-size:clamp(2.2rem,4.4vw,3.4rem);">Automation across industries.</h1>
      <p class="hero-sub reveal">Autonomous material movement applies wherever things need to move &mdash; reliably and repeatedly &mdash; across a facility.</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      {grid(3, [
        tile("", "Automotive", "Component movement, line-side delivery and intra-factory logistics across assembly operations.", photo=IMG_AUTOMOTIVE, photo_alt="Vehicle assembly inside an automotive factory"),
        tile("", "Manufacturing", "Raw material, work-in-progress and finished-goods transportation between production stages.", photo=IMG_MANUFACTURING, photo_alt="Robotic arms assembling a chassis on a factory line"),
        tile("", "Electronics", "Controlled movement of components and materials between sensitive process steps.", photo=IMG_ELECTRONICS, photo_alt="Automated electronics manufacturing floor"),
        tile("", "Warehousing", "Autonomous transportation and workflow automation across storage and dispatch zones.", photo=IMG_WAREHOUSE, photo_alt="Warehouse storage shelving"),
        tile("", "Heavy Industry", "Industrial material handling and repetitive transportation in demanding environments.", photo=IMG_HEAVY_INDUSTRY, photo_alt="Heavy industrial factory floor"),
        tile("", "Custom Industrial Operations", "Automation solutions designed around unique operational requirements outside a standard category.", photo=IMG_ROBOT_ARM_BLUE, photo_alt="Industrial robot arm in a factory setting"),
      ])}
      <p class="placeholder-note reveal" style="margin-top:24px;">Photography above is generic industry imagery, not a photo of Iyonex&rsquo;s own robots or a named customer site. Iyonex does not publish named customer deployments until they are officially confirmed for release.</p>
    </div>
  </section>

  <section class="section section--tight" style="background:var(--bg-raised);border-top:1px solid var(--line-soft);border-bottom:1px solid var(--line-soft);">
    <div class="wrap">
      {section_head("HOW WE EVALUATE FIT", "Every facility is different.",
                     "Rather than fitting your operation to a fixed product, we start by understanding your specific material flow.")}
      {grid(3, [
        tile("", "Workflow Assessment", "We study how material currently moves through your facility, including bottlenecks and manual steps."),
        tile("", "Environment Mapping", "Floor layout, traffic patterns and existing infrastructure are reviewed before any deployment plan is proposed."),
        tile("", "Phased Deployment", "Solutions are typically introduced on a defined route or process first, then expanded once validated."),
      ])}
    </div>
  </section>

  {cta_band("Not sure where your industry fits?",
            "Tell us about your operation and we&rsquo;ll help identify where automation would create the most value.",
            "Talk to Iyonex", "contact.html", "Explore Solutions", "solutions.html")}
"""

PAGES_IND.append(("industries.html", {
    "title": "Industries | Iyonex Automation",
    "desc": "Iyonex Automation applies autonomous robotics and industrial automation across automotive, manufacturing, electronics, warehousing and heavy industry.",
    "active": "industries",
}, body))
