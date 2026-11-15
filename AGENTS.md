# AGENTS.md

Instructions for agents working in this repository.

## What this repo is

A Markdown-only library of **75 agent skills** (`skills/<category>/<skill-name>/SKILL.md`), published as a snapshot of the owner's personal library. Most skills are ports of Daniel Miessler's Fabric patterns.

There is no build, test suite, lint config, or package manifest. The one executable artifact is **`scripts/check.py`** (stdlib-only), which validates README↔skills consistency — run it before finishing any change to skills or README; CI ([`.github/workflows/check.yml`](.github/workflows/check.yml)) runs it on PRs. Other files: `README.md`, `LICENSE`, `assets/` (README images).

## Invariants not obvious from files

- Frontmatter `name` must exactly equal the skill's folder name (true for all 75 today).
- Every skill is currently a **single `SKILL.md` file**; the format allows optional support files (`references/`, scripts), but none exist yet.
- The `skills/<category>/<skill>/` layout is the catalog format the [`skills` CLI](https://github.com/vercel-labs/skills) (`npx skills add gdellis/Agent-Skills`) discovers on. Don't flatten, re-nest, or rename folders.
- Eight fixed categories: `analysis` (19), `extraction` (16), `summarization` (10), `writing` (14), `learning` (7), `meta` (6), `research` (2), `tools` (1). New skills go into an existing one.

## SKILL.md format

- YAML frontmatter with exactly `name` and `description`, then a Markdown body.
- Dominant frontmatter style is block scalars (69/75 files): `name: |` / `description: |` with indented values. Match it.
- `description` is the routing trigger an agent reads to decide whether to load the skill. ≤1024 chars; most open with "Load this skill when …" (63 skills) or "Use this skill when …" — keep that phrasing.
- Common body sections, in order (not all required): `## Identity and Purpose` (or `## Identity`), `## Steps`, `## Output` / `## Output Sections`, `## Output Instructions`.
- When creating or editing skills, follow the repo's own authority: [`skills/meta/skill-creator/SKILL.md`](skills/meta/skill-creator/SKILL.md).

## README must stay in sync (the easy thing to forget)

`README.md` is a hand-maintained catalog. When adding, removing, renaming, or re-describing a skill, update all of:

1. **Count + date line** near the top: "(75 skills, synced November 14, 2026)".
2. **The per-category table** under the matching `### \`<category>/\` (N skills)` heading — update the row *and* the `N` count. Rows are alphabetical; each description is a second-person rewrite of the frontmatter description ("Load this skill when the user wants…" → "Load this when you want…"), **compressed — never truncated — to a complete sentence of ≤160 chars** (drop enumerated items rather than cutting mid-list; never end a cell with `...`).
3. **The Structure table** (8 category rows) only if a category is added or its purpose changes.

Run **`python3 scripts/check.py`** — it enforces this whole contract (counts, ordering, links, cell lengths, `name` == folder); CI runs it on PRs.

## Conventions

- Folder names: kebab-case, verb-led (`extract-`, `summarize-`, `analyze-`, `write-`, `create-`, `improve-`, `explain-`). Pick the category whose verb family fits.
- Portability: skills are plain Markdown that must work in any Agent-Skills-compatible agent and most chat assistants. Don't couple skills to one agent's features. Sole exception: `tools/youtube-transcript`, which assumes a shell + Python.
- Git history: changes land via PRs with short imperative subjects ("Scrub …", "Remove …", "Add …"). Recent work has been pruning/normalizing the skill set and cleaning up the README.

## Quick check before finishing a skill change

- `python3 scripts/check.py` passes (it covers everything below).
- File is at `skills/<category>/<name>/SKILL.md`; frontmatter `name` == folder name.
- YAML frontmatter parses; description present, ≤1024 chars, says when to load it.
- README: count/date line, per-category table row + heading count, alphabetical order — all updated.
