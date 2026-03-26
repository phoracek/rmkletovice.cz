# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Static website for Raketomodelářský klub Letovice (RMK Letovice), a Czech rocket modeling club. Built with [Pelican](https://getpelican.com/), a Python static site generator. Content is written in reStructuredText (`.rst`). The site language is Czech.

## Build & Preview

```bash
# Install dependency (once)
pip3 install pelican

# Build and serve locally (development)
python3 -m pelican -t theme -s pelicanconf.py && cd output && python3 -m http.server && cd ..

# Build for production
python3 -m pelican -t theme -s publishconf.py
```

`pelicanconf.py` is for development (relative URLs), `publishconf.py` is for production (absolute URLs, feeds enabled, deletes output dir before build).

## Content Structure

All content lives in `content/` as `.rst` files. Two article categories:

- `content/letove-akce/` — Flying event reports and announcements (`Letové akce` category)
- `content/ostatni/` — Club news, greetings, announcements (`Ostatní` category)
- `content/pages/` — Static pages (club history, etc.)
- `content/docs/` — Static file attachments (PDFs, images referenced by articles)

**File naming:** `YYYYMMDD-slug.rst` — the date is extracted from the filename via regex in `pelicanconf.py`, not from metadata.

**URL pattern:** `/clanky/{category}/{slug}.html`

## Article Metadata

Standard `.rst` article header:

```rst
Název článku
############

:category: Letové akce

Obsah článku...
```

For flying events, the `:action:` metadata field holds a Python dict parsed by a custom Jinja2 filter:

```rst
:action: {
  'date': '5. 9. 2015',
  'place': 'Letiště Letovice',
  'map': 'http://mapy.cz/...',
  'documents': [{'name': 'Propozice', 'filename': 'propozice.pdf', 'formats': ['pdf']}],
  'gallery': 'https://www.zonerama.com/...'
}
```

This metadata is rendered by `theme/templates/include/action-detail.html`.

## Theme

Custom Pelican theme in `theme/`:

- `theme/templates/` — Jinja2 templates; `base.html` is the master layout
- `theme/static/css/style.css` — Custom CSS (Bootstrap 3 + responsive overrides)
- `theme/static/images/top_*.jpg` — Responsive hero images (8 sizes, 800px–2560px)

The theme uses Bootstrap 3. Navigation, footer contacts, and archive year links are configured directly in `pelicanconf.py` (not in templates).

## Tools

`tools/odt2pdf.sh` — converts ODT files to PDF using LibreOffice. Output PDFs are placed alongside the source files. Requires `libreoffice` on `$PATH`.

```bash
tools/odt2pdf.sh content/docs/file.odt
tools/odt2pdf.sh content/docs/*.odt
```

When an event has ODT documents (e.g. propozice), run this script to produce the PDF before adding the article that references it.

`tools/odt2text.py` — extracts plain text from an ODT file. Useful for reading event dates or other details without opening LibreOffice.

```bash
tools/odt2text.py content/docs/file.odt
```

## Git

Always sign commits with `git commit -s` (adds a `Signed-off-by` trailer).

## Scope of Work

Claude Code is used **only to create new content** — never to adjust themes or page configuration. New articles should follow the existing `.rst` format and naming conventions above.
