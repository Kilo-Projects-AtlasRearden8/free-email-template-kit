# Status — Free Email Template Kit

## What was built
A freebies kit of fillable email templates in Markdown and printable HTML:

- `templates/thank-you-note.md` + `html/thank-you-note.html` — thank-you notes
- `templates/inquiry-letter.md` + `html/inquiry-letter.html` — inquiry letters
- `templates/follow-up.md` + `html/follow-up.html` — follow-ups
- `templates/polite-decline.md` + `html/polite-decline.html` — polite declines
- `html/index.html` — kit landing page linking every template
- `LICENSE` — MIT License, `Copyright (c) 2026 Asdale Dynamics, LLC`
- `README.md` — credits Asdale Dynamics, LLC, usage instructions

Every template uses bracketed placeholders (`[Recipient Name]`, `[Your Name]`, etc.).
HTML pages are styled for clean printing (`@media print`, US Letter, screen chrome
hidden when printed). No account, no tracking, no personal data, no build step,
local-first. Credit: Asdale Dynamics, LLC (Indiana), founded by Dylan Asdale.

## How to run it
- Markdown: open any `templates/*.md` in a text editor, replace the bracketed
  fields, delete the brackets, copy into your email client.
- HTML: open any `html/*.html` in a browser, fill in the fields, then print
  (Ctrl+P / Cmd+P) or save to PDF. Open `html/index.html` for the kit overview.
- Nothing to install, no server, nothing to buy.

## Verification results
- All 11 expected files present
- All 5 HTML files parse with balanced tags (Python `html.parser` check)
- All 4 template pages include `@media print` styles and Asdale Dynamics, LLC credit
- `LICENSE` contains the exact line `Copyright (c) 2026 Asdale Dynamics, LLC`
- `README.md` contains the Asdale Dynamics, LLC credit
- No `.github/workflows` directory; no secrets, API keys, or personal data found
- Git commit `4a8a75e` on `master`, working tree clean (before STATUS.md)

## Known gaps
- No automated test suite beyond the one-off verification script (static HTML/
  Markdown, no build step)
- Printed output not visually QA'd in an actual browser/PDF (no headless browser
  available in this environment)
- `@page` is US Letter only; no A4 variant
- Placeholder fields are not interactive form fields (filled manually)
