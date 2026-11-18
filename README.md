# Neurospace Coaching website

Static site for neurospacecoaching.com. No build step on Cloudflare, no cookies, no tracking. Fonts are self-hosted (no Google Fonts, for GDPR).

## Structure
- `site/` — the published website (the only folder Cloudflare serves, set in `wrangler.toml`)
  - `assets/styles.css` — colours, fonts, layout (palette under `:root`, latest palette block at the bottom)
  - `assets/fonts/` — Titan One (headings), Atkinson Hyperlegible (body)
  - `assets/img/` — photos and ghost logo
- `tools/build.py` — generates the HTML pages in `site/` from one place (shared header/footer, hours, email, booking link). Edit it, then run `python3 tools/build.py`.

## Cloudflare
Deployed as a Cloudflare Worker (static assets) named `neurospace-web`, connected to this repo.
Every push to `main` redeploys automatically. Config lives in `wrangler.toml`.
- Preview: https://neurospace-web.elliothelt34.workers.dev
- Build command: (empty) · Deploy command: `npx wrangler deploy` · Root directory: `/`

## Before launch
- Add the street address (`ADDRESS` in `tools/build.py`) — used in the Impressum and privacy policy
- Paste the Formspree form ID (`FORM_ENDPOINT` in `tools/build.py`)
- Set the "Last updated" date in the privacy policy
