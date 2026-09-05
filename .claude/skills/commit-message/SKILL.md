---
name: commit-message
description: Use this skill when the user asks to write or suggest a git commit message. Formats messages using Conventional Commits (feat, fix, docs, chore, etc).
---

# Commit Message Skill

## Rules
1. Format: `<type>(<scope>): <short description>`
2. Types: feat, fix, docs, style, refactor, test, chore
3. Description in imperative mood, under 50 characters
4. If the change is complex, add a body explaining "why", not "what"

## Example
feat(auth): add JWT token refresh logic

- Tokens now auto-refresh 5 minutes before expiry
- Prevents forced re-login during long sessions