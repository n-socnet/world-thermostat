#!/usr/bin/env python3
"""Check index.json and posts/ against the rules in README.md ("Post file format" and "index.json format").

Reads files only. Never changes a file and never uses the network. Run from the repository root:
    python3 tools/check_content.py
Exit code 0 = everything passes; 1 = at least one rule is broken (each one is listed).
GitHub runs this on every push and pull request (.github/workflows/checks.yml). A red cross does not stop a post from
going live; it tells you which rule to fix in the next commit.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPS = {"calm", "simmering", "hot", "boiling"}
DISCLAIMER = "*Open-source summary, not advice.*"
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
problems = []


def bad(msg):
    problems.append(msg)


def front_matter(text, name):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        bad(f"{name}: no front matter block (--- ... ---) at the top")
        return {}
    fields = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fields[k.strip()] = v.strip().strip('"')
    return fields


def check_post(name, entry=None):
    path = os.path.join(ROOT, "posts", name)
    with open(path, encoding="utf-8") as f:
        text = f.read().replace("\r\n", "\n")
    day = name[:-3]
    fm = front_matter(text, name)
    if fm.get("date") != day:
        bad(f"{name}: front matter date is {fm.get('date')!r}, file name says {day}")
    if fm.get("title") != f"World Thermostat, {day}":
        bad(f"{name}: title must be exactly 'World Thermostat, {day}' (found {fm.get('title')!r})")
    if fm.get("temp") not in TEMPS:
        bad(f"{name}: temp must be one of calm, simmering, hot, boiling (found {fm.get('temp')!r})")
    lines = [l for l in text.strip().splitlines() if l.strip()]
    if not lines or lines[-1].strip() != DISCLAIMER:
        bad(f"{name}: the last line must be {DISCLAIMER}")
    body = text.split("\n---\n", 1)[-1]
    if "```" in body:
        bad(f"{name}: code blocks are not allowed in posts")
    if re.search(r"<\s*/?\s*[a-zA-Z][^>]*>", body):
        bad(f"{name}: raw HTML is not allowed in posts")
    if re.search(r"!\[[^\]]*\]\(", body):
        bad(f"{name}: images are not allowed in posts")
    if re.search(r"^\s*\|.*\|\s*$", body, re.M):
        bad(f"{name}: tables are not allowed in posts")
    if entry:
        for key in ("title", "temp"):
            if entry.get(key) != fm.get(key):
                bad(f"index.json entry {day}: {key} {entry.get(key)!r} does not match the post ({fm.get(key)!r})")


def main():
    try:
        with open(os.path.join(ROOT, "index.json"), encoding="utf-8") as f:
            index = json.load(f)
    except (OSError, ValueError) as e:
        print(f"FAIL  index.json is not valid JSON: {e}")
        return 1
    if not isinstance(index, list):
        bad("index.json must be a list ([ ... ])")
        index = []
    posts = sorted(n for n in os.listdir(os.path.join(ROOT, "posts")) if n.endswith(".md"))
    seen, previous = set(), None
    for i, e in enumerate(index):
        if not isinstance(e, dict):
            bad(f"index.json item {i + 1} is not an object")
            continue
        day = e.get("date", "")
        if set(e) != {"date", "title", "temp", "path"}:
            bad(f"index.json entry {day or i + 1}: keys must be date, title, temp, path (found {', '.join(sorted(e))})")
        if not DATE.match(day):
            bad(f"index.json item {i + 1}: date {day!r} is not YYYY-MM-DD")
            continue
        if day in seen:
            bad(f"index.json: {day} appears more than once")
        seen.add(day)
        if previous and day >= previous:
            bad(f"index.json: {day} is below {previous}; newest must be first")
        previous = day
        if e.get("path") != f"posts/{day}.md":
            bad(f"index.json entry {day}: path must be posts/{day}.md (found {e.get('path')!r})")
        elif f"{day}.md" not in posts:
            bad(f"index.json entry {day}: {e['path']} does not exist")
        else:
            check_post(f"{day}.md", e)
    for name in posts:
        if not DATE.match(name[:-3]):
            bad(f"posts/{name}: file name must be YYYY-MM-DD.md")
        elif name[:-3] not in seen:
            bad(f"posts/{name} has no entry in index.json, so the page will never show it")
            check_post(name)
    for p in problems:
        print("FAIL  " + p)
    print(f"{len(index)} index entries, {len(posts)} posts, {len(problems)} problem(s).")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
