# World Thermostat

**A nightly world-tension briefing from Not-So Oddly Connected.**

World Thermostat is written each night by Doomsday, one of the founder's bots. Each briefing rates how "hot" the world feels that night, names the hotspots, fact-checks claims made by public commentators, gives one line on the home front and one practical prep tip.

This repository holds **content only**: the posts and their index, plus one small read-only checker (see [Automatic content check](#automatic-content-check)). The page runs no code from here. It is the source the World Thermostat page reads from:

> **Live page:** https://the-lab.notsooddlyconnected.com/conversations/world-thermostat/

The page is a sibling of the two other Conversations pages on The Lab. The three pages link to each other in their header as **Night**, **Dawn** and **World**.

> Every briefing is an **open-source summary, not advice.** It is not news, legal, financial, medical or emergency guidance.

---

## Contents

1. [How it works](#how-it-works)
2. [Repository layout](#repository-layout)
3. [The nightly upload (contract)](#the-nightly-upload-contract)
4. [Post file format](#post-file-format)
5. [`index.json` format](#indexjson-format)
6. [Commit message format](#commit-message-format)
7. [Dates and time zone](#dates-and-time-zone)
8. [Skipped nights, corrections and removals](#skipped-nights-corrections-and-removals)
9. [What must never be in this repo](#what-must-never-be-in-this-repo)
10. [Automatic content check](#automatic-content-check) · [Pre-commit checklist](#pre-commit-checklist)
11. [Troubleshooting](#troubleshooting)
12. [Who does what](#who-does-what)
13. [License](#license)

---

## How it works

```
Doomsday writes the briefing (already scrubbed of anything personal)
        │
        ▼
~3:00 AM ET  Gigi commits 2 files to `main` in this repo, as 1 commit:
             posts/YYYY-MM-DD.md   +   the updated index.json
        │
        ▼
This repo is public. The World Thermostat page on The Lab fetches
index.json and the newest post straight from GitHub when someone opens it.
        │
        ▼
The new briefing shows on the live page, usually within about 5 minutes.
No rebuild or deploy is needed, and nobody has to touch The Lab's code.
```

Key points:

- **Nothing else needs to happen.** No build, deploy, token or manual step on The Lab side. The commit here is the publish.
- **Because this repo is public, everything committed here is public at once,** including the commit history. Treat every commit as published.
- GitHub caches raw files for a few minutes, so a new post can take up to about 5 minutes to show.
- If a night's post is missing, the page shows the most recent post with its date. It never shows an error.
- Each post is shown as plain formatted text. The page escapes everything, so raw HTML, scripts, embeds and iframes in a post **do not render.** Write plain Markdown only.

---

## Repository layout

```
world-thermostat/
├── posts/
│   ├── 2026-11-20.md      # one file per night, named by the Eastern-time date of the night it covers
│   ├── 2026-11-21.md
│   └── ...
├── index.json             # newest-first list of every published post
├── tools/check_content.py # read-only check of index.json and posts/ (added Nov 24, 2026)
├── .github/               # the check workflow and a monthly Dependabot check for its Actions
├── README.md              # this file
└── LICENSE                # All rights reserved
```

Don't add any other files or folders (images, scripts, workflows, drafts) without the founder's OK. The checker, its workflow and the agent-kit files (`AGENTS.md` and friends) were approved on Nov 24, 2026. `posts/.gitkeep` only exists so the empty folder is tracked; leave it or delete it, it doesn't matter.

---

## The nightly upload (contract)

| Item | Rule |
|---|---|
| **Who** | Gigi (GitHub user `n-socnet`) |
| **When** | About 3:00 AM ET, after the night the briefing covers |
| **Branch** | `main`, committed directly. No PR is needed for nightly posts |
| **Files** | Exactly 2: the new `posts/YYYY-MM-DD.md` and the updated `index.json` |
| **Commits** | Exactly 1 commit containing both files |
| **Message** | `post: YYYY-MM-DD (temp)`. See [Commit message format](#commit-message-format) |
| **First post** | `posts/2026-11-20.md` (Friday night, Nov 20, 2026), uploaded about 3 AM on Saturday, Nov 21, 2026 |

Steps:

1. Save Doomsday's briefing as `posts/YYYY-MM-DD.md`, using the date of the **night it covers** (see [Dates](#dates-and-time-zone)).
2. Open `index.json` and add the new entry at the **top** of the list.
3. Check the [pre-commit checklist](#pre-commit-checklist).
4. Commit both files together with the message `post: YYYY-MM-DD (temp)`.

---

## Post file format

Each post is a Markdown file with front matter at the top. Use this layout:

```markdown
---
title: "World Thermostat, 2026-11-20"
date: 2026-11-20
temp: simmering
---

# World Thermostat, 2026-11-20

## World temp: Simmering

### Hotspots
- **Region or topic.** One or two sentences on what is happening and why it matters.
- **Region or topic.** ...

### Fact-checks
- **Claim:** What a public commentator said, attributed to them by name or show.
  **Check:** What the public record shows, with the source named (for example "per Reuters" or "per the agency's own release").
  **Verdict:** Accurate / Misleading / False / Unproven.

### Home front
One line on how tonight's picture touches everyday life at home.

### Prep tip
One practical, low-cost preparedness tip.

---

*Open-source summary, not advice.*
```

### Front matter fields

| Field | Required | Rule |
|---|---|---|
| `title` | yes | Exactly `World Thermostat, YYYY-MM-DD`, in quotes |
| `date` | yes | `YYYY-MM-DD`. Must match the file name and the `index.json` entry |
| `temp` | yes | Exactly one of `calm`, `simmering`, `hot`, `boiling`, all lowercase |

The `temp` value sets the badge colour on the page. Any other value shows as an unknown, neutral badge, so spell it exactly.

| `temp` | Meaning (Doomsday's scale) | Badge colour |
|---|---|---|
| `calm` | Quiet night, no major escalation | teal |
| `simmering` | Ongoing tension, nothing breaking | amber |
| `hot` | Real escalation in one or more hotspots | orange |
| `boiling` | Severe, fast-moving events | red |

### Body rules

- **Plain Markdown only:** headings (`#` to `###`), paragraphs, bold, italics, bullet and numbered lists, links, block quotes and horizontal rules (`---`).
- **No raw HTML, images, embeds, tables or code blocks** in posts. They won't render.
- Links should be full `https://` URLs. Other link types are shown as plain text.
- **The last line must be the disclaimer:** `*Open-source summary, not advice.*` The page also shows the disclaimer on every view, but each file has to carry it as well.
- Keep it public-ready. See [What must never be in this repo](#what-must-never-be-in-this-repo).

---

## `index.json` format

`index.json` is a JSON array, **newest first**. One object per published post:

```json
[
  {
    "date": "2026-11-21",
    "title": "World Thermostat, 2026-11-21",
    "temp": "calm",
    "path": "posts/2026-11-21.md"
  },
  {
    "date": "2026-11-20",
    "title": "World Thermostat, 2026-11-20",
    "temp": "simmering",
    "path": "posts/2026-11-20.md"
  }
]
```

| Key | Rule |
|---|---|
| `date` | `YYYY-MM-DD`, same as the post's front matter and file name |
| `title` | Same as the post's front matter `title` |
| `temp` | Same as the post's front matter `temp` |
| `path` | `posts/YYYY-MM-DD.md`, exactly matching the real file name |

Rules:

- The file must stay **valid JSON**: double quotes, commas between entries, **no comma after the last entry**, and square brackets around the whole list.
- **Newest entry at the top.** Never reorder older entries.
- **One entry per date.** No duplicates.
- Every entry's `path` must point to a file that exists in `posts/`.
- Before the first post, the file is an empty list: `[]`.

If `index.json` is broken (invalid JSON), the page keeps showing the last good copy it saved on that visitor's device and shows nothing new until the file is fixed. A broken index is the most likely way a night gets missed, so check it before committing.

---

## Commit message format

```
post: YYYY-MM-DD (temp)
```

Examples:

```
post: 2026-11-20 (simmering)
post: 2026-11-21 (calm)
```

For anything other than a nightly post, use one of these:

| Change | Message |
|---|---|
| Fix a typo or fact in a published post | `fix: YYYY-MM-DD <short reason>` |
| Remove a post | `remove: YYYY-MM-DD <short reason>` |
| Edit README or LICENSE | Open a PR. The founder reviews and merges it |

---

## Dates and time zone

- All dates are **Eastern Time (America/New_York)**.
- A post is named for the **night it covers**, not the moment it is uploaded. Friday night's briefing is uploaded about 3 AM Saturday and is still named `2026-11-20.md`.
- The date appears in 4 places, and all 4 must match: the file name, front matter `date`, front matter `title`, and the `index.json` entry.

---

## Skipped nights, corrections and removals

- **Skipped night:** if there's no briefing, commit nothing. **Don't backfill** a missed night later. The page simply shows the most recent post.
- **Correction:** edit the post file. If `title` or `temp` changes, update the matching `index.json` entry in the same commit. Use the `fix:` message.
- **Removal:** delete the post file **and** its `index.json` entry in one commit, using the `remove:` message. The old version still exists in the public commit history. If something truly must be scrubbed from history, stop and tell the founder; don't try to rewrite history yourself.

---

## What must never be in this repo

This repo is **public**. Never commit:

- personal information about the founder, family, friends or anyone private: names, addresses, schedules, locations, phone numbers, emails, photos;
- details of the founder's own home, supplies, routes or prep plans (the home-front line and prep tip stay **general**);
- secrets of any kind: tokens, keys, passwords, backup files, export links, internal URLs;
- names of private repositories or internal-only projects;
- drafts, notes or anything Doomsday wrote that isn't the finished, scrubbed briefing.

If something like this gets committed by mistake, don't push more commits trying to hide it. Tell the founder right away.

---

## Automatic content check

Added Nov 24, 2026 (Founder OK). `.github/workflows/checks.yml` runs `python3 tools/check_content.py` on every push, including the nightly post commit. It checks the rules above: `index.json` is valid JSON, newest first, one entry per date, with the four keys; every `path` exists; every post's front matter `date`, `title` and `temp` match its file name and index entry; `temp` is `calm`, `simmering`, `hot` or `boiling`; the last line is the disclaimer; no raw HTML, images, tables or code blocks; and no post file is missing from the index.

The check never changes or blocks anything: the post is already live when it runs. A red cross on the commit lists which rule to fix in the next commit. To run it before committing: `python3 tools/check_content.py` from the repository root.

---

## Pre-commit checklist

- [ ] File is named `posts/YYYY-MM-DD.md` with the date of the night it covers (Eastern Time).
- [ ] Front matter has `title`, `date` and `temp`, and `temp` is exactly `calm`, `simmering`, `hot` or `boiling`.
- [ ] Title reads `World Thermostat, YYYY-MM-DD`.
- [ ] Post ends with `*Open-source summary, not advice.*`
- [ ] No raw HTML, images, tables, code blocks or personal details.
- [ ] New entry is at the **top** of `index.json`, with matching `date`, `title`, `temp` and `path`.
- [ ] `index.json` is valid JSON (no trailing comma).
- [ ] Both files are in **one** commit, message `post: YYYY-MM-DD (temp)`.

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| New post isn't on the page yet | GitHub's raw-file cache | Wait about 5 minutes and reload |
| Page still shows yesterday after 10+ minutes | `index.json` not updated, broken JSON, or wrong `path` | Check `index.json` against this README and commit a fix |
| Badge is neutral or the wrong colour | `temp` misspelled or capitalised | Use exactly `calm`, `simmering`, `hot` or `boiling` |
| A heading or list shows oddly | Unsupported Markdown | Stick to the elements listed in [Body rules](#body-rules) |
| Something private was committed | Mistake | Tell the founder right away. Don't try to rewrite history |

---

## Who does what

| Who | Role |
|---|---|
| **Doomsday** (founder's bot) | Writes each briefing and scrubs it of anything personal |
| **Gigi** (`n-socnet`) | Uploads the nightly post plus `index.json` at about 3 AM ET |
| **Clyde** (Claude) | Built the World Thermostat page on The Lab and maintains this README via PRs. Never merges |
| **Founder** (Michael) | Owns the project. Reviews and merges every PR. Approves every deploy |

---

## License

Copyright (c) 2026 Michael Atchley / Not-So Oddly Connected. **All rights reserved.** See [LICENSE](LICENSE).
