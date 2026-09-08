from content_helpers import section_head, tile, grid, process_step, process, cta_band, hero_3d

PAGES_AMR = []

body = f"""
  <section class="hero" style="padding-bottom:0;">
    <div class="aurora"></div>
    <div class="blueprint-bg"></div>
    <div class="wrap hero-inner" style="position:relative;z-index:1;">
      <div>
        <div class="hero-tag reveal"><span class="dot"></span>AUTONOMOUS MATERIAL MOVEMENT</div>
        <h1 class="h1 grad-text reveal" style="font-size:clamp(2.2rem,4.4vw,3.6rem);">Move materials. Not people.</h1>
        <h2 style="color:var(--text-dim);font-weight:600;font-size:1.1rem;margin-bottom:20px;" class="reveal">Iyonex Autonomous Material Movement Platform</h2>
        <p class="hero-sub reveal">Our autonomous mobile robotics platform is designed to automate repetitive material transportation across factories, warehouses and industrial environments.</p>
        <div class="btn-row reveal">
          <a href="contact.html" class="btn btn-primary">Talk to Iyonex <span class="arrow" aria-hidden="true">&rarr;</span></a>
          <a href="technology.html" class="btn btn-ghost">See the Technology</a>
        </div>
      </div>
      <div class="hero-3d reveal">{hero_3d("SENSORS: ONLINE", "FLEET: COORDINATED")}</div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      {section_head("PLATFORM CAPABILITIES", "Engineered for dynamic factory floors.",
                     "Every capability below is built to operate inside real, changing industrial environments &mdash; not just controlled demo conditions.")}
      {grid(3, [
        tile("", "Autonomous Navigation", "Robots plan and follow routes across the facility without fixed rails or wires."),
        tile("", "Obstacle Detection", "Sensors continuously scan the environment to identify people, equipment and obstructions."),
        tile("", "Dynamic Path Planning", "Routes are recalculated on the fly as the floor layout or traffic changes."),
        tile("", "Point-to-Point Transportation", "Materials move directly between defined pickup and drop-off locations."),
        tile("", "Material Handling", "Interfaces designed around how materials are actually loaded and unloaded on your floor."),
        tile("", "Multi-Robot Coordination", "Multiple units share the floor and coordinate to avoid conflicts and bottlenecks."),
        tile("", "Real-Time Monitoring", "Operators can see robot status, location and task progress as it happens."),
        tile("", "Factory Workflow Integration", "The platform is designed to connect with existing production and logistics workflows."),
        tile("", "Scalable Deployment", "Start with a single unit or route, and expand coverage as requirements grow."),
      ])}
      <p class="placeholder-note reveal" style="margin-top:24px;">Specific payload capacity, speed, battery life and accuracy figures are confirmed during a site assessment and are not published as general specifications.</p>
    </div>
  </section>

  <section class="section section--tight" style="background:var(--bg-raised);border-top:1px solid var(--line-soft);border-bottom:1px solid var(--line-soft);">
    <div class="wrap">
      {section_head("HOW IT OPERATES", "Perception, planning and action, in a continuous loop.",
                     "A simplified view of how the platform reasons about its environment while it is moving material.")}
      {process([
        process_step("01", "Sense", "Onboard sensors build a live picture of the surrounding floor, racks and moving obstacles."),
        process_step("02", "Localize", "The robot determines exactly where it is on the facility map in real time."),
        process_step("03", "Plan", "A path to the next pickup or drop-off point is calculated, accounting for traffic and obstacles."),
        process_step("04", "Act", "The robot moves, adjusting speed and route continuously as conditions change."),
        process_step("05", "Report", "Task status and location are reported back to the fleet monitoring layer."),
      ])}
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      {section_head("WHERE IT FITS", "Built for repetitive, high-friction material flows.", "")}
      {grid(4, [
        tile("", "Automotive", "Line-side component delivery and intra-factory logistics."),
        tile("", "Manufacturing", "Raw material, WIP and finished-goods transportation."),
        tile("", "Electronics", "Controlled movement between sensitive process stages."),
        tile("", "Warehousing", "Repetitive transportation across storage and dispatch zones."),
      ])}
    </div>
  </section>

  {cta_band("Explore the AMR platform for your factory.",
            "Share your material movement challenge and we&rsquo;ll help you evaluate where autonomous transportation fits.",
            "Talk to Iyonex", "contact.html", "Explore All Solutions", "solutions.html")}
"""

PAGES_AMR.append(("amr.html", {
    "title": "Autonomous Mobile Robots (AMR) | Iyonex Automation",
    "desc": "The Iyonex Autonomous Material Movement Platform automates repetitive material transportation across factories, warehouses and industrial environments.",
    "active": "solutions",
}, body))
