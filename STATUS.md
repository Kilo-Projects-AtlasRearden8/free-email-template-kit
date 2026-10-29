# Status — Free Email Template Kit

## What was built
A freebies kit of fillable email templates in Markdown and printable HTML:

- `templates/thank-you-note.md` + `html/thank-you-note.html` — thank-you notes
- `templates/inquiry-letter.md` + `html/inquiry-letter.html` — inquiry letters
- `templates/follow-up.md` + `html/follow-up.html` — follow-ups
- `templates/polite-decline.md` + `html/polite-decline.html` — polite declines
- `html/index.html` — kit landing page linking every template
- `scripts/verify_kit.py` — committed verification script (run with `python3 scripts/verify_kit.py`)
- `LICENSE` — MIT License, `Copyright (c) 2026 Asdale Dynamics, LLC`
- `README.md` — usage instructions, filled-in example, Asdale Dynamics, LLC credit
- `STATUS.md` — this file

Every template uses bracketed placeholders (`[Recipient Name]`, `[Your Name]`, etc.).
HTML fields are `contenteditable`, so they can be filled in the browser before
printing, or printed and filled in by hand. HTML pages are styled for clean
printing (`@media print`, US Letter, screen chrome hidden when printed).
No account, no tracking, no personal data, no build step, local-first.
Credit: Asdale Dynamics, LLC (Indiana), founded by Dylan Asdale.

## How to run it
- Markdown: open any `templates/*.md` in a text editor, replace the bracketed
  fields, delete the brackets, copy into your email client.
- HTML: open any `html/*.html` in a browser, click each underlined field and
  type, then print (Ctrl+P / Cmd+P) or save to PDF. Open `html/index.html` for
  the kit overview.
- Verification: `python3 scripts/verify_kit.py`
- Nothing to install, no server, nothing to buy.

## Verification results
- `python3 scripts/verify_kit.py` → VERIFICATION PASSED
- 13 expected files present
- All 5 HTML files parse with balanced tags (Python `html.parser`)
- All 4 template pages include `@media print` styles, `contenteditable`
  fields, and Asdale Dynamics, LLC credit
- `LICENSE` contains the exact line `Copyright (c) 2026 Asdale Dynamics, LLC`
- `README.md` contains the Asdale Dynamics, LLC credit and a filled-in example
- No `.github/workflows` directory; no secrets, API keys, or personal data found
- Git commits on `master`, working tree clean

## Known gaps
- `@page` is US Letter only; no A4 variant (Dylan is Indiana-based, so US
  Letter is the default)
- Printed output not visually QA'd in an actual browser/PDF (no headless
  browser available in this environment)
- Placeholder fields are simple underlined spans (contenteditable), not full
  `<form>` inputs — sufficient for copy/send and print-by-hand workflows
