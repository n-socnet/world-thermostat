# HANDOFF.md — Session Log

Every work session ends with a new entry at the top, whichever agent (or person) did the work. The next session starts by reading the newest entry.
Entries older than a few weeks can be trimmed to one line each.

## Entry format

```
### YYYY-MM-DD — session title
- Agent / model:
- Branch / PR:
- Built or changed:
- Decisions made (and why):
- Verified (and how):
- Not verified / known issues:
- Next step:
```

---

<!-- New entries go below this line, newest first -->

### 2026-11-24 — Agent Kit v1.1 installed
- Agent / model: Claude (Opus 5.5)
- Branch / PR: `agent/claude/agent-kit-v1.1` (or first commit on an empty repo)
- Built or changed: added the N-SOC Agent Kit (AGENTS.md rules, pointer files for Claude/Gemini/Copilot, LESSONS, HANDOFF, DESIGN, PRELAUNCH, guide). Existing files were not overwritten.
- Decisions made (and why): AGENTS.md is the one rules file so every agent reads the same rules.
- Verified (and how): installer output checked; files present; no existing file content removed.
- Not verified / known issues: Project facts are only partly filled in.
- Next step: owner fills in the blank Project facts in AGENTS.md (especially Definition of done).
