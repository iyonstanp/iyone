#!/usr/bin/env python3
"""Assembles the Iyonex Automation static site from shared partials.
Run: python3 build.py
"""
import os

OUT = os.path.dirname(os.path.abspath(__file__))

from content_business import (
    COMPANY_NAME, COMPANY_EMAIL, COMPANY_PHONE, COMPANY_ADDRESS_FULL,
    COMPANY_LINKEDIN, COMPANY_DOMAIN,
)

# ---------------------------------------------------------------- NAV ----
def nav(active=""):
    def cls(name):
        return " active" if name == active else ""

    return f"""
  <a href="#main" class="skip-link">Skip to content</a>
  <nav class="nav">
    <div class="nav-inner">
      <a href="index.html" class="logo" aria-label="Iyonex Automation — home">
        <img src="assets/iyonex-logo.png" alt="Iyonex" class="logo-img">
        <span class="logo-sub">AUTOMATION</span>
      </a>

      <ul class="nav-links">
        <li class="{cls('home').strip() or ''}"><a href="index.html">Home</a></li>
        <li class="{cls('solutions')}"><a href="solutions.html">Solutions</a></li>
        <li class="{cls('technology')}"><a href="technology.html">Technology</a></li>
        <li class="{cls('industries')}"><a href="industries.html">Industries</a></li>
        <li class="{cls('learning')}">
          <a href="learning.html" style="display:flex;align-items:center;gap:6px;">Learning
            <svg class="nav-caret" viewBox="0 0 10 6" fill="none"><path d="M1 1l4 4 4-4" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>
          </a>
          <div class="mega">
            <div class="mega-panel">
            <div class="mega-grid">
              <a href="internships.html">
                <div class="mega-title">Internships</div>
                <div class="mega-desc">Hands-on engineering exposure for students.</div>
              </a>
              <a href="workshops.html">
                <div class="mega-title">Workshops</div>
                <div class="mega-desc">Technical sessions on robotics &amp; automation.</div>
              </a>
              <a href="learning.html">
                <div class="mega-title">Training Programs</div>
                <div class="mega-desc">Structured, project-based learning tracks.</div>
              </a>
            </div>
            </div>
          </div>
        </li>
        <li class="{cls('about')}"><a href="about.html">About</a></li>
        <li class="{cls('contact')}"><a href="contact.html">Contact</a></li>
      </ul>

      <div class="nav-actions">
        <a href="contact.html" class="btn btn-ghost">Talk to Iyonex</a>
        <button class="hamburger" aria-label="Open menu" aria-expanded="false">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
  </nav>

  <div class="mobile-menu">
    <a href="index.html">Home</a>
    <a href="solutions.html">Solutions</a>
    <a href="technology.html">Technology</a>
    <a href="industries.html">Industries</a>
    <button class="m-toggle" data-target="m-learning">Learning
      <svg class="nav-caret" viewBox="0 0 10 6" fill="none"><path d="M1 1l4 4 4-4" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/></svg>
    </button>
    <div class="mobile-sub" id="m-learning">
      <a href="internships.html">Internships</a>
      <a href="workshops.html">Workshops</a>
      <a href="learning.html">Training Programs</a>
    </div>
    <a href="about.html">About</a>
    <a href="contact.html">Contact</a>
    <a href="contact.html" class="btn btn-primary">Talk to Iyonex</a>
  </div>
"""


# --------------------------------------------------------------- FOOTER --
FOOTER = f"""
  <footer class="footer">
    <div class="wrap">
      <div class="footer-top">
        <div class="footer-brand">
          <a href="index.html" class="logo" aria-label="Iyonex Automation — home">
            <img src="assets/iyonex-logo.png" alt="Iyonex" class="logo-img logo-img--lg">
          </a>
          <p>Intelligent robotics. Smarter factories.<br>Autonomous mobile robots and industrial automation, engineered for real-world factory deployment.</p>
        </div>
        <div>
          <h4>Solutions</h4>
          <ul>
            <li><a href="amr.html">Autonomous Mobile Robots</a></li>
            <li><a href="solutions.html#automation">Industrial Automation</a></li>
            <li><a href="solutions.html#integration">Factory Integration</a></li>
            <li><a href="solutions.html#software">Robotics Software</a></li>
          </ul>
        </div>
        <div>
          <h4>Company</h4>
          <ul>
            <li><a href="about.html">About</a></li>
            <li><a href="technology.html">Technology</a></li>
            <li><a href="industries.html">Industries</a></li>
            <li><a href="contact.html">Contact</a></li>
          </ul>
        </div>
        <div>
          <h4>Learning</h4>
          <ul>
            <li><a href="internships.html">Internships</a></li>
            <li><a href="workshops.html">Workshops</a></li>
            <li><a href="learning.html">Training Programs</a></li>
          </ul>
          <h4 style="margin-top:26px;">Connect</h4>
          <ul>
            <li><a href="{COMPANY_LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a></li>
            <li><a href="mailto:{COMPANY_EMAIL}">{COMPANY_EMAIL}</a></li>
            <li><a href="tel:{COMPANY_PHONE.replace(' ', '')}">{COMPANY_PHONE}</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <span>&copy; 2026 {COMPANY_NAME}. All rights reserved.</span>
        <span>{COMPANY_ADDRESS_FULL} &nbsp;&middot;&nbsp; <a href="mailto:{COMPANY_EMAIL}" style="color:var(--text-dim)">{COMPANY_EMAIL}</a> &nbsp;&middot;&nbsp; <a href="admin-login.html" rel="nofollow" style="color:var(--text-faint);font-size:0.78rem;">Staff Login</a></span>
      </div>
    </div>
  </footer>
"""

# --------------------------------------------------------------- HEAD ----
def head(title, desc, og_title=None, extra=""):
    og_title = og_title or title
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{COMPANY_DOMAIN}" />
<meta property="og:type" content="website">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="assets/iyonex-logo.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="assets/favicon.png">
<link rel="stylesheet" href="css/style.css">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "{COMPANY_NAME}",
  "url": "{COMPANY_DOMAIN}",
  "logo": "{COMPANY_DOMAIN}assets/iyonex-logo.png",
  "email": "{COMPANY_EMAIL}",
  "telephone": "{COMPANY_PHONE}",
  "address": {{
    "@type": "PostalAddress",
    "streetAddress": "Lawspet",
    "addressLocality": "Puducherry",
    "postalCode": "605008",
    "addressCountry": "IN"
  }},
  "sameAs": ["{COMPANY_LINKEDIN}"]
}}
</script>
{extra}
</head>
"""

def page(filename, title, desc, active, body, og_title=None, use_3d=False):
    extra_head = ""
    extra_body_scripts = ""
    if use_3d:
        extra_body_scripts = '\n<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>\n<script src="js/hero3d.js"></script>'
    html = (head(title, desc, og_title, extra_head) + "<body>\n" + nav(active) + '\n<main id="main">\n' + body
            + "\n</main>\n" + FOOTER + '\n<script src="js/main.js"></script>' + extra_body_scripts + '\n</body>\n</html>\n')
    with open(os.path.join(OUT, filename), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", filename)


# import page content builders
from content import PAGES  # noqa

THREE_D_PAGES = {"index.html", "amr.html"}

for fname, meta, body in PAGES:
    page(fname, meta["title"], meta["desc"], meta["active"], body, meta.get("og_title"), use_3d=(fname in THREE_D_PAGES))

print("Done.")
