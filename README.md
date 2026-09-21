# Study Hub

An independent, single-page study resource for software testing certifications and standards: ISTQB® syllabi, the WCAG accessibility guidelines and the OWASP Application Security Verification Standard.

**Live site:** https://s149.github.io/study_hub/

> Study Hub is not affiliated with or endorsed by ISTQB®, W3C® or OWASP®. It is a non-commercial study aid based on publicly available syllabi, glossaries and standards. All original material remains the property of its owners; see [Sources and copyright](#sources-and-copyright).

## What is inside

Each module opens as a self-contained guide with chapter summaries, key-term tooltips taken from the official glossary, cognitive-level (K-level) tooltips on learning objectives, diagrams, worked examples and a short recap per chapter.

| Group | Module | Source version |
|---|---|---|
| Foundation | CTFL — Foundation Level | v4.0.1 |
| Core Advanced | CTAL-TA — Test Analyst | v4.0 |
| Core Advanced | CTAL-TTA — Technical Test Analyst | v4.0 |
| Core Advanced | CTAL-TM — Test Manager | v3.0 |
| Testing Specialist | CT-PT — Performance Testing | v1.0 (2018) |
| Testing Specialist | CT-UT — Usability Testing | v1.0 (2018) |
| Testing Specialist | CT-AcT — Acceptance Testing | v1.0 (2019) |
| Testing Specialist | CT-MBT — Model-Based Testing | v1.1 |
| Testing Specialist | CT-GenAI — Testing with Generative AI | v1.1 |
| Testing Specialist | CT-SEC — Security Tester | v1.0 (2016) |
| Testing Specialist | CTAL-AT — Agile Tester | v2.0 |
| Additional Materials | WCAG — Accessibility Reference | 2.2 |
| Additional Materials | ASVS — Application Security Reference | 5.0.0 |

## Features

- Hash-routed single page: every chapter and section has a stable link (`#ch4`, `#tt2`, …).
- Sidebar table of contents that follows the syllabus you are reading.
- Full-text search across all modules or within the current one (`Ctrl/Cmd + K`).
- Filterable WCAG and ASVS requirement tables.
- Light and dark themes, following the system setting.
- Responsive layout and keyboard-accessible components; diagrams are inline SVG with text descriptions.

## Run locally

There is no build step. The site is one static file, `index.html`.

```bash
python -m http.server 5173
```

Then open http://localhost:5173. Fonts are loaded from Google Fonts, so the page needs an internet connection to render them.

## Project layout

```
index.html                     the whole site: markup, styles and scripts
sources/                       source PDFs (git-ignored, not published)
.claude/                       Claude Code project configuration
  skills/add-reference-page/     how a new syllabus is added and wired in
  skills/check-mobile-a11y/      mobile and accessibility checklist
  skills/commit-message/         commit message conventions
  skills/refactoring/            behaviour-preserving refactoring rules
  agents/ui-reviewer.md          reviewer for mobile-layout and accessibility issues
  hooks_check_html.py            HTML tag-balance check for edits to index.html
```

## Adding a new module

New syllabi follow the conventions documented in `.claude/skills/add-reference-page/SKILL.md`: the id scheme, sidebar and hub wiring, the JavaScript routing tables, keyword-tooltip formatting and the diagram rules. In Claude Code the workflow is started with:

```
/add-reference-page <path to syllabus PDF>, keywords from <path to glossary PDF>
```

## Sources and copyright

The content is written from the official documents listed above; the PDFs themselves are not part of this repository. ISTQB® is a registered trademark of the International Software Testing Qualifications Board, and the syllabi and glossary are © ISTQB®. WCAG is published by the W3C®; the OWASP Application Security Verification Standard is published by OWASP®. Please refer to the original documents for authoritative wording.

## License

No license has been chosen for the code and original text of this repository yet.
