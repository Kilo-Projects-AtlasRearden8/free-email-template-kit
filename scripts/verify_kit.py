#!/usr/bin/env python3
"""Verification for the Free Email Template Kit.

Checks that every expected file exists, HTML is well-formed, the LICENSE
copyright line is exact, the README credits Asdale Dynamics, LLC, no
.github/workflows are present, and no secrets/keys are committed.
Run with: python3 scripts/verify_kit.py
"""
import sys
from html.parser import HTMLParser
from pathlib import Path

root = Path(__file__).resolve().parent.parent
errors = []

expected = [
    "LICENSE",
    "README.md",
    "STATUS.md",
    "scripts/verify_kit.py",
    "templates/thank-you-note.md",
    "templates/inquiry-letter.md",
    "templates/follow-up.md",
    "templates/polite-decline.md",
    "html/index.html",
    "html/thank-you-note.html",
    "html/inquiry-letter.html",
    "html/follow-up.html",
    "html/polite-decline.html",
]

# 1. Files exist
for rel in expected:
    if not (root / rel).exists():
        errors.append(f"MISSING: {rel}")

# 2. LICENSE exact copyright line + MIT header
license_text = (root / "LICENSE").read_text()
if "Copyright (c) 2026 Asdale Dynamics, LLC" not in license_text:
    errors.append("LICENSE missing exact copyright line")
if "MIT License" not in license_text:
    errors.append("LICENSE missing MIT header")

# 3. README credits Asdale Dynamics, LLC
readme = (root / "README.md").read_text()
if "Asdale Dynamics, LLC" not in readme:
    errors.append("README missing Asdale Dynamics, LLC credit")

# 4. HTML parse + credit + title
class TagChecker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.bad = []
        self.void = {
            "area", "base", "br", "col", "embed", "hr", "img", "input",
            "link", "meta", "param", "source", "track", "wbr",
        }
    def handle_starttag(self, tag, attrs):
        if tag not in self.void:
            self.stack.append(tag)
    def handle_endtag(self, tag):
        if tag in self.void:
            return
        if not self.stack or self.stack[-1] != tag:
            self.bad.append(
                f"mismatched close </{tag}> (stack top: "
                f"{self.stack[-1] if self.stack else None})"
            )
        else:
            self.stack.pop()

template_pages = [
    "html/thank-you-note.html",
    "html/inquiry-letter.html",
    "html/follow-up.html",
    "html/polite-decline.html",
]
for rel in template_pages:
    text = (root / rel).read_text()
    checker = TagChecker()
    checker.feed(text)
    if checker.bad:
        errors.append(f"{rel}: " + "; ".join(checker.bad))
    if checker.stack:
        errors.append(f"{rel}: unclosed tags {checker.stack}")
    if "@media print" not in text:
        errors.append(f"{rel}: missing @media print styles")
    if "contenteditable" not in text:
        errors.append(f"{rel}: fields are not fillable (missing contenteditable)")
    if "Asdale Dynamics, LLC" not in text:
        errors.append(f"{rel}: missing Asdale Dynamics, LLC credit")
    if "<title>" not in text:
        errors.append(f"{rel}: missing <title>")

# index page: parse + credit + title (landing page)
for rel in ["html/index.html"]:
    text = (root / rel).read_text()
    checker = TagChecker()
    checker.feed(text)
    if checker.bad:
        errors.append(f"{rel}: " + "; ".join(checker.bad))
    if checker.stack:
        errors.append(f"{rel}: unclosed tags {checker.stack}")
    if "Asdale Dynamics, LLC" not in text:
        errors.append(f"{rel}: missing Asdale Dynamics, LLC credit")
    if "<title>" not in text:
        errors.append(f"{rel}: missing <title>")

# 5. No .github/workflows
if (root / ".github" / "workflows").exists():
    errors.append("FORBIDDEN: .github/workflows exists")

# 6. No real secrets/keys (placeholder text like [Your Name] is expected)
secret_patterns = ["sk-", "AKIA", "ghp_", "github_pat", "secret_key=", "api_key="]
for p in root.rglob("*"):
    if not p.is_file() or not p.is_relative_to(root):
        continue
    if ".git" in p.parts or p.name == "verify_kit.py":
        continue
    try:
        t = p.read_text()
    except Exception:
        continue
    for needle in secret_patterns:
        if needle in t:
            errors.append(f"POSSIBLE SECRET in {p.relative_to(root)}: {needle}")

if errors:
    print("VERIFICATION FAILED")
    for e in errors:
        print(" -", e)
    sys.exit(1)

print(
    f"VERIFICATION PASSED: {len(expected)} expected files present, "
    "all HTML well-formed, LICENSE/README credit correct, fields fillable, "
    "no workflows, no secrets."
)
