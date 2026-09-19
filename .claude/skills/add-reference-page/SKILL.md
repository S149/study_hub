---
name: add-reference-page
description: Turn a source PDF (or other study material) into a new reference section in index.html, following this project's existing design system, sidebar/TOC wiring, JS routing, and component patterns. Use when the user wants to add a new standard/syllabus page (e.g. another ISTQB module, a new OWASP doc) to Study Hub.
disable-model-invocation: true
---

# Add Reference Page

Study Hub (`index.html`) is a single-file static site. Every reference page (ISTQB modules, OWASP ASVS, WCAG, etc.) is hand-authored inside that one file, following the same structural and visual conventions, **and the same JavaScript routing wiring**. Most repeat bugs on this project have come from the second half — content that looks right but that the router doesn't know how to navigate to. This skill exists to stop re-deriving (and re-breaking) that pattern from scratch each time.

Treat every step below as required, not optional. A page that "looks done" in a text diff but skips the routing/verification steps is not done — it will silently bounce users back to the hub menu.

## Steps

### 1. Identify the source
Confirm the PDF lives in `sources/` (or ask the user to drop it there). Use the `pdf` skill / PDF reading to extract structure: chapters, sections, key terms, tables.

**Extract exact numbers, never estimate.** Pull the precise learning-objective count and the precise cognitive-level range (K1–K5) straight from the syllabus's own "Learning Objectives" list (usually a `PREFIX-x.y.z (Kn) ...` pattern per section). Do not write `~35` or guess a K-range like "K1–K3" by copying another page's stat card — count it from the source and verify against every K-level actually used.

### 2. Study an existing page of the same shape — and copy its exact ID scheme
Don't guess the pattern — open one comparable existing section in `index.html` (e.g. CT-SEC for a multi-chapter specialist syllabus, WCAG/ASVS for a standard) and read it end to end: its `<section>`/heading structure, footer (`class="pagefoot"`), callout boxes (`--note/--warn/--success` tokens), tooltip/pill components, and how it registers in the sidebar TOC (`#side-toc`, `.toc-chapter`, `.toc-ch-row`).

**Different syllabi on this site use slightly different id-prefix conventions** (e.g. some use a bare `secX-Y-Z` for both the sidebar link and the content heading; others use an `h`-prefixed variant in places). Do not assume the pattern from memory or from a *different* syllabus than the one you're templating off. For the syllabus you're copying, grep it directly and confirm, side by side:
- the `href="#...">` in its sidebar `.toc-sub` links,
- the `id="..."` on the matching `<h2>` in its content, and
- the `id="..."` on the wrapping `<section class="topic" id="t...">`.

All three families must use the exact same numbering suffix (just prefixed with `t` for the section wrapper) for every single subsection — copy that scheme mechanically, don't improvise a new one.

### 3. Reuse design tokens, never hardcode colors/fonts
Use the existing CSS custom properties (`--c1`..`--c6`, `--ink`, `--surface`, `--accent`, `--radius`, `--shadow`, `--font-heading`, `--font-body`) — do not introduce new ad hoc colors or fonts.

### 4. Build full content depth for every chapter — no stubs
Match the granularity of the template page for **every** chapter, not just the first one. Break into the same section/subsection rhythm as the source's own numbering (1.1, 1.1.1, 1.1.2…) — don't dump the whole PDF as one wall of text, and don't write a detailed chapter 1 followed by thin one-paragraph placeholders for chapters 2–N. If the syllabus has 8 chapters, all 8 need the same density of cards/tables/callouts/keyword tooltips as the template.

**Keyword tooltip formatting**: when a glossary term has an abbreviation or synonym, put it on its **own** `<span class="kw-line">` with a `<strong>` label — `<span class="kw-line"><strong>Abbreviation:</strong> SUS</span>` / `<span class="kw-line"><strong>Synonyms:</strong> facilitator</span>` — never inline as plain trailing text in the definition sentence. Check the template page's tooltips for the exact wrapping.

**Keyword tooltips contain ONLY the definition plus Abbreviation and/or Synonyms lines.** Do not add any other glossary metadata — no `See also`, `Reference`, `Term type`, or `Version` lines — even when the glossary PDF lists them.

### 5. Wire it into sidebar navigation (HTML)
Add the corresponding entry to the sidebar TOC (`#side-toc` / `.side-toc-nav`) so the page is reachable, matching the existing chapter/section nesting pattern (`.toc-section-divider`, `.toc-chapter`, `.toc-ch-row`, `.toc-ch-body`). Also add the syllabus's entry to the hub category list (`.synchoice-list` under the relevant `.hub-category`) and to the hub page's own per-chapter `<ul class="hublist">` listing with the **full** per-chapter subsection TOC (not an abbreviated 1–2-item summary) — this listing uses the exact same ids as the sidebar.

### 6. Wire it into JavaScript routing — this is the step most often skipped
Adding the HTML is not enough. The page's view-switching, sidebar-visibility, and search logic are all driven by small hardcoded JS tables near the end of the file (search for `var VIEWS`, `var ID_TO_VIEW`, `function currentChapterNum`, `function syllabusOf`, `var CHAPTER_ROOT`). **Every one of these must be updated with your new chapter-id prefix**, or the page will silently misbehave — usually by bouncing back to the hub on any click, or by never showing the sidebar at all. Update all of the following:

| What | Where (search for) | What to add |
|---|---|---|
| Chapter view whitelist | `var VIEWS = [...]` | Your new syllabus root id (e.g. `"ctut"`) and every chapter id (e.g. `"ut1"..."ut8"`) |
| Content-id → view lookup | `var ID_TO_VIEW = {...}` | **Every** `id=` you used in your new chapter content (section wrappers, headings, keyword-tooltip ids, K-pill tooltip ids, recap heading) mapped to its owning chapter view id. This table is large (100+ entries per syllabus) — generate it programmatically from your own HTML rather than typing it by hand, then paste it in. |
| Sidebar visibility / "am I in a chapter" detection | `function currentChapterNum()` regex `/^view-(ch\d\|ta\d\|pt\d\|...)$/` | Your new chapter prefix added to the alternation |
| Sidebar syllabus filter (which chapters show when open) | `function syllabusOf(ch)` | A new `if (/^yourprefix\d$/.test(ch)) return 'yourprefix';` branch |
| Global search result grouping | `var CHAPTER_ROOT = [...]` | A new `[/^yourprefix\d+/, 'yoursyllabusroot']` entry |

After editing, **re-verify none of these five spots still miss your prefix** — grep each one for your new prefix string and confirm it appears in all five.

### 7. Self-verify before calling it done
Run these checks against `index.html` and fix anything they surface — don't rely on eyeballing the diff:

- **Tag balance** on the new content block specifically (not just the whole file): counts of `<div>`/`</div>`, `<section>`/`</section>`, `<span>`/`</span>`, `<h2>`/`</h2>`, `<table>`/`</table>`, `<dl>`/`</dl>`, `<ul>`/`</ul>` must match.
- **Link resolution**: every `href="#xxx"` added in the sidebar/hub-page TOC must have a matching `id="xxx"` somewhere in the new content (chapter-root ids like `#ut1` are the one expected exception — those resolve via the JS router, not a literal element id).
- **Routing round-trip**: for a handful of representative subsection ids, confirm they appear in `ID_TO_VIEW` mapped to the correct chapter, and that the chapter id appears in `VIEWS`.
- **Stats card**: the "Learning objectives" number is an exact integer (no `~`), and the K-level range matches every K-level actually used by the syllabus's own LOs — cross-check against your Step 1 extraction, not a copy-pasted range from another page.

### 8. Run the `check-mobile-a11y` skill
Do this last, against the new section — this project has a history of shipping pages with mobile layout and tooltip-clipping bugs that get fixed in a follow-up commit. Catch them now instead.

## Things this project has gotten wrong before (don't repeat)

**Routing / JS wiring** (the most common and most invisible category — the HTML renders fine, so it's easy to skip these and only discover the bug when a user actually clicks something):
- New syllabus added to the page HTML and sidebar, but never added to `VIEWS` — its top-level "chapters" hub page never opens (stays on the general hub).
- Chapter content written with full id structure, but none of those ids added to `ID_TO_VIEW` — clicking any sidebar/TOC subsection link bounces back to the main hub menu instead of opening the chapter.
- New chapter-id prefix missing from `currentChapterNum()`'s regex — the side table-of-contents panel never appears at all while viewing that syllabus's chapters (it silently stays `hidden`).
- New chapter-id prefix missing from `syllabusOf()` — even if the sidebar does show, it displays the wrong syllabus's chapter list.
- New chapter-id prefix missing from `CHAPTER_ROOT` in the search script — global search results for that syllabus get grouped under the wrong (or no) syllabus label.

**Content quality**:
- Placeholder-depth content ("Chapter N in one screen" with a single generic paragraph) shipped for later chapters while chapter 1 got full treatment — inconsistent and reads as unfinished.
- Approximate stats (`~35` learning objectives, a guessed K-level range) instead of the exact count/range from the source.
- Glossary terms' Abbreviation/Synonyms typed as inline trailing text in the definition instead of their own styled `<span class="kw-line"><strong>...</strong></span>` line.

**Markup/id scheme**:
- Sidebar TOC subsection links built with an invented `h`-prefixed id scheme that doesn't match what the actual content headings use, breaking every jump link in that chapter's table of contents.

**Visual/mobile** (verify with `check-mobile-a11y`):
- Tooltip arrows pointing the wrong direction for keyword/K-level pills.
- Empty stats cells and off-screen tooltips on mobile widths.
- Native `<select>` used instead of the project's themed listbox component.
