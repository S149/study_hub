# CTAL-TA chapter authoring spec (shared across all 5 chapters)

You are writing ONE chapter's HTML content for an existing, published study-hub artifact
(a single self-contained HTML page, ISTQB CTFL + now CTAL-TA study hub). You must reuse the
EXACT existing CSS component vocabulary below — do not invent new CSS classes, do not add
<style> or <script> blocks, do not add opacity to colored text/boxes (WCAG contrast rule),
do not use color alone to convey meaning.

## Output file
Write your output to the exact path given to you in your task (one file). It must contain
THREE clearly delimited blocks, in this exact order, each wrapped in an HTML comment marker
so they can be spliced out programmatically:

```html
<!-- HUBITEM-START -->
...single <li class="hubitem" ...>...</li> block...
<!-- HUBITEM-END -->
<!-- TOCCHAPTER-START -->
...single <div class="toc-chapter" ...>...</div> block...
<!-- TOCCHAPTER-END -->
<!-- VIEW-START -->
...single <div class="view" id="view-taN" hidden>...</div> block...
<!-- VIEW-END -->
```

Do not include anything else in the file (no markdown, no explanation, no code fences).

## Identity for your chapter
You will be told: chapter number N (1-5), chapter title, accent hex (light) and accent hex
(dark), the emoji icon, and the full syllabus source text for your chapter (from the official
ISTQB CTAL-TA v4.0 syllabus). ALL content must be derived from that source text — do not
invent facts, examples, or numbers not present in the source. You may paraphrase for
readability the way a study guide would, but keep every concept, technique, criterion, and
example from the source. Do not omit content to save space — full coverage is required,
matching the depth of detail in the source (this is an advanced-level syllabus, denser than
Foundation Level).

## ID naming (CRITICAL — avoid collisions with existing CTFL content which uses ch1..ch6,
## t1-1, h1-1, etc.)
- View: `id="view-taN"` (e.g. `view-ta3`)
- Main landmark: `id="main-taN"` with `tabindex="-1"`
- Topic section id: `id="ttaN-S"` (e.g. `tta3-1`, `tta3-2`) — one per top-level numbered
  section (3.1, 3.2, ...)
- Heading ids: `id="htaN-S"` for the section's `<h2>` (e.g. `hta3-1`), `id="htaN-S-K"` for a
  `<h3>` subsection (e.g. `hta3-1-1`), and if a sub-subsection is needed `htaN-S-K-J`.
- Recap heading id: `id="recap-heading-taN"`
- Hub anchor id: `id="ht-taN"` on the `<h2>` inside the hubitem
- data-ch attribute: use `data-ch="taN"` on both the hubitem `<li>` and the toc-chapter `<div>`
  (NOT a bare number — the existing CTFL ones use `ch1`..`ch6`, yours use `taN`)
- Keyword tooltip ids: `id="kwtip-taN-K"` (e.g. `kwtip-ta3-1`) — the `taN-` prefix avoids
  colliding with CTFL's existing `kwtip-1`..`kwtip-102`.

## Accent color usage
Use CSS variable `--card-accent-light` / `--card-accent-dark` (inline style, exact hex you
were given) on both the hubitem `<li>` and the toc-chapter `<div>` — copy this pattern
verbatim (values are placeholders, use your real hex):
```html
<li class="hubitem" style="--card-accent-light:#961B31; --card-accent-dark:#F19EAC;" data-ch="ta1">
```
```html
<div class="toc-chapter" data-ch="ta1" style="--card-accent-light:#961B31; --card-accent-dark:#F19EAC;">
```
You do NOT need to write the `#view-taN { --accent: ... }` CSS scoping rule yourself — that is
added separately to the stylesheet. Just use the two data attributes above consistently.

## Component vocabulary (use ONLY these; copy structure exactly, vary only text/counts)

### View wrapper + topbar + hero (top of your VIEW block)
```html
<div class="view" id="view-ta1" hidden>
<header class="topbar">
  <div class="topbar-inner">
    <a class="brand" href="#"><span class="mark" aria-hidden="true">✦</span> ISTQB Study Hub</a>
    <nav class="jumpnav" aria-label="Sections in this chapter">
      <a href="#tta1-1">Short Label</a>
<a href="#tta1-2">Short Label</a>
    </nav>
  </div>
</header>
<main id="main-ta1" tabindex="-1">
  <section class="hero">
    <p class="eyebrow"><span class="dot" aria-hidden="true"></span><span aria-hidden="true">🧭</span> CTAL-TA · Chapter 1</p>
    <h1>Chapter Title</h1>
    <p class="lede">2-4 sentence chapter intro, adapted from the syllabus's own chapter intro paragraph.</p>
    <ul class="keywords" aria-label="Key terms in this chapter">
<li class="kw-chip" tabindex="0" aria-describedby="kwtip-ta1-1">term<span class="kw-pop" id="kwtip-ta1-1" role="tooltip"><span class="kw-line">Definition, 1 sentence, derived from how the syllabus defines/uses the term.</span></span></li>
    </ul>
  </section>
```
Note: keyword `<li>` elements must NOT have `role="button"` (invalid ARIA on a list item —
this was a bug we fixed elsewhere; just `tabindex="0" aria-describedby="...">`). Put ALL
keyword chips for the chapter (from the syllabus's "Keywords" list at the chapter head) in
this one `<ul class="keywords">`, same one-line-per-several-chips density as shown (don't
add line breaks inside `<li>` tags themselves — write them all on one or a few long lines,
exactly like the existing hub does, it's fine for the source to be dense here).

### Topic section (repeat per top-level numbered section, e.g. 1.1, 1.2, ...)
```html
<section class="topic" id="tta1-1" aria-labelledby="hta1-1">
  <p class="subhead">1.1</p>
  <h2 id="hta1-1">Section Title</h2>
  <p>Intro paragraph for the section.</p>

  <h3 id="hta1-1-1">1.1.1 Subsection Title</h3>
  <p>Body text. Use <strong>bold</strong> for key terms on first use, <em>emphasis</em>
  sparingly. Use &mdash; (em dash), &rsquo; (right single quote), &ldquo;&rdquo; (curly
  quotes) as HTML entities, not literal unicode characters.</p>
</section>
```
Every learning objective code from the syllabus (e.g. `TA-1.1.1 (K2)`) should surface
somewhere near its topic — either as a `<span class="pill">K2</span>` badge inline near the
relevant `<h3>`, or folded into a callout. Use `.pill` like this right after the heading text
inside the `<h3>` (or on its own line right under it) — e.g.:
```html
<h3 id="hta1-1-1">1.1.1 Subsection Title <span class="pill">K2</span></h3>
```

### Card grid (for parallel short items: lists of factors, benefits, criteria, etc.)
```html
<div class="card-grid cols-3">
  <div class="card"><h4>Short heading</h4><p>1-2 sentence description.</p></div>
  <div class="card"><h4>Short heading</h4><p>1-2 sentence description.</p></div>
</div>
```
Use `cols-2` or `cols-3` depending on item count/length. A card can also omit `<h4>` and just
have `<p>` (for a plain bullet-like list), or add `<span class="tag">Label</span>` before the
`<h4>` for a category tag (used sparingly).

### Table (for comparisons, criteria checklists with descriptions, tool categories, etc.)
```html
<div class="table-wrap">
  <div class="table-scroll">
  <table>
    <thead><tr><th scope="col">Column A</th><th scope="col">Column B</th></tr></thead>
    <tbody>
      <tr><th scope="row">Row label</th><td>Cell</td></tr>
    </tbody>
  </table>
  </div>
</div>
```
Never leave a `<th scope="col">` empty — if a column genuinely has no label, use
`<th scope="col"><span class="sr-only">Hidden label</span></th>`.

### Flowchain (for sequential processes/pipelines, 3-7 steps)
```html
<div class="flowchain" role="img" aria-label="Full text description of what this diagram shows, for screen readers">
  <div class="step"><span class="n">01</span><strong>Step name</strong><span class="d">Short description</span></div>
  <div class="arrow" aria-hidden="true">→</div>
  <div class="step"><strong>Step name</strong><span class="d">Short description</span></div>
</div>
```
The `<span class="n">` (step number/label) is optional per step.

### Callout (for asides, notes, warnings, "don't confuse this with X")
```html
<div class="callout"><span class="label">Note</span><p>Callout text.</p></div>
```
Vary the label text (e.g. "Note", "Key distinction", "Watch out", "Example") — don't reuse the
same label twice in one chapter.

### Rail (for ordered/numbered principles or steps, like a numbered list of core ideas)
```html
<ol class="rail">
  <li><span class="num" aria-hidden="true">1</span><div><h3>Point title</h3><p>Explanation.</p></div></li>
</ol>
```

### Spectrum (for a scale/continuum with 3-5 discrete levels)
```html
<div class="spectrum" role="img" aria-label="Full text description of the scale, for screen readers">
  <div class="seg"><span class="lvl">Level label</span><strong>Name</strong><span>Description</span></div>
</div>
```

### Deflist (for the chapter recap, at the very end — REQUIRED, one per chapter)
```html
<section class="recap" aria-labelledby="recap-heading-ta1">
<h2 id="recap-heading-ta1">Chapter 1 in one screen</h2>
<dl class="deflist">
<div><dt>Term</dt><dd>One-line definition.</dd></div>
</dl>
</section>
```
Include 10-16 of the chapter's most important terms/ideas as recap entries.

### Footer (after recap, closes the view)
```html
</main>
<footer class="pagefoot">
  <span class="step"></span>
  <span class="step">Chapter N of 5 · CTAL-TA</span>
  <a href="#taN+1">Next Chapter Title →</a>
</footer>
</div>
```
For chapter 5 (last), omit the `<a>` link (leave that pagefoot slot empty, matching how the
existing hub's last chapter has no "next" link — just two empty `<span class="step">` there
in that case, check with your task for the exact next-chapter title/link if you're not
chapter 5).

## Hub card block (goes in HUBITEM-START/END)
```html
<li class="hubitem" style="--card-accent-light:#HEXLIGHT; --card-accent-dark:#HEXDARK;" data-ch="taN">
  <span class="hub-num" aria-hidden="true">TA1</span>
  <span>
    <h2 id="ht-ta1"><a href="#ta1"><span aria-hidden="true">🧭</span> Chapter Title</a></h2>
    <p class="blurb">One-sentence chapter summary.</p>
    <ul class="toc" aria-label="Contents of Chapter 1">
      <li class="toc-sec"><a href="#tta1-1"><span class="n">1.1</span>Section Title</a>
        <ul class="toc-sub">
          <li><a href="#hta1-1-1"><span class="n">1.1.1</span>Subsection Title</a></li>
        </ul>
      </li>
    </ul>
  </span>
</li>
```
This TOC must exactly mirror the section/subsection structure and ids you used in your VIEW
block (same hrefs). A top-level section with no subsections omits the nested `<ul class="toc-sub">`.

## Sidebar toc-chapter block (goes in TOCCHAPTER-START/END)
```html
<div class="toc-chapter" data-ch="ta1" style="--card-accent-light:#HEXLIGHT; --card-accent-dark:#HEXDARK;">
  <div class="toc-ch-row">
    <a class="toc-ch-link" href="#ta1">
      <span class="toc-ch-ico" aria-hidden="true">🧭</span>
      <span class="toc-ch-label">TA1. Chapter Title</span>
    </a>
    <button class="toc-ch-toggle" type="button" aria-expanded="false" aria-controls="toc-ta1-body">
      <span class="toc-ch-caret" aria-hidden="true">›</span>
      <span class="sr-only">Toggle sections of Chapter 1 (CTAL-TA)</span>
    </button>
  </div>
  <div class="toc-ch-body" id="toc-ta1-body" hidden>
  <!-- exact same <ul class="toc">...</ul> markup as the hubitem's TOC above, byte-for-byte identical -->
  </div>
</div>
```

## WCAG rules (non-negotiable, already enforced site-wide — do not violate)
- Never use inline `opacity` on any element that has both a background and text color (kills
  contrast). Don't add opacity anywhere.
- Every image/diagram substitute (flowchain, spectrum) needs a full descriptive
  `aria-label` on the `role="img"` wrapper — write real, useful alt text, not "diagram".
  Decorative emoji/icons get `aria-hidden="true"`.
  - Do not use color alone to distinguish items in a card-grid or table — always pair with a
  text label (already the pattern: card-grid items all have `<h4>` text, not just color).
- Use real HTML entities: `&mdash;` `&rsquo;` `&ldquo;` `&rdquo;` `&amp;` `&ndash;` — never
  raw curly-quote/em-dash unicode characters (keeps the file's encoding consistent with the
  rest of the page, which uses entities throughout).
- Keep table headers non-empty (see Table section above).

## Tone / style
Match the existing CTFL hub's voice: crisp, confident, study-guide register — short
sentences, active voice, no fluff, no marketing language, no "In today's fast-paced world".
Bold the term being defined on first mention in body prose. Prefer concrete examples from the
syllabus over abstract restatement.
