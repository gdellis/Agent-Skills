# Building and editing workbooks with openpyxl

## Environment

- Unless the execution environment is already upgraded, call `upgrade_execution_environment` before the first Python command.
- If the upgrade fails, stop: tell the user the workbook cannot be built in this turn, write no `CANVAS.md`, and do not try another way.
- Begin every Python command with exactly `. /home/user/skills/data-analysis/python/library/activate.sh &&` in the same shell call, with no other path or fallback; it provides openpyxl and pandas, and nothing may be installed.

## Files

- Uploads in `/home/user/uploads/` are read-only.
- Scripts and scratch files go in `/home/user/tool-results/data-analysis/<run>/`.
- Deliver the workbook to `/home/user/canvases/<name>/workbook.xlsx`; that folder holds only the workbook and `CANVAS.md`.

## Reading a workbook

- When the user asks about a workbook and wants no new or edited file, read it and answer in chat, with no canvas.
- Use pandas for values (list the sheets, find the header row); to see formulas beside their stored results, load it twice with openpyxl, once plainly and once with `data_only=True`.
- If formula cells read back empty, copy the file into `/home/user/tool-results/data-analysis/<run>/`, run the checker on that copy, and read the results from it, leaving the upload untouched.

## Steps to build or edit a workbook

1. Build with openpyxl, writing every derived number as a live formula rather than a value computed in Python.
2. Save to the canvas path.
3. Run the checker on that final file, which calculates the formulas and stores their results in it, changing nothing else, and repeat until `verdict` is `"clean"`:

   ```
   . /home/user/skills/data-analysis/python/library/activate.sh && \
   python /home/user/skills/data-analysis/spreadsheets/scripts/check_workbook.py \
     /home/user/canvases/<name>/workbook.xlsx
   ```

   - It prints one JSON object whose `verdict` is `"clean"` or `"needs_fixes"`; deliver a file once it is clean, or once a refusal says it can be delivered as it is.
   - `problems` and `layout_notes` are lists of `{kind, cells, more, how_to_fix}`, and each `how_to_fix` holds everything needed to act on its entry.
   - Fix each `problems` entry as its `how_to_fix` says, covering the listed cells and the `more` further cells with the same cause, then rerun; `layout_notes` are advisory, so act on those a reader would notice.
   - `{"refused": ...}` means nothing was checked; take the next step its reason names. With `"file_unchanged": false`, the formulas could not be calculated here and the file is set for Excel to calculate them on open: either make them calculable as the reason says and check again, or deliver the file as it is and tell the user its figures were not checked.

4. Read back from the checked file every figure and claim your answer makes, and have the answer name every value you changed, corrected, or assumed relative to what the user supplied.
5. As the very last step, after the final check, write `CANVAS.md` if the canvas does not have one yet, where `<name>` is the canvas folder name, with only this frontmatter and an empty body:

   ```
   ---
   name: <name>
   title: "<short title for the user>"
   type: spreadsheet
   entryPoint: workbook.xlsx
   ---
   ```

   When you edit a workbook whose canvas already exists, run the checker after your last change before you finish: it is what recalculates the formulas and stores their results in the file.

## Rules

- The first sheet is the one the user asked for.
- Growing lists (logs, transactions, entries) are Excel tables holding records only, with totals in the table's total row or a separate summary, and every formula, drop-down, and conditional format that reads or formats the list refers to table columns so it extends with new rows.
- When editing, keep the user's values, totals, formulas, sheets, layout, and formatting (column widths, fonts, fills) as they are, unless the user asks otherwise; you may widen a column so content you add fits. Only cells you add follow the rules here, and any cell added to a table matches its style and sits inside the table range. A sheet you add to an existing workbook takes its title, header, and body styling from the workbook's own sheets.

## House style (only for workbooks you create from scratch)

- Gridlines off, column A width 2, content from B2, and on each sheet the header row of its main table frozen.
- Title Arial 20 colour `303030` on a row 28 pt high, optional subtitle colour `626262`, then a thick `FA500F` bottom border under them, each spanning the full content width.
- Table headers fill `303030`, bold white; body text Arial 11 colour `303030`; numbers and their headers right-aligned, text left-aligned.
- Set the font on every cell you write, including cells you give no other formatting, since openpyxl writes those in Calibri.
- Every used column gets an explicit width that fits its content.
- Input cells font `1F4E79` on fill `FFF2CC`; formulas reading another sheet `2E7D6B`; formulas reading another file `A34B4B`; total rows bold.

## openpyxl traps that lose data silently

- `load_workbook(data_only=True)` drops formulas, and saving that workbook replaces them with constants.
- Load a workbook you will save with `load_workbook(path, rich_text=True)`; the default flattens mixed formatting inside cells.
