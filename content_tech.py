from content_helpers import section_head, tile, grid, stack_row, cta_band
from content_images import IMG_ROBOT_ARM_WHITE

PAGES_TECH = []

body = f"""
  <section class="hero" style="padding-bottom:20px;">
    <div class="aurora"></div>
    <div class="blueprint-bg"></div>
    <div class="wrap hero-inner" style="position:relative;z-index:1;">
      <div>
        <div class="eyebrow reveal">TECHNOLOGY</div>
        <h1 class="h1 grad-text reveal" style="font-size:clamp(2.2rem,4.4vw,3.2rem);">Robotics. Automation. Intelligence.</h1>
        <p class="hero-sub reveal">One interconnected technology stack &mdash; from embedded hardware to fleet software &mdash; engineered to work together as a single system.</p>
      </div>
      <div class="reveal" style="border:1px solid var(--line);overflow:hidden;box-shadow:0 24px 60px -24px rgba(46,60,90,0.18);">
        <img src="{IMG_ROBOT_ARM_WHITE}" alt="Robotic arm hardware, representative of the embedded and robotics layers of the stack" style="width:100%;height:100%;object-fit:cover;display:block;">
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="stack-list">
        {stack_row("Robotics", "HARDWARE LAYER", ["Mobile robots", "AMRs", "Robotic systems"])}
        {stack_row("Embedded Systems", "FIRMWARE LAYER", ["Controllers", "Sensors", "Motor control", "Real-time systems"])}
        {stack_row("Autonomous Systems", "INTELLIGENCE LAYER", ["Localization", "Navigation", "Path planning", "Obstacle avoidance"])}
        {stack_row("Industrial Automation", "INTEGRATION LAYER", ["PLC", "HMI", "Machine integration", "Industrial communication"])}
        {stack_row("Software", "PLATFORM LAYER", ["Robot control", "Fleet management", "Monitoring", "Integration"])}
      </div>
    </div>
  </section>

  <section class="section section--tight" id="autonomous" style="background:var(--bg-raised);border-top:1px solid var(--line-soft);border-bottom:1px solid var(--line-soft);">
    <div class="wrap">
      {section_head("ROBOT INTELLIGENCE", "What lets a robot decide, not just move.",
                     "Autonomy is the layer that turns a mobile machine into a robot capable of operating in a live factory.")}
      {grid(4, [
        tile("", "Localization", "Determining the robot&rsquo;s precise position on the facility map in real time."),
        tile("", "Navigation", "Moving safely between defined points across a shared, active floor."),
        tile("", "Path Planning", "Calculating efficient routes and adjusting them as conditions change."),
        tile("", "Obstacle Avoidance", "Detecting and safely responding to people, equipment and unexpected obstructions."),
      ])}
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      {section_head("ENGINEERING PRINCIPLES", "How we approach the stack.", "")}
      {grid(3, [
        tile("", "Built for Integration", "Every layer is designed to connect with existing machines, controllers and factory systems rather than replace them outright."),
        tile("", "Modular by Design", "Hardware, firmware and software components are structured to evolve independently as requirements change."),
        tile("", "Engineered for Reliability", "Real-time systems and industrial communication are treated as first-class engineering requirements, not afterthoughts."),
      ])}
    </div>
  </section>

  {cta_band("Curious how the stack applies to your facility?",
            "Tell us about your process and we&rsquo;ll walk through where each layer of the stack would fit.",
            "Talk to Iyonex", "contact.html", "See the AMR Platform", "amr.html")}
"""

PAGES_TECH.append(("technology.html", {
    "title": "Technology | Iyonex Automation",
    "desc": "Robotics, embedded systems, autonomous systems, industrial automation and software \u2014 the interconnected technology stack behind Iyonex Automation.",
    "active": "technology",
}, body))
