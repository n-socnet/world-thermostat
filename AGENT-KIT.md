# N-SOC Agent Kit — Guide (v1.1)

A small set of plain-text files that gives every repository the same working rules, safety checks and memory between sessions, for **any AI agent** (Claude, Codex, Gemini, Copilot, Grok, ChatGPT, local models) and for people.

Nothing to install, nothing that runs on its own. Every file is Markdown that agents read at the start of a session.

---

## Table of contents

1. [What's in the kit](#1-whats-in-the-kit)
2. [How each agent finds the rules](#2-how-each-agent-finds-the-rules)
3. [Starting a new project](#3-starting-a-new-project)
4. [Adding the kit to an existing repo](#4-adding-the-kit-to-an-existing-repo)
5. [The working loop](#5-the-working-loop)
6. [Several agents on one repo](#6-several-agents-on-one-repo)
7. [File-by-file guide](#7-file-by-file-guide)
8. [Risks the kit guards against](#8-risks-the-kit-guards-against)
9. [Customizing per project](#9-customizing-per-project)
10. [Updating the kit](#10-updating-the-kit)
11. [FAQ](#11-faq)
12. [Changelog](#12-changelog)

---

## 1. What's in the kit

| File | Purpose | Read by | When |
|---|---|---|---|
| `AGENTS.md` | **The rules.** Project facts, file locations, workflow, git, security, cost | Every agent | Every session start |
| `CLAUDE.md` | Pointer to `AGENTS.md` (plus any Claude-only project notes) | Claude Code | Automatically |
| `GEMINI.md` | Pointer to `AGENTS.md` | Gemini CLI | Automatically |
| `.github/copilot-instructions.md` | Pointer to `AGENTS.md` | GitHub Copilot | Automatically |
| `LESSONS.md` | Mistakes not to repeat | Every agent | Every session start |
| `HANDOFF.md` | Session log: who did what, next step | Every agent | Start and end of every session |
| `DESIGN.md` | Colors, type, components, layout, voice | Every agent | Before UI work |
| `PRELAUNCH.md` | Go-live checklist | Agent runs it, owner signs off | Before anything goes public |
| `AGENT-KIT.md` | This guide | People | Setup and reference |
| `.gitignore` / `.env.example` | Keep secrets out of git; list env variables | git / people | Always (template only for `.env.example`) |
| `scripts/install-agent-kit.sh` | Adds the kit to an existing repo safely | People / agents | Once per repo (template repo only) |

## 2. How each agent finds the rules

| Agent | Reads automatically | What to do |
|---|---|---|
| Claude Code | `CLAUDE.md` → imports `AGENTS.md` | Nothing |
| OpenAI Codex | `AGENTS.md` | Nothing |
| Gemini CLI | `GEMINI.md` → imports `AGENTS.md` | Nothing |
| GitHub Copilot (chat / coding agent) | `.github/copilot-instructions.md`, `AGENTS.md` | Nothing |
| Cursor, Windsurf, Zed and other `AGENTS.md`-aware tools | `AGENTS.md` | Nothing |
| Claude, ChatGPT, Grok, Gemini in a browser chat | nothing | Upload or paste `AGENTS.md` + newest `HANDOFF.md` entry, say "follow these rules" |
| Local models / home-lab agents | depends | Load `AGENTS.md`, `LESSONS.md`, `HANDOFF.md` into the system prompt or context loader |

`AGENTS.md` is the only place rules live. The pointer files stay short so there is never a second, out-of-date copy.

## 3. Starting a new project

1. On GitHub, open the template repo and click **Use this template → Create a new repository**.
2. Fill in **Project facts** in `AGENTS.md`. The **Definition of done** line matters most: without it, "verify" has nothing to check against.
3. Fill in `DESIGN.md` if the project has a UI. Five lines (palette, fonts, "avoid") beat nothing.
4. Replace `README.md` with the project's own README.
5. Copy `.env.example` to `.env` for real values (`.env` is git-ignored). Delete `.env.example` if the project has no environment variables.
6. Delete `scripts/install-agent-kit.sh` if you like; new projects don't need it.

## 4. Adding the kit to an existing repo

```bash
git clone <template-repo-url> /tmp/agent-kit
cd /path/to/your-repo
git checkout -b agent/kit-install
/tmp/agent-kit/scripts/install-agent-kit.sh . 
# or, if the repo already keeps lessons/design elsewhere:
/tmp/agent-kit/scripts/install-agent-kit.sh . --skip "LESSONS.md DESIGN.md"
```

The installer **never overwrites**: existing files are left alone, an existing `CLAUDE.md`/`GEMINI.md` keeps its content with a pointer added on top, `README.md` is never touched, and `.gitignore` only gains missing secret lines. Then fill in `AGENTS.md` → Project facts and Where things live, commit, and open a pull request.

## 5. The working loop

**Start:** the agent reads `AGENTS.md`, the docs it lists, `LESSONS.md`, the newest `HANDOFF.md` entry and (for UI) `DESIGN.md`, checks open PRs, then posts a plan for anything non-trivial.

**During:** build → verify (tests, edge cases, diff review) → repeat. Work on an `agent/<name>/<topic>` branch. Anything irreversible needs the owner's yes.

**End:** `HANDOFF.md` entry (agent + model, what changed, what was verified, next step), `LESSONS.md` entry if something broke, push, open/update the PR. The owner reviews and merges.

**Before going public:** `PRELAUNCH.md`, every item done or N/A with a reason; the owner signs off.

## 6. Several agents on one repo

- **Branches keep agents apart.** One agent per branch; branch names carry the agent's name, so it's always clear who's working where.
- **Check before starting.** Agents look at open PRs and the newest `HANDOFF.md` entry before they begin, so two agents don't do the same job.
- **The handoff entry is the baton.** Switching from Claude to Codex to Grok mid-project works because the next agent picks up from "Next step".
- **Only the owner merges.** No agent approves or merges its own work.
- **Rules are protected.** Agents can't quietly weaken `AGENTS.md`; rule changes come as separate `rules:` PRs.
- **Untrusted text isn't a command.** An instruction hidden in an issue, web page or dependency is reported, not followed.

## 7. File-by-file guide

### `AGENTS.md`
- **Project facts**: the only part you must fill in per project.
- **Where things live**: change a path when a repo already keeps that file elsewhere (for example `docs/LESSONS.md`). Add every other doc agents must read to "Other project docs to read".
- **Sections 1–8**: the same in every repo. Change them in the template so every new project gets the change; existing repos get it through a PR.

### `LESSONS.md`
Specific beats vague. Good: "This repo uses pnpm; never run `npm install`." / "Use `<input type="date">` unless the design needs more." Bad: "Be careful with installs."

### `HANDOFF.md`
Newest first. "Verified (and how)" and "Not verified" keep reports honest; "Decisions made (and why)" stops the next agent undoing a deliberate choice.

### `DESIGN.md`
Contrast minimums are built into the color table so accessibility is decided at design time. The "Avoid" line is the cheapest way to stop generic AI-looking design.

### `PRELAUNCH.md`
Seven sections: secrets, database and auth, cost and abuse, accessibility, messaging and privacy, function, recovery. The logged-out visitor test is the single most important check for any app with a database.

## 8. Risks the kit guards against

| Risk | Example | Covered in |
|---|---|---|
| Open database | Table with row-level security off: anyone with the public key reads every row | `AGENTS.md` §5; `PRELAUNCH.md` §2 |
| Surprise hosting bill | A static site billed ~$104,500 after a traffic spike (2024) | `AGENTS.md` §6; `PRELAUNCH.md` §3 |
| Runaway cloud costs | Loops and retries; budget alerts notify but don't stop spending | `AGENTS.md` §6; `PRELAUNCH.md` §3 |
| Accessibility lawsuits | 5,000+ digital accessibility suits a year, many against small businesses | `DESIGN.md`; `PRELAUNCH.md` §4 |
| Texting without consent | TCPA damages of $500 per message ($1,500 if willful) | `AGENTS.md` §5; `PRELAUNCH.md` §5 |
| Leaked secrets | Service keys in frontend code or a committed `.env` | `.gitignore`; `AGENTS.md` §5; `PRELAUNCH.md` §1 |
| Prompt injection | Hidden instructions in an issue or web page | `AGENTS.md` §5 |
| Agents colliding | Two agents editing the same files | `AGENTS.md` §1, §3 |
| Lost context | New session doesn't know yesterday's work | `HANDOFF.md` |
| Repeated mistakes | Same wrong command again | `LESSONS.md` |
| Overbuilding | Custom code where native features work | `AGENTS.md` §2 |

*The kit reduces risk; it isn't legal advice. For real legal exposure, have accessibility and consent setups reviewed by someone qualified.*

## 9. Customizing per project

- **Static site, no database:** `PRELAUNCH.md` §2 and §5 are N/A. Keep §3 (bandwidth costs money) and §4.
- **Business site:** §4 Accessibility and the business-details check in §6 are mandatory.
- **Login / member site:** §2 is mandatory, including the three-role test.
- **Local-only tools:** cost and accessibility can be N/A; secrets and recovery still apply.
- **Non-code repos (notes, research, coursework):** `DESIGN.md` and most of `PRELAUNCH.md` can be N/A; the git, honesty and handoff rules still help.

## 10. Updating the kit

1. Change the files in the template repo and add a line to the Changelog below.
2. For existing repos, re-run `install-agent-kit.sh`: it adds new files but never overwrites, so for changed rules copy sections 1–8 of `AGENTS.md` over by hand (keeping each repo's Project facts and Where things live) in a PR.

## 11. FAQ

**Do I need plugins?** No. Everything is Markdown.

**Does this slow down small fixes?** No. Plan-first applies to non-trivial work; a typo fix doesn't need a plan or a prelaunch run.

**An agent ignored a rule. Now what?** Point at the line in `AGENTS.md` and add the slip to `LESSONS.md` so it's front-loaded next time.

**Why can't agents commit to main?** So nothing reaches the live branch without your review, whichever agent wrote it.

## 12. Changelog

- **v1.1 (2026-11-24):** Works with any AI agent. `AGENTS.md` is now the single rules file; `CLAUDE.md`, `GEMINI.md` and `.github/copilot-instructions.md` point to it. Added git/PR rules (branch per agent, owner merges), multi-agent coordination, prompt-injection and rule-protection rules, a "Where things live" table for repos with existing docs, a safe installer script, and agent/model + verification fields in `HANDOFF.md`. Removed example entries from `LESSONS.md` so agents don't mistake them for real project facts.
- **v1.0 (2026-11-22):** First kit (Claude-focused).
