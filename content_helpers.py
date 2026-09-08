# Reusable HTML fragment builders for the Iyonex site generator.

def section_head(eyebrow, h2, lede, center=False):
    cls = "section-head center" if center else "section-head"
    return f"""
    <div class="{cls} reveal">
      <div class="eyebrow">{eyebrow}</div>
      <h2 class="h2">{h2}</h2>
      <p class="lede" style="{'margin:16px auto 0' if center else 'margin-top:16px'}">{lede}</p>
    </div>"""


def tile(index, title, desc, link=None, link_text=None, soon=False, photo=None, photo_alt=None):
    soon_tag = '<span class="tag-soon">Coming soon</span>' if soon else ""
    idx = f'<span class="tile-index">{index}</span>' if index and not soon else (f'<span class="tile-index">{index}</span>' if index else "")
    link_html = ""
    if link:
        link_html = f'<a class="tile-link" href="{link}">{link_text or "Learn more"} <span aria-hidden="true">&rarr;</span></a>'
    photo_html = ""
    if photo:
        alt = photo_alt or title
        photo_html = f'<div class="tile-photo"><img src="{photo}" alt="{alt}" loading="lazy"></div>'
    cls = "tile is-soon" if soon else "tile"
    return f"""
      <div class="{cls} reveal">
        {photo_html}
        {soon_tag}
        {idx}
        <h3>{title}</h3>
        <p>{desc}</p>
        {link_html}
      </div>"""


def grid(cols, tiles_html):
    return f'<div class="grid-{cols}">{"".join(tiles_html)}</div>'


def process_step(num, title, desc):
    return f"""
      <div class="process-step reveal">
        <div class="process-num">{num}</div>
        <div>
          <h3>{title}</h3>
          <p>{desc}</p>
        </div>
      </div>"""


def process(steps_html):
    return f'<div class="process"><div class="process-line"></div>{"".join(steps_html)}</div>'


def cta_band(h2, lede, primary_text, primary_href, secondary_text=None, secondary_href=None):
    sec = f'<a href="{secondary_href}" class="btn btn-ghost">{secondary_text}</a>' if secondary_text else ""
    return f"""
  <section class="cta-band">
    <div class="blueprint-bg"></div>
    <div class="wrap" style="position:relative;z-index:1;">
      <h2 class="h2 reveal">{h2}</h2>
      <p class="lede reveal">{lede}</p>
      <div class="btn-row reveal">
        <a href="{primary_href}" class="btn btn-primary">{primary_text} <span class="arrow" aria-hidden="true">&rarr;</span></a>
        {sec}
      </div>
    </div>
  </section>"""


def stack_row(name, code, items):
    chips = "".join(f'<span class="chip">{i}</span>' for i in items)
    return f"""
      <div class="stack-row reveal">
        <div class="stack-name">{name}<span>{code}</span></div>
        <div class="stack-items">{chips}</div>
      </div>"""


# ---------------------------------------------------------------- HERO ---

def hero_svg(label="AMR\u201301"):
    """Top-down schematic: AMR navigating a factory floor between rack zones."""
    return f"""
    <div class="corner-mark tl"></div><div class="corner-mark tr"></div>
    <div class="corner-mark bl"></div><div class="corner-mark br"></div>
    <div class="hero-readout r1"><span class="dot"></span>NAV: ACTIVE</div>
    <div class="hero-readout r2"><span class="dot sv-blink"></span>PATH: OPTIMIZING</div>
    <svg viewBox="0 0 480 420" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Schematic top-down diagram of an autonomous mobile robot navigating between storage racks on a factory floor">
      <!-- rack zones -->
      <rect x="34" y="34" width="86" height="196" class="sv-line" stroke-width="1"></rect>
      <rect x="360" y="196" width="86" height="196" class="sv-line" stroke-width="1"></rect>
      <text x="40" y="26" class="sv-text" style="font-family:'IBM Plex Mono',monospace;font-size:9px;letter-spacing:1px;">RACK ZONE A</text>
      <text x="366" y="404" class="sv-text" style="font-family:'IBM Plex Mono',monospace;font-size:9px;letter-spacing:1px;">RACK ZONE B</text>

      <!-- travelled path -->
      <polyline points="70,392 150,350 208,282 230,206" fill="none" class="sv-blue sv-path" stroke-width="1.5"></polyline>
      <circle cx="70" cy="392" r="4" class="sv-blue-fill"></circle>
      <circle cx="150" cy="350" r="3.5" class="sv-blue-fill" opacity="0.6"></circle>
      <circle cx="208" cy="282" r="3.5" class="sv-blue-fill" opacity="0.6"></circle>

      <!-- planned path ahead -->
      <polyline points="240,150 300,92" fill="none" class="sv-dim sv-path" stroke-width="1" stroke-dasharray="3 5"></polyline>
      <circle cx="300" cy="92" r="9" class="sv-blue" stroke-width="1.3" fill="none"></circle>
      <circle cx="300" cy="92" r="3" class="sv-blue-fill sv-blink"></circle>
      <text x="312" y="88" class="sv-text" style="font-family:'IBM Plex Mono',monospace;font-size:9px;letter-spacing:0.5px;">TARGET</text>

      <!-- sensor field of view -->
      <path d="M240,150 L205,90 A70,70 0 0 1 275,90 Z" class="sv-blue" fill="var(--blue)" fill-opacity="0.06" stroke-width="0.75" opacity="0.8"></path>

      <!-- radar sweep -->
      <g class="sv-scan" style="transform-origin:240px 150px;">
        <line x1="240" y1="150" x2="240" y2="96" class="sv-blue" stroke-width="1"></line>
      </g>

      <!-- robot chassis -->
      <g transform="translate(240,150)">
        <rect x="-22" y="-22" width="44" height="44" rx="6" fill="var(--surface-2)" class="sv-blue" stroke-width="1.4"></rect>
        <path d="M-8,-22 L0,-32 L8,-22 Z" class="sv-blue-fill"></path>
        <circle cx="0" cy="0" r="7" class="sv-blue" stroke-width="1.2" fill="none"></circle>
        <circle cx="0" cy="0" r="2.4" class="sv-blue-fill"></circle>
      </g>
      <text x="256" y="176" class="sv-text" style="font-family:'IBM Plex Mono',monospace;font-size:10px;letter-spacing:0.5px;">{label}</text>
    </svg>
    """


def hero_3d(tag1="NETWORK: SYNCED", tag2="FLEET: 46 NODES"):
    """Cinematic 3D node-network hero, rendered client-side by hero3d.js.
    Degrades gracefully (readouts + corner marks only) if JS/WebGL is unavailable."""
    return f"""
    <div class="corner-mark tl"></div><div class="corner-mark tr"></div>
    <div class="corner-mark bl"></div><div class="corner-mark br"></div>
    <div class="hero-readout r1"><span class="dot"></span>{tag1}</div>
    <div class="hero-readout r2"><span class="dot sv-blink"></span>{tag2}</div>
    <div data-hero3d style="position:absolute;inset:0;"></div>
    """
