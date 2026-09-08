from content_helpers import section_head, tile, grid, process_step, process, cta_band
from content_images import IMG_WORKSHOP_STUDENT, IMG_TEAM_ENGINEERING

PAGES_LEARN = []

# --------------------------------------------------------- LEARNING HUB -
learning_body = f"""
  <section class="hero" style="padding-bottom:20px;">
    <div class="aurora"></div>
    <div class="blueprint-bg"></div>
    <div class="wrap" style="position:relative;z-index:1;max-width:760px;">
      <div class="eyebrow reveal">LEARNING</div>
      <h1 class="h1 grad-text reveal" style="font-size:clamp(2.2rem,4.4vw,3.4rem);">Learn. Build. Innovate.</h1>
      <p class="hero-sub reveal">Practical exposure to robotics, automation and emerging industrial technologies &mdash; designed to help students and young engineers move from theory to real-world engineering.</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      {grid(3, [
        tile("", "Internships", "Gain hands-on exposure to robotics, embedded systems, automation and autonomous systems through practical engineering projects.", "internships.html", "Explore Internships"),
        tile("", "Workshops", "Participate in focused technical workshops covering robotics, automation, embedded systems and emerging technologies.", "workshops.html", "Explore Workshops"),
        tile("", "Training Programs", "Structured learning programs designed to develop practical engineering skills through projects, demonstrations and technical sessions.", "#programs", "See Programs Below"),
      ])}
    </div>
  </section>

  <section class="section section--tight" id="programs" style="background:var(--bg-raised);border-top:1px solid var(--line-soft);border-bottom:1px solid var(--line-soft);">
    <div class="wrap">
      {section_head("TRAINING PROGRAMS", "Structured, project-based learning tracks.",
                     "Rather than lecture-only sessions, Iyonex training is organized around actually building and configuring working systems.")}
      {grid(3, [
        tile("", "Concept Sessions", "Focused technical sessions that build the engineering fundamentals behind each topic."),
        tile("", "Guided Projects", "Structured project work that applies concepts to a real, hands-on engineering task."),
        tile("", "Technical Demonstrations", "Live walkthroughs of robotics and automation systems operating in practice."),
      ])}
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      {section_head("LEARNING PARTNERSHIPS", "Partner with us in building the next generation of engineers.",
                     "We collaborate with educational institutions and organizations to create practical learning experiences around robotics, automation and emerging technologies.")}
      <div class="grid-2 reveal">
        <div>
          <h3 style="margin-bottom:14px;">Partnership types</h3>
          <ul style="display:flex;flex-direction:column;gap:10px;">
            {"".join(f'<li style="font-size:0.94rem;color:var(--text-dim);display:flex;gap:10px;"><span style="color:var(--blue);font-family:var(--font-mono);font-size:0.75rem;">&#9654;</span>{p}</li>' for p in [
              "Technical workshops","Robotics demonstrations","Internship programs","Industry interaction",
              "Project mentoring","Technical training","Campus innovation programs"])}
          </ul>
        </div>
        <div class="note-box">
          <strong>A note on partnerships.</strong> Iyonex does not list specific institutional partnerships on this page unless they are officially confirmed. If your institution is interested in collaborating, reach out through the contact page.
        </div>
      </div>
    </div>
  </section>

  {cta_band("Bring practical robotics learning to your campus.",
            "Iyonex Automation can collaborate with colleges, universities and technical institutions to conduct focused workshops and training programs.",
            "Request a Workshop", "workshops.html#request", "Partner With Iyonex", "contact.html")}
"""

PAGES_LEARN.append(("learning.html", {
    "title": "Learning: Internships, Workshops & Training | Iyonex Automation",
    "desc": "Iyonex Automation's learning programs give students and young engineers practical, project-based exposure to robotics and industrial automation.",
    "active": "learning",
}, learning_body))

# ------------------------------------------------------------ INTERNSHIP
internship_body = f"""
  <section class="hero" style="padding-bottom:20px;">
    <div class="aurora"></div>
    <div class="blueprint-bg"></div>
    <div class="wrap hero-inner" style="position:relative;z-index:1;">
      <div>
        <div class="eyebrow reveal">INTERNSHIPS</div>
        <h1 class="h1 grad-text reveal" style="font-size:clamp(2.2rem,4.4vw,3.2rem);">Build. Learn. Experience real engineering.</h1>
        <p class="hero-sub reveal">Iyonex Automation offers practical learning opportunities for students and aspiring engineers interested in robotics, automation and intelligent systems.</p>
        <div class="btn-row reveal">
          <a href="#apply" class="btn btn-primary">Apply for Internship <span class="arrow" aria-hidden="true">&rarr;</span></a>
          <a href="#domains" class="btn btn-ghost">View Openings</a>
        </div>
      </div>
      <div class="reveal" style="border:1px solid var(--line);overflow:hidden;box-shadow:0 24px 60px -24px rgba(46,60,90,0.18);aspect-ratio:4/3.4;">
        <img src="{IMG_WORKSHOP_STUDENT}" alt="Student operating machinery in an engineering workshop" style="width:100%;height:100%;object-fit:cover;display:block;">
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      {section_head("WHY INTERN WITH IYONEX", "Learning grounded in real engineering work.", "")}
      {grid(4, [
        tile("", "Hands-On Engineering", "Work on practical engineering problems rather than learning only through theory."),
        tile("", "Robotics Exposure", "Understand robotics systems, mobile robots, sensors, controllers and autonomous technologies."),
        tile("", "Industry-Oriented Learning", "Learn how engineering concepts are applied to real-world industrial challenges."),
        tile("", "Project-Based Experience", "Develop practical understanding through projects, experiments and technical tasks."),
      ])}
    </div>
  </section>

  <section class="section section--tight" id="domains" style="background:var(--bg-raised);border-top:1px solid var(--line-soft);border-bottom:1px solid var(--line-soft);">
    <div class="wrap">
      {section_head("INTERNSHIP DOMAINS", "Where you can contribute.", "Only domains that are currently active are open for application; others are marked coming soon.")}
      {grid(3, [
        tile("", "Robotics", "Robot architecture, mechanisms, sensors and robotic systems."),
        tile("", "Autonomous Mobile Robots", "Navigation, localization, obstacle avoidance and autonomous movement."),
        tile("", "Embedded Systems", "Microcontrollers, sensors, communication, motor control and embedded programming."),
        tile("", "Industrial Automation", "PLC, HMI, industrial communication and automation systems.", None, None, True),
        tile("", "Robotics Software", "Robot control, monitoring, simulation and software integration."),
        tile("", "AI &amp; Autonomous Systems", "Computer vision, perception, planning and intelligent decision-making.", None, None, True),
      ])}
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      {section_head("INTERNSHIP PROCESS", "From application to completion.", "")}
      {process([
        process_step("01", "Apply", "Submit your internship application."),
        process_step("02", "Screening", "Application and technical background are reviewed."),
        process_step("03", "Selection", "Selected candidates receive further communication."),
        process_step("04", "Learn", "Get introduced to the relevant technology and engineering environment."),
        process_step("05", "Build", "Work on practical assignments or projects."),
        process_step("06", "Complete", "Complete the internship and receive relevant documentation or a certificate, where applicable."),
      ])}
      <div class="note-box reveal" style="margin-top:36px;">
        <strong>Internship policy.</strong> Internship opportunities, eligibility, duration, selection process and available domains may vary by program. Please refer to the specific opportunity or contact Iyonex Automation for current details. Iyonex does not guarantee placement, employment, stipend or project publication as part of an internship.
      </div>
    </div>
  </section>

  <section class="section section--tight" id="apply" style="background:var(--bg-raised);border-top:1px solid var(--line-soft);border-bottom:1px solid var(--line-soft);">
    <div class="wrap" style="max-width:760px;">
      {section_head("APPLY", "Ready to build your engineering skills?",
                     "Explore practical opportunities in robotics, automation and emerging industrial technologies.")}
      <form class="reveal" data-demo-form data-store-key="internship">
        <div class="form-grid">
          <div class="field"><label for="i-name">Full Name</label><input id="i-name" name="name" type="text" required></div>
          <div class="field"><label for="i-email">Email</label><input id="i-email" name="email" type="email" required></div>
          <div class="field"><label for="i-phone">Phone</label><input id="i-phone" name="phone" type="tel"></div>
          <div class="field"><label for="i-college">College / University</label><input id="i-college" name="college" type="text"></div>
          <div class="field"><label for="i-degree">Degree / Program</label><input id="i-degree" name="degree" type="text"></div>
          <div class="field"><label for="i-year">Year of Study</label><input id="i-year" name="year" type="text"></div>
          <div class="field full">
            <label for="i-interest">Area of Interest</label>
            <select id="i-interest" name="interest">
              <option>Robotics</option>
              <option>AMR / Autonomous Systems</option>
              <option>Embedded Systems</option>
              <option>Industrial Automation</option>
              <option>Robotics Software</option>
              <option>AI / Computer Vision</option>
              <option>Other</option>
            </select>
          </div>
          <div class="field full">
            <label for="i-resume">Resume Upload</label>
            <div class="field-file">Drag and drop, or click to attach your resume (PDF) &mdash; placeholder, not yet connected</div>
          </div>
          <div class="field full"><label for="i-portfolio">Portfolio / LinkedIn</label><input id="i-portfolio" name="portfolio" type="url"></div>
          <div class="field full"><label for="i-why">Why do you want to intern with Iyonex?</label><textarea id="i-why" name="why"></textarea></div>
        </div>
        <button type="submit" class="btn btn-primary" style="margin-top:26px;">Submit Application</button>
        <p class="form-status" style="display:none;margin-top:16px;color:var(--text-dim);font-size:0.9rem;"></p>
      </form>
    </div>
  </section>
"""

PAGES_LEARN.append(("internships.html", {
    "title": "Internships | Iyonex Automation",
    "desc": "Hands-on robotics and industrial automation internships for students and aspiring engineers at Iyonex Automation.",
    "active": "learning",
}, internship_body))

# -------------------------------------------------------------- WORKSHOPS
workshop_body = f"""
  <section class="hero" style="padding-bottom:20px;">
    <div class="aurora"></div>
    <div class="blueprint-bg"></div>
    <div class="wrap hero-inner" style="position:relative;z-index:1;">
      <div>
        <div class="eyebrow reveal">WORKSHOPS</div>
        <h1 class="h1 grad-text reveal" style="font-size:clamp(2.2rem,4.4vw,3.2rem);">Learn robotics. Build something real.</h1>
        <p class="hero-sub reveal">Industry-oriented workshops designed to introduce students and professionals to practical robotics, automation and autonomous systems.</p>
      </div>
      <div class="reveal" style="border:1px solid var(--line);overflow:hidden;box-shadow:0 24px 60px -24px rgba(46,60,90,0.18);aspect-ratio:4/3.4;">
        <img src="{IMG_TEAM_ENGINEERING}" alt="Engineers collaborating during a technical session" style="width:100%;height:100%;object-fit:cover;display:block;">
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      {section_head("WORKSHOP CATEGORIES", "Only workshops we actually plan to conduct.", "")}
      {grid(3, [
        tile("", "Robotics Fundamentals", "Introduction to robotic systems, components, sensors and control."),
        tile("", "Autonomous Mobile Robots", "Understand how AMRs navigate, perceive and move through dynamic environments."),
        tile("", "Embedded Systems", "Hands-on learning with microcontrollers, sensors, actuators and communication."),
        tile("", "Industrial Automation", "Introduction to PLCs, sensors, actuators, HMI and industrial control."),
        tile("", "ROS / Robotics Software", "Introduction to robotics software frameworks, simulation and robot control.", None, None, True),
        tile("", "AI &amp; Computer Vision", "Explore perception, object detection and intelligent robotic applications.", None, None, True),
      ])}
    </div>
  </section>

  <section class="section section--tight" style="background:var(--bg-raised);border-top:1px solid var(--line-soft);border-bottom:1px solid var(--line-soft);">
    <div class="wrap">
      {section_head("WORKSHOP FORMAT", "Designed around practical learning.", "")}
      {grid(4, [
        tile("", "Technical Concepts", "Understand the engineering fundamentals."),
        tile("", "Live Demonstrations", "See robotics and automation systems operating in practice."),
        tile("", "Hands-On Activities", "Apply concepts through practical exercises."),
        tile("", "Industry Perspective", "Understand how these technologies are applied beyond academic environments."),
      ])}
    </div>
  </section>

  <section class="section section--tight" id="request" style="background:var(--bg-raised);border-top:1px solid var(--line-soft);border-bottom:1px solid var(--line-soft);">
    <div class="wrap" style="max-width:780px;">
      {section_head("REQUEST A WORKSHOP", "Bring robotics to your campus.",
                     "Iyonex Automation can collaborate with colleges, universities, technical institutions and organizations to conduct focused workshops and technical learning programs.")}
      <form class="reveal" data-demo-form data-store-key="workshop">
        <div class="form-grid">
          <div class="field"><label for="w-name">Name</label><input id="w-name" name="name" type="text" required></div>
          <div class="field"><label for="w-org">Organization / College</label><input id="w-org" name="org" type="text" required></div>
          <div class="field"><label for="w-role">Designation</label><input id="w-role" name="role" type="text"></div>
          <div class="field"><label for="w-email">Email</label><input id="w-email" name="email" type="email" required></div>
          <div class="field"><label for="w-phone">Phone</label><input id="w-phone" name="phone" type="tel"></div>
          <div class="field"><label for="w-topic">Workshop Topic</label><input id="w-topic" name="topic" type="text"></div>
          <div class="field"><label for="w-count">Expected Participants</label><input id="w-count" name="count" type="number" min="1"></div>
          <div class="field"><label for="w-date">Preferred Date</label><input id="w-date" name="date" type="date"></div>
          <div class="field full"><label for="w-location">Location / Online</label><input id="w-location" name="location" type="text"></div>
          <div class="field full"><label for="w-message">Message</label><textarea id="w-message" name="message"></textarea></div>
        </div>
        <button type="submit" class="btn btn-primary" style="margin-top:26px;">Request Workshop</button>
        <p class="form-status" style="display:none;margin-top:16px;color:var(--text-dim);font-size:0.9rem;"></p>
      </form>
    </div>
  </section>

  {cta_band("Want to partner on a learning program instead?",
            "We collaborate with institutions on internships, demonstrations, mentoring and training beyond single workshops.",
            "Partner With Iyonex", "contact.html", "See Internships", "internships.html")}
"""

PAGES_LEARN.append(("workshops.html", {
    "title": "Workshops | Iyonex Automation",
    "desc": "Industry-oriented robotics, automation and embedded systems workshops from Iyonex Automation, for campuses and organizations.",
    "active": "learning",
}, workshop_body))
