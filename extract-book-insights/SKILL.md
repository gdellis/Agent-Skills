---
name: |
  extract-book-insights
description: |
  Load this skill when the user gives a book name and wants its most important content pulled out — 50-100 of its most surprising and interesting ideas, or 50-100 of its most practical instructive recommendations.
---

# Extract Book Insights

You take a book name as input and output a full summary of the book's most important content, using the mode requested.

## Mode 1 — Ideas (default)

- Scour your memory for everything you know about this book.
- Extract 50 to 100 of the most surprising, insightful, and/or interesting ideas into a section called IDEAS:. If there are less than 50, collect all of them; extract at least 20.
- Order the ideas by the most interesting, surprising, and insightful first.
- Limit each bullet to a maximum of 20 words.

## Mode 2 — Recommendations

- Scour your memory for everything you know about this book.
- Extract 50 to 100 of the most practical RECOMMENDATIONS into a section called RECOMMENDATIONS:. If there are less than 50, collect all of them; extract at least 20.
- Order by the most powerful and important first.
- Write all recommendations as instructive advice, not abstract ideas.
- Limit each bullet to a maximum of 20 words.

## Output Instructions

- Only output Markdown.
- Do not give warnings or notes; only output the requested sections.
- Use bulleted lists, not numbered lists.
- Do not repeat ideas, and vary the wording — don't restate the same idea with different phrasing.
