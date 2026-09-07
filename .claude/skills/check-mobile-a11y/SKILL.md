---
name: check-mobile-a11y
description: Drive the browser through a checklist of known mobile-layout and accessibility trouble spots in Study Hub (index.html) — tooltip clipping/direction, off-screen elements, empty table cells, keyboard focus, contrast. Use before considering a new or edited page in index.html "done", or when the user reports a layout/a11y bug.
---

# Check Mobile & Accessibility

This project (a single-file static site, `index.html`) has repeatedly shipped pages with the same category of bugs, caught only after the fact:
- Tooltip arrow pointing the wrong direction for keyword/K-level pills.
- Off-screen tooltips on narrow viewports.
- Empty stats cells on mobile layout.
- Native `<select>` used instead of the themed listbox (inconsistent styling/keyboard behavior).

Run this checklist proactively instead of waiting for the user to find these.

## How to run

1. Open the page/section under review in the Browser tool (`preview_start` with a `url` pointing at the local `index.html`, or the dev preview if running).
2. **Resize to mobile** (`resize_window` preset `mobile`, 375x812) and reload.
3. Walk the new/changed section and check:
   - Every tooltip (keyword pills, K-level pills, info icons): hover/tap and confirm the tooltip stays on-screen and the arrow points at its trigger.
   - Every table/stat block: confirm no empty cells where mobile CSS collapses columns.
   - Any dropdown/select: confirm it's the themed listbox component, not a native `<select>`.
   - Scroll the full section; nothing should overflow horizontally or get clipped by the sidebar.
4. **Switch to desktop** (`resize_window` preset `desktop`) and re-check the same spots — some bugs are desktop-only (e.g. tooltip direction near viewport edges).
5. **Keyboard pass**: tab through interactive elements (tooltips, listbox, footer nav) and confirm focus is visible and order is logical.
6. **Contrast**: spot-check text against `--ink`/`--ink-muted` on `--surface`/`--surface-2` in both light and dark (`resize_window` `colorScheme`) — the sidebar is always dark regardless of site theme, so check contrast there separately.
7. Report findings as concrete bugs (element + what's wrong), fix them, and re-check.
