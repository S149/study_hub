---
name: add-reference-page
description: Turn a source PDF (or other study material) into a new reference section in index.html, following this project's existing design system, sidebar/TOC wiring, and component patterns. Use when the user wants to add a new standard/syllabus page (e.g. another ISTQB module, a new OWASP doc) to Study Hub.
disable-model-invocation: true
---

# Add Reference Page

Study Hub (`index.html`) is a single-file static site. Every reference page (ISTQB modules, OWASP ASVS, WCAG, etc.) is hand-authored inside that one file, following the same structural and visual conventions. This skill turns a new source PDF into a page that matches the rest of the site instead of reinventing the pattern (and re-introducing bugs already fixed on earlier pages).

## Steps

1. **Identify the source.** Confirm the PDF lives in `sources/` (or ask the user to drop it there). Use the `pdf` skill / PDF reading to extract structure: chapters, sections, key terms, tables.

2. **Study an existing page of the same shape first.** Don't guess the pattern — open one comparable existing section in `index.html` (e.g. the OWASP ASVS or WCAG page) and read it end to end: its `<section>`/heading structure, footer (`class="pagefoot"`), callout boxes (`--note/--warn/--success` tokens), tooltip/pill components, and how it registers in the sidebar TOC (`#side-toc`, `.toc-chapter`, `.toc-ch-row`).

3. **Reuse design tokens, never hardcode colors/fonts.** Use the existing CSS custom properties (`--c1`..`--c6`, `--ink`, `--surface`, `--accent`, `--radius`, `--shadow`, `--font-heading`, `--font-body`) — do not introduce new ad hoc colors or fonts.

4. **Wire it into navigation.** Add the corresponding entry to the sidebar TOC (`#side-toc` / `.side-toc-nav`) so the page is reachable, matching the existing chapter/section nesting pattern.

5. **Build content incrementally**, matching the granularity of existing pages (don't dump the whole PDF as one wall of text — break into the same section/subsection rhythm as neighboring pages).

6. **Before calling it done, run the `check-mobile-a11y` skill** against the new section — this project has a history of shipping pages with mobile layout and tooltip-clipping bugs that get fixed in a follow-up commit. Catch them now instead.

## Things this project has gotten wrong before (don't repeat)
- Tooltip arrows pointing the wrong direction for keyword/K-level pills.
- Empty stats cells and off-screen tooltips on mobile widths.
- Native `<select>` used instead of the project's themed listbox component.
