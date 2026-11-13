# Table Canvases

Optional extra guidance for `table`.

- Write a single standalone well-formed Markdown table as the canvas content.
- If the user asks for an editable Spreadsheet Canvas or an XLSX workbook, use `type: "spreadsheet"` instead of `type: "table"`.
- Use `type: "table"` only for an explicitly requested standalone editable table or CSV with at most 50 data rows.
- A Table Canvas is authored Markdown, not a file-backed boundary. Do not use it to surface an existing CSV unchanged.
- For larger CSVs or datasets, use computation tools to create the complete file and surface it through Artifacts. Writing every Markdown cell directly is inefficient and error-prone.
- For explicitly requested CSV, TSV, or other file exports, preserve the requested format and schema through the shared file-delivery route; use the table export control only when it satisfies that request.
- Do not wrap it in code fences.
- Do not add prose before or after the table.
- Use one header row, one separator row, then data rows.
- The separator row must contain exactly one separator cell per header cell, using `---`, `:---`, `---:`, or `:---:`.
- Keep the table rectangular: count cells before writing, and make sure the header row, separator row, and every data row have the same number of cells.
- Keep headers unique.
- Keep cells compact. Avoid nested markdown, raw HTML, and multiline content when possible.
- A header-only table parses as empty. If the user wants a blank template, include at least one blank row.
- Users can edit cells directly, sort, filter, rename columns, add rows or columns, and export as CSV or XLSX.
- When editing an existing table Canvas, use `edit` for the exact
  row, column header, separator row, or contiguous row group that changed. Do
  not rewrite the full table for a small data correction.

Good default:

```markdown
| Plan | Monthly Price | Seats | Best For |
| --- | --- | --- | --- |
| Starter | $19 | 3 | Small teams |
| Growth | $79 | 15 | Expanding teams |
| Enterprise | Custom | Unlimited | Large organizations |
```