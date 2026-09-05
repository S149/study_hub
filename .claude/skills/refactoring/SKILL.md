---
name: refactoring
description: Behavior-preserving refactoring for a specific, user-selected piece of code (function, file, or module) — never the whole project. Use when the user asks to clean up, simplify, or restructure existing code without changing its behavior. Requires an explicit scope and a way to verify behavior before starting. Do NOT use for adding new behavior/features, or for repository-wide changes.
---

# Refactoring

Refactoring = improving code structure WITHOUT changing what it does.
This skill applies only to the scope the user names — a specific function, file, or module. Never expand scope to "the whole project" or nearby files unless the user explicitly asks.

## Step 0 — Confirm scope and baseline (always do this first)

Before touching any code:

1. **Scope**: Restate exactly what will be refactored (e.g. "only the `calculateTotal` function in `cart.ts`"). If the user's request is vague ("clean up the code"), ask them to name the file/function, or propose a scope and get confirmation.
2. **Baseline**: Check if there's a way to verify behavior doesn't change:
   - Existing automated tests covering this code → run them, confirm they pass, note the result.
   - No tests → say so explicitly, and either:
     a) ask the user if they want tests written first, or
     b) proceed manually with extra care, showing before/after behavior comparison (e.g. sample inputs/outputs) instead of automated proof.
3. Do not proceed to refactoring until scope and baseline status are clear.

## When to refactor

- Only if it genuinely improves readability, removes duplication, or clarifies intent.
- Skip if the code is already clean enough for the task at hand.
- Skip if "improvement" would require speculative abstractions for requirements that don't exist yet.

## Priority

| Priority | Action | Examples |
|---|---|---|
| Critical | Fix now | Duplicated business logic, confusing control flow on a risky path |
| High | Do in this pass | Magic numbers, unclear names, functions doing too many things |
| Nice | Mention, don't do | Minor naming, single-use helpers |
| Skip | Leave alone | Already clean |

## Workflow

1. Confirm scope + baseline (Step 0).
2. Make ONE small change at a time (e.g. extract one constant, rename one variable, split one function).
3. After each change: re-run tests if available, or manually re-check behavior (same inputs → same outputs).
4. Stop and show the diff to the user before moving to the next change if the change is non-trivial.
5. Never commit without explicit user approval. Keep refactor commits separate from feature commits.

## DRY — abstract only when it's the same *knowledge*

**Merge/abstract when:**
- Same business rule or concept
- Would change together if requirements change

**Keep separate when:**
- Looks similar but represents different concepts
- Would evolve independently

## Never do this during refactoring

- ❌ Add new behavior, error handling, or edge-case logic that wasn't there before (that's a feature — needs its own task/test).
- ❌ Touch files/functions outside the confirmed scope.
- ❌ Remove a code branch just because it looks unused — check all callers first, or ask the user to confirm it's dead.
- ❌ Commit without explicit approval.

## Checklist before finishing

- [ ] Only the confirmed scope was touched
- [ ] Behavior verified unchanged (tests pass, or manual before/after check shown)
- [ ] No new behavior/features slipped in
- [ ] Code is more readable than before
- [ ] Diff shown to user; commit only if explicitly approved