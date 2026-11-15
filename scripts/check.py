#!/usr/bin/env python3
"""Consistency checks for the Agent-Skills repo. Stdlib-only; exits 1 on any failure.

Verifies the sync contract between skills/ and README.md:
  - every skill is skills/<category>/<name>/SKILL.md with frontmatter name == folder
  - frontmatter has a non-empty description of at most 1024 chars
  - the README intro line "(N skills, synced ...)" matches the real count
  - the Structure table lists exactly the category directories on disk
  - each category has a "### `<category>/` (N skills)" heading matching its table
  - table rows are alphabetical, links resolve, cells are <=160 chars,
    truncated cells end with "..." (never the single-char "…")
  - every skill has exactly one README row and vice versa
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
failures = []
passes = 0


def check(ok, label, detail=""):
    global passes
    if ok:
        passes += 1
    else:
        print(f"[FAIL] {label}" + (f" — {detail}" if detail else ""))
        failures.append(label if not detail else f"{label}: {detail}")


def frontmatter(path):
    """Return (name, description) from a SKILL.md, or None if unparseable."""
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        return None
    name, desc, cur = None, None, None
    for line in lines[1:]:
        if line == "---":
            break
        m = re.match(r"^(name|description):\s*(.*)$", line)
        if m:
            cur, val = m.group(1), m.group(2).strip()
            if val in ("|", ">"):
                if cur == "name":
                    name = ""
                else:
                    desc = ""
                continue
            val = val.strip("\"'")
            if cur == "name":
                name = val
            else:
                desc = val
            cur = None
            continue
        if cur and (line.startswith(" ") or line == ""):
            if cur == "name":
                name = ((name or "") + " " + line.strip()).strip()
            else:
                desc = ((desc or "") + " " + line.strip()).strip()
        else:
            cur = None
    return (name, desc) if name is not None else None


skills = sorted(ROOT.glob("skills/*/*/SKILL.md"))
skill_dirs = [p.parent for p in skills]
categories = sorted({d.parent.name for d in skill_dirs})

# --- SKILL.md files ---
for p in skills:
    rel = p.relative_to(ROOT)
    fm = frontmatter(p)
    check(fm is not None, f"{rel}: frontmatter parses with a name")
    if not fm:
        continue
    name, desc = fm
    check(name == p.parent.name, f"{rel}: frontmatter name matches folder", f"name={name!r}")
    check(bool(desc), f"{rel}: description present")
    check(desc is not None and len(desc) <= 1024, f"{rel}: description <= 1024 chars",
          f"{len(desc or '')} chars")

# --- README ---
readme_path = ROOT / "README.md"
text = readme_path.read_text(encoding="utf-8")
lines = text.splitlines()

m = re.search(r"\((\d+) skills, synced [A-Z][a-z]+ \d{1,2}, \d{4}\)", text)
check(m is not None, "README intro has '(N skills, synced <date>)'")
if m:
    check(int(m.group(1)) == len(skills), "README skill count matches disk",
          f"README says {m.group(1)}, disk has {len(skills)}")

rows = [l for l in lines if l.startswith("| [`")]
cat_rows, skill_rows = [], []
for r in rows:
    m = re.match(r"^\| \[`([a-z]+)/`\]\(\./skills/[a-z]+/\) \| (.+?) \|$", r)
    if m:
        cat_rows.append(m.groups())
        continue
    m = re.match(r"^\| \[`([a-z0-9-]+)`\]\(\./skills/([a-z]+)/[a-z0-9-]+/\) \| (.+?) \|$", r)
    if m:
        skill_rows.append(m.groups())
    else:
        check(False, "README table row matches expected format", r[:80])

check(sorted(c for c, _ in cat_rows) == categories,
      "Structure table lists exactly the category dirs",
      f"table={sorted(c for c, _ in cat_rows)} disk={categories}")

heading_re = re.compile(r"^### `([a-z]+)/` \((\d+) skills\)$")
headings = [m.groups() for l in lines if (m := heading_re.match(l))]
check(sorted(c for c, _ in headings) == categories,
      "every category has a '### `<category>/` (N skills)' heading")
for cat, n in headings:
    on_disk = sum(1 for d in skill_dirs if d.parent.name == cat)
    check(int(n) == on_disk, f"heading count for `{cat}/` matches disk", f"{n} vs {on_disk}")

per_cat = {c: [] for c in categories}
for name, cat, _cell in skill_rows:
    per_cat.setdefault(cat, []).append(name)
for cat, n in headings:
    check(len(per_cat.get(cat, [])) == int(n), f"`{cat}/` table rows match heading count",
          f"{len(per_cat.get(cat, []))} rows")

seen = set()
for name, cat, cell in skill_rows:
    check(name not in seen, f"README row for `{name}` appears once")
    seen.add(name)
    check((ROOT / "skills" / cat / name / "SKILL.md").exists(),
          f"README link `{cat}/{name}` resolves")
    check(len(cell) <= 160, f"README cell `{name}` <= 160 chars", f"{len(cell)} chars")
    check(not cell.endswith("…"), f"README cell `{name}` uses '...' not '…' when truncated")
for d in skill_dirs:
    check((d.parent.name, d.name) in {(c, n) for n, c, _ in skill_rows},
          f"skill `{d.parent.name}/{d.name}` has a README row")

for cat, names in per_cat.items():
    check(names == sorted(names, key=str.lower), f"`{cat}/` rows are alphabetical")

print(f"{passes} checks passed, {len(failures)} failed")
sys.exit(1 if failures else 0)
