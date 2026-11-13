---
name: "canvas"
description: "Use this skill when the user likely wants a separately rendered artifact instead of a chat reply, explicitly mentions a canvas, wants to view or edit a supported existing artifact, asks for a code example, create/build an app or other artifact work with a compatible Canvas type. Do not use Canvas for a Personal Knowledge request unless the user separately asks for a Canvas. A Canvas is a folder with a special file structure, not a tool. Common canvas outputs include documents, code files, React UIs, HTML pages, slides, diagrams, SVGs, standalone tables, spreadsheet/XLSX workbooks. Common trigger verbs include make, create, write, rewrite, edit, draft, compose, build, code, generate, prepare, and document. Do not use a Canvas when the most appropriate answer format is a list, a list of action items, or a list of sequential steps: answer it in chat as a plain Markdown list, or, when the user explicitly asks for a checklist or to-do list or wants to tick items off, load the `rich-ui` skill and render the inline `Checklist` component. Always read this skill before producing code examples or app-like artifacts so you can decide whether to use canvas, whether to create or update one, which mode to choose, and which optional file to read next. Also read this file before making any edits to files under /home/user/canvases/. For existing Canvas edits, prefer targeted `edit` calls over full-file `write_file` rewrites."
---
# Canvas Files

A Canvas is a durable user-facing artifact represented by a Canvas File at `/home/user/canvases/{name}/CANVAS.md`. That path is only an internal editing target.

Use chat only for a brief acknowledgment or next step. Do not paste the full Canvas body back into chat. In your final answer, never mention, quote, or Markdown-link the Canvas File path. Refer to the artifact as "the canvas" or by its title instead.

## Use Canvas

Use a Canvas when the user wants a deliverable they will likely inspect, edit, preview, copy, export, or iterate on:

- Documents
- Code files
- React UIs or HTML pages
- Slides
- Mermaid diagrams or SVGs
- Standalone tables
- Spreadsheet/XLSX workbooks

When image generation is available, use it instead of a Canvas when the user wants a picture: a drawing, painting, illustration, photo-like scene, or a graphic meant to be used as a picture, such as a logo, poster, card, sticker, or cover, or wants an uploaded image changed. Draw it as an SVG or HTML Canvas only when the user asks for SVG, vector, or code output, or an editable or interactive layout. Charts, diagrams, slide decks, and tables stay in Canvas.

Stay in chat for short answers, explanations, tiny inline snippets, lookup questions, a list, a list of action items, or a list of sequential steps (plain Markdown lists by default, the inline `Checklist` component via `renderComponent` only for an explicitly requested checklist or completion tracking, never as a Canvas), or ambiguous requests where the artifact shape is still unclear.

## Canvas As A File Boundary

The user cannot browse your filesystem by default. Most Canvas types contain content authored directly in Canvas files. Only `spreadsheet` for XLSX is a file-backed boundary in this context.

When an existing XLSX file is already available, place a copy unchanged at the entry point required by its Canvas type and add only the Canvas metadata. Never move the source file or manually reproduce it by reading and rewriting its contents. For a new file-backed deliverable, write the final file directly to its Canvas entry point when practical. Reuse its existing Canvas if it already has one. Surfacing an unchanged file does not require an authoring workflow.

If no file-backed Canvas type matches the file extension, explain that the format cannot currently be surfaced in Canvas. Do not invent a download path or silently convert or rebuild the file as a different Canvas type.

## Download Or Export

Use or point to the Canvas export/download control when it meets the request.

Writing a file to an arbitrary filesystem path does not create a user-visible download. Do not invent delivery paths such as `/home/user/downloads` or `/home/user/sandbox`. If the user wants changes to the Canvas itself, update the Canvas.

## File Format

Most Canvas types live in exactly one file:

```text
/home/user/canvases/{name}/CANVAS.md
```

The folder name and Canvas Frontmatter `name` must match exactly. Canvas renames and deletion are not supported.

Default Canvas directories contain only `CANVAS.md`. Spreadsheet Canvas directories contain exactly `CANVAS.md` plus the `.xlsx` workbook named by `entryPoint` (usually `workbook.xlsx`). Do not add sibling files, nested files, generated assets, or helper modules inside a Canvas directory unless the selected Canvas type explicitly allows them.

The frontmatter fields are:

- `name`: stable chat-scoped identifier, required.
- `title`: displayed title, optional. Always wrap its value in double quotes.
- `type`: required Canvas type.
- `language`: optional and recommended for `type: code`; ignored for other types.
- `entryPoint`: required only for `type: spreadsheet`; set it to a safe `.xlsx` filename such as `workbook.xlsx`.

`description` is not part of the Canvas File format.

For source-code Canvas types, everything beneath the frontmatter must be only the raw code. For Spreadsheet Canvas, keep the `CANVAS.md` body empty and write the XLSX workbook bytes in the `.xlsx` file named by `entryPoint`. Do not add markdown fences, headings, explanations, comments about the answer, or any other formatting wrapper unless that text is part of the code itself.

## Minimal Template

Make sure to start every Canvas File with the YAML frontmatter block at the very first character of the file. Do not write a title, heading, blank line, or any other content before its opening `---`.

```md
---
name: example-canvas
title: "Example Canvas"
type: text/markdown
---

# Example Canvas

Content goes here.
```


For Spreadsheet Canvas, use exactly these frontmatter fields, including a concise user-facing `title`. Do not write `canvasType`.

```md
---
name: sales-forecast
title: Sales Forecast
type: spreadsheet
entryPoint: workbook.xlsx
---
```



## Supported Types

- `text/markdown`: prose-first documents shown in the rich markdown editor.
  Before writing any fenced Mermaid block inside a Markdown Canvas, read
  `skills/canvas/references/diagrams.md`.
- `code`: source artifacts with editable code only. Set `language` when known.
- `react`: interactive UI rendered in the React canvas runtime. Load the `canvas-react` skill first.
- `text/html`: self-contained browser page rendered in an iframe. Load the `references/html.md` first.
- `slides`: Marp markdown slide deck. Use `---` between slides.
- `mermaid`: raw Mermaid source. Before writing it, read
  `skills/canvas/references/diagrams.md`. Do not wrap it in fences.
- `image/svg+xml`: raw SVG. Start with a real `<svg>` element.
- `table`: a standalone well-formed Markdown table. Use one header row, one separator row, then data rows. Keep every row rectangular: the separator row and each data row must have exactly the same number of cells as the header row. Do not add prose before or after the table.
- `spreadsheet`: a real XLSX workbook. Use `type: spreadsheet`, not `type: table`, CSV, JSON, or Markdown table. To surface an existing workbook unchanged, copy it to the Canvas entry point and write its metadata; never move or recreate the source, and do not load `data-analysis`. Use `data-analysis` only to create, modify, inspect, or verify workbook content.

## Create Or Edit

- To create a Canvas, choose a concise kebab-case `name` and prepare the content required by its type. Write `/home/user/canvases/{name}/CANVAS.md` with valid frontmatter and any required body after the artifact files are ready.
- To edit an existing Canvas, read its `CANVAS.md`, preserve user edits, and keep the same path and `name`.
- For existing Canvas edits, `edit` is the default tool. Use it for section, paragraph, component, import, style, copy, table row, slide, diagram edge, or other localized changes.
- Before calling `edit`, read the current file and choose the smallest exact text span to replace that is unique and stable. Include only enough surrounding lines to disambiguate the target.
- Prefer several small `edit` blocks over one large replacement. If a replacement fails, reread the file and retry with a corrected exact block instead of immediately falling back to `write_file`.
- Do not recreate or overwrite the full Canvas File for a localized edit, even if the file is short.
- Use `write_file` with the full Canvas File when creating a new Canvas, replacing most of the artifact, recovering invalid structure, or when the user explicitly asks for a complete rewrite.
- If the request is clearly artifact-shaped but the user did not say "Canvas", you can still create one.

## Optional References

- `skills/canvas/references/code.md`: extra guidance for non-React code Canvases.
- `skills/canvas/references/html.md`: mandatory guidance for HTML Canvases.
- `skills/canvas/references/documents.md`: extra guidance for markdown documents.
- `skills/canvas/references/slides.md`: extra guidance for Marp decks.
- `skills/canvas/references/diagrams.md`: mandatory guidance for any Mermaid
  output, including Mermaid blocks inside Markdown, plus extra SVG guidance.
- `skills/canvas/references/table.md`: extra guidance for standalone tables.

Do not load every file. Pick at most one extra path unless the task truly needs more.
For a Markdown document containing Mermaid, pick
`skills/canvas/references/diagrams.md`; it includes the Markdown embedding
rules.