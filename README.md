# Iyonex Automation — Website

A static, dependency-free website (HTML/CSS/JS). No build tools or frameworks
required to run it — open it or drop it on any static host.

## 1. File structure

```
iyonex/
├── index.html            Home
├── solutions.html        Solutions overview
├── amr.html              Autonomous Mobile Robots (flagship platform, 3D hero)
├── technology.html       Technology stack
├── industries.html       Industries
├── learning.html         Learning hub / Training Programs
├── internships.html      Internships + application form
├── workshops.html        Workshops + request form
├── about.html            About, approach, and team photography
├── contact.html          Contact form + real business details
├── 404.html              Not-found page
├── admin-login.html      Staff login (client-side gate — see §7)
├── admin.html            Admin dashboard for viewing form submissions
├── robots.txt            Keeps admin pages out of search indexes
├── css/style.css         Full design system (tokens, layout, components)
├── js/main.js            Nav, mobile menu, scroll reveal, demo form handling
├── js/hero3d.js          Three.js animated node-network hero (index + amr)
├── js/admin-auth.js      Login form check (demo-grade — see §7)
├── js/admin-auth-guard.js  Redirects to login if not signed in
├── js/admin-dashboard.js   Renders/exports/deletes saved submissions
├── assets/
│   ├── iyonex-logo.png   Your real logo, auto-cropped, used site-wide
│   ├── favicon.png       Brand-blue favicon (transparent background)
│   └── favicon-32.png
├── build.py               Generator script (see §4 — optional, not needed to run the site)
├── content*.py            Page content used by build.py
├── content_business.py    Single source of truth for name/email/phone/address/LinkedIn
└── README.md
```

The navbar and footer both use your actual logo file (`assets/iyonex-logo.png`),
auto-cropped to remove excess white margin so it sits crisply at any size.

## 2. Run it locally

No install needed. Two options:

**Just open it:**
Double-click `index.html`. Every page works with plain `file://` links.

**Or serve it (recommended, matches production):**
```bash
cd iyonex
python3 -m http.server 8080
# visit http://localhost:8080
```

## 3. Deploy it

This is a static site, so any static host works:

- **Netlify / Vercel**: drag the `iyonex` folder into the dashboard, or connect
  a Git repo and set the publish directory to the project root (no build
  command needed).
- **GitHub Pages**: push the folder to a repo and enable Pages on the `main`
  branch / root.
- **Any shared hosting / cPanel**: upload the contents of `iyonex/` to
  `public_html`.

Set the 404 page in your host's settings to `404.html` if it isn't picked up
automatically (Netlify and GitHub Pages do this by convention).

The site currently assumes **iyonex.com** as the live domain (used in the
canonical link, Open Graph tags, and structured data). If that's not the
final domain, update `COMPANY_DOMAIN` in `content_business.py` and re-run
the build.

## 4. Regenerating the site (optional)

The site was assembled from small Python content modules so the navbar,
footer, and business details stay identical and in sync across every page.
You don't need this to use the site — it's only useful if you want to keep
editing content in one place and regenerate the HTML.

```bash
cd iyonex
python3 build.py
```

- **Contact details** (email, phone, address, LinkedIn) live in one place:
  `content_business.py`. Change them there and every page updates.
- **Page copy** lives in `content.py`, `content_amr.py`, `content_tech.py`,
  `content_industries.py`, `content_learning.py`, and
  `content_about_contact.py`.
- If you'd rather hand-edit the generated `.html` files directly, that's
  fine too — the generator is a convenience, not a dependency. Just note
  that re-running `build.py` will overwrite hand-edits.

## 5. What's already wired up

- **Real business details** — address (Lawspet, Puducherry 605008), email,
  phone, and LinkedIn appear in the footer of every page, on the contact
  page, and in the site's structured data (JSON-LD) for search engines.
- **Real logo** — used in the navbar and footer, plus as the favicon mark
  and Open Graph share image.
- **Photography** — free-to-use, no-attribution stock photos illustrate
  industry context (factory floors, warehouses, robot arms, workshops)
  across the homepage, About, Industries, Technology, and Learning pages.
  None are presented as actual Iyonex products, customers, or facilities —
  see the disclosure note on the Industries page.
- **3D hero** — an animated, cursor-reactive node-network scene (Three.js)
  on the Home and AMR pages, with a graceful static fallback if WebGL is
  unavailable.

## 7. Admin panel — read this before you rely on it

A small "Staff Login" link in the footer leads to `admin-login.html`, which
gates `admin.html` — a dashboard that lists whatever the Contact, Internship,
and Workshop forms have saved.

**Default login:** username `admin`, password `Iyonex#2026` — set in
`js/admin-auth.js`. Change this before publishing the site.

**Two important limits, because this is a static site with no server:**

1. **It's not real security.** The password check runs in the visitor's own
   browser, in a JS file anyone can open and read. This only stops casual
   browsing — it will not stop someone who actually wants in. Don't put
   anything genuinely sensitive behind it as-is.
2. **It's not a real inbox.** When someone submits a form, the data is saved
   to *that visitor's own browser* (`localStorage`) — it is never sent
   anywhere, including to you. So the admin panel will only ever show
   submissions made from the same browser you're viewing it in (handy for
   testing the forms yourself; not useful for collecting real inquiries from
   your actual website visitors).

**To make this genuinely functional**, the forms need a real backend. Any of
these would work well with this site as-is:

- **Formspree** or **Netlify Forms** — point the form's `action` at their
  endpoint; both give you a real inbox with almost no setup, no separate
  admin panel needed.
- **Netlify Identity + a small serverless function** — real login, and a
  function that writes submissions to a database (or emails them to you).
- **A custom backend** (Node/Python/etc.) with a real database and a proper
  session-based login — the most work, but gives you full control and the
  admin dashboard here could be pointed at its API with light changes.

Happy to help wire up whichever direction you'd like.

## 8. Information still useful to add

- **Founder name, title, and biography** — `about.html` currently has an
  honest, un-clunky placeholder note instead of a fake bio card. Replace it
  with real founder details whenever you're ready.
- **Dedicated Open Graph image** — link previews currently use the logo;
  a dedicated 1200×630 share image would look better on social platforms.
- **Confirm which internship domains and workshop topics are currently
  active** vs. "coming soon" — `internships.html` and `workshops.html`
  reflect a reasonable default split; adjust the `soon=True` tiles in
  `content_learning.py` as your programs firm up.
- **A live form backend** — see §7 above. Until one's wired up, the real
  email/phone shown on the contact page remain the reliable way for people
  to actually reach you.
