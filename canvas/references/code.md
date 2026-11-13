# Code Canvases

Optional extra guidance for `code`.

- Use `code` for substantial non-React source artifacts the user will keep or iterate on.
- Use `language` when you know it.
- The canvas is editable code only. There is no execution and no live preview.
- Keep the output as the source artifact itself, not a markdown wrapper around the source.
- When editing an existing code Canvas, patch the specific import, function,
  class, block, or constant with `edit`; do not rewrite the full
  `CANVAS.md` unless most of the source must change.
