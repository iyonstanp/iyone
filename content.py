# Page content for the Iyonex Automation site.
from content_helpers import section_head, tile, grid, process_step, process, cta_band, stack_row, hero_3d
from content_images import IMG_WAREHOUSE, IMG_MANUFACTURING

PAGES = []

# ============================================================= HOME =====
home_body = f"""
  <section class="hero hero--photo" style="background-image:url('{IMG_MANUFACTURING}');">
    <div class="aurora"></div>
    <div class="wrap hero-inner" style="position:relative;z-index:1;">
      <div>
        <div class="hero-tag reveal"><span class="dot"></span>AUTONOMOUS INDUSTRIAL ROBOTICS</div>
        <h1 class="h1 grad-text reveal">Intelligent robotics for smarter factories.</h1>
        <p class="hero-sub reveal">Autonomous robotics and industrial automation designed to transform material movement, factory operations and industrial workflows.</p>
        <div class="btn-row reveal">
          <a href="solutions.html" class="btn btn-primary">Explore Solutions <span class="arrow" aria-hidden="true">&rarr;</span></a>
          <a href="contact.html" class="btn btn-ghost">Talk to Iyonex</a>
        </div>
      </div>
      <div class="hero-3d reveal">
        {hero_3d()}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      {section_head("THE PROBLEM", "Factories are automated. Material movement still isn&rsquo;t.",
                     "Modern factories run advanced machines, but material still moves between them by forklift, fixed conveyor and manual handling.")}
      {grid(4, [
        tile("", "Manual Dependency", "Repetitive material transportation still depends heavily on human effort."),
        tile("", "Inefficient Movement", "Unoptimized material flow creates delays between production processes."),
        tile("", "Safety Challenges", "Manual transportation and forklift movement can create unnecessary operational risks."),
        tile("", "Limited Scalability", "Traditional systems can be difficult and expensive to adapt as factory requirements change."),
      ])}
      <p class="lede reveal" style="margin-top:48px;max-width:760px;">Iyonex is building the bridge between robotics and real-world factory operations.</p>
    </div>
  </section>

  <section class="section section--tight" style="background:var(--bg-raised);border-top:1px solid var(--line-soft);border-bottom:1px solid var(--line-soft);position:relative;overflow:hidden;">
    <div class="wrap grid-2" style="align-items:center;position:relative;z-index:1;">
      <div class="reveal">
        <div class="eyebrow">FLAGSHIP SOLUTION</div>
        <h2 class="h2" style="margin-bottom:10px;">Move materials. Not people.</h2>
        <p class="body-copy" style="margin-bottom:26px;">The Iyonex Autonomous Material Movement Platform automates repetitive transportation across factories and warehouses &mdash; sensing, planning and coordinating without fixed rails or wires.</p>
        <div class="badge-row" style="margin-bottom:30px;">
          {"".join(f'<span class="badge">{f}</span>' for f in ["Autonomous navigation","Multi-robot coordination","Real-time monitoring","Factory integration"])}
        </div>
        <a href="amr.html" class="btn btn-primary">Explore AMR Platform <span class="arrow" aria-hidden="true">&rarr;</span></a>
      </div>
      <div class="img-frame reveal">
        <img src="{IMG_WAREHOUSE}" alt="Warehouse storage racks where autonomous robots would transport material">
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      {section_head("HOW WE WORK", "From factory problem to autonomous solution.",
                     "A repeatable engineering process, from understanding the workflow to scaling the solution across facilities.")}
      {process([
        process_step("01", "Understand", "Study the existing workflow and identify automation opportunities."),
        process_step("02", "Design", "Develop the robotic and automation architecture."),
        process_step("03", "Develop", "Build the required hardware, embedded systems, robotics and software."),
        process_step("04", "Integrate", "Connect the robotic system with existing factory infrastructure."),
        process_step("05", "Deploy", "Validate the solution in the real operating environment."),
        process_step("06", "Scale", "Expand the solution across processes, production lines and facilities."),
      ])}
    </div>
  </section>

  <section class="section section--tight" style="background:var(--bg-raised);border-top:1px solid var(--line-soft);border-bottom:1px solid var(--line-soft);">
    <div class="wrap">
      {section_head("WHY IYONEX", "Engineering the next generation of industrial automation.", "")}
      {grid(4, [
        tile("", "End-to-End Engineering", "Hardware, embedded systems, robotics, automation and software under one engineering ecosystem."),
        tile("", "Deployment Focused", "The goal is not simply to demonstrate a robot &mdash; it is to make the system work in real industrial environments."),
        tile("", "Modular Architecture", "Solutions designed to evolve with changing automation requirements."),
        tile("", "Innovation Driven", "Continuous exploration of robotics, autonomous systems and intelligent industrial automation."),
      ])}
    </div>
  </section>

  <section class="vision">
    <div class="aurora"></div>
    <div class="blueprint-bg"></div>
    <div class="wrap" style="position:relative;z-index:1;">
      <div class="eyebrow reveal" style="justify-content:center;">OUR VISION</div>
      <h2 class="reveal">Building the intelligent factory.</h2>
      <p class="reveal">The future of manufacturing isn&rsquo;t simply about adding more machines &mdash; it&rsquo;s about robots, machines, software and people working together intelligently.</p>
      <p class="reveal">Iyonex Automation is working toward a future where material movement is autonomous and industrial automation is accessible at scale.</p>
    </div>
  </section>

  {cta_band("Ready to make your factory smarter?",
            "Let&rsquo;s identify where robotics and intelligent automation can create real operational value.",
            "Talk to Iyonex", "contact.html", "Explore Our Solutions", "solutions.html")}
"""

PAGES.append(("index.html", {
    "title": "Iyonex Automation | Intelligent Robotics & Industrial Automation",
    "desc": "Iyonex Automation develops intelligent robotics, Autonomous Mobile Robots and industrial automation solutions for modern factories.",
    "active": "home",
}, home_body))

# =========================================================== SOLUTIONS ==
solutions_body = f"""
  <section class="hero" style="padding-bottom:40px;">
    <div class="aurora"></div>
    <div class="blueprint-bg"></div>
    <div class="wrap" style="position:relative;z-index:1;max-width:760px;">
      <div class="eyebrow reveal">SOLUTIONS</div>
      <h1 class="h1 grad-text reveal" style="font-size:clamp(2.2rem,4.4vw,3.4rem);">From robot to real-world deployment.</h1>
      <p class="hero-sub reveal">We don&rsquo;t just build robots. We engineer complete robotic automation solutions designed around how factories actually operate.</p>
    </div>
  </section>

  <section class="section" id="amr">
    <div class="wrap">
      {grid(3, [
        tile("01", "Autonomous Mobile Robots", "Intelligent mobile robots for autonomous industrial material transportation, built for dynamic factory floors.", "amr.html"),
        tile("02", "Industrial Automation", "Automation systems connecting machines, sensors, controllers and robotic platforms into one coordinated operation."),
        tile("03", "Robot Intelligence", "Navigation, perception, planning and autonomous decision-making that let a robot operate safely without constant supervision."),
      ])}
    </div>
  </section>

  <section class="section section--tight" id="integration" style="background:var(--bg-raised);border-top:1px solid var(--line-soft);border-bottom:1px solid var(--line-soft);">
    <div class="wrap">
      {grid(2, [
        tile("04", "Factory Integration", "Connecting robotic systems with existing factory workflows, machines and infrastructure &mdash; so automation fits into how a plant already runs, rather than forcing a rebuild around it."),
        tile("05", "Robotics Software", "Control, monitoring, fleet management and system integration software that keeps robotic operations visible and manageable from a single place."),
      ])}
    </div>
    <a name="software"></a>
    <a name="automation"></a>
  </section>

  {cta_band("Have a material movement challenge in mind?",
            "Walk us through your process and we&rsquo;ll help you evaluate where autonomous transportation fits.",
            "Talk to Iyonex", "contact.html", "See the AMR Platform", "amr.html")}
"""

PAGES.append(("solutions.html", {
    "title": "Solutions | Iyonex Automation",
    "desc": "Autonomous mobile robots, industrial automation, factory integration and robotics software from Iyonex Automation.",
    "active": "solutions",
}, solutions_body))

from content_amr import PAGES_AMR
from content_tech import PAGES_TECH
from content_industries import PAGES_IND
from content_learning import PAGES_LEARN
from content_about_contact import PAGES_AC

PAGES.extend(PAGES_AMR)
PAGES.extend(PAGES_TECH)
PAGES.extend(PAGES_IND)
PAGES.extend(PAGES_LEARN)
PAGES.extend(PAGES_AC)
