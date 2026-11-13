# Slides Canvases

Optional extra guidance for `slides`.

- Slides use Marp markdown.
- Separate slides with `---`.
- The Canvas frontmatter supports only `name`, `title`, `type`, `language`, and `entryPoint`.
- Set deck-wide Marp options with HTML comment directives after the Canvas frontmatter, such as `<!-- theme: beam -->` and `<!-- paginate: true -->`.
- Useful slide-local directives: `_class`, `_header`, `_footer`, `_paginate`, `_backgroundColor`, `_color`.
- Raw HTML is enabled, so small HTML snippets are fine for columns or KPI blocks.
- Images are not supported in this renderer. Do not use markdown images or image-based slide designs.
- PowerPoint export is basic, text only.
- When editing an existing slide Canvas, use `edit` for the specific
  slide, heading, bullet list, directive, or speaker-facing content that
  changed. Do not rewrite the whole deck for one-slide edits.

Good default:

```markdown
---
name: example-deck
title: "Example Deck"
type: slides
---

<!-- theme: beam -->
<!-- paginate: true -->
<!-- _class: lead -->

# Deck Title

## Short subtitle

---

# Slide Title

- Point one
- Point two
- Point three
```

## Theme Notes

- `default`: the standard renderer theme.
- `beam`: supports `<!-- _class: title -->` for stronger title slides and `<!-- _class: tinytext -->` for dense appendix or references slides.
