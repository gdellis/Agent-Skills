# Document Canvases

Optional extra guidance for `text/markdown`.

- The user edits the document in a rich markdown editor, not a code editor.
- Headings, lists, blockquotes, fenced code blocks, GFM tables, and math work well.
- Raw HTML is not the main authoring path.
- If SVG illustrations are useful, use fenced `svg` code blocks with triple
  backticks. Put only the `<svg>...</svg>` markup inside the fence. Do not
  insert raw inline SVG outside a fenced `svg` block. Keep SVG static and
  self-contained: do not use scripts, event handler attributes,
  `<foreignObject>`, external URLs, external images, external fonts, or remote
  `href`/`xlink:href` references.
- Markdown image URLs are rewritten to placeholder images, so do not design the document around embedded images.
- Raw export is `.md`, and PDF export is available. Simple semantic markdown is the safest export path.
- When editing an existing document Canvas, patch only the affected heading,
  paragraph, list, table, or section with `edit`. Avoid rewriting the
  entire document unless the user asked for a full rewrite or restructure.
