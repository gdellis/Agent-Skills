---
name: "data-analysis"
description: "Use this skill for substantive computation, data analysis and transformation, mathematical or statistical modeling, simulation, and optimization, with a prepared Python environment (pandas, NumPy, SciPy, statsmodels, scikit-learn, matplotlib) when available. Also use it to create, modify, inspect, and verify `.xlsx` workbook content with openpyxl. Do not use it to open, display, or reconstruct an unchanged uploaded workbook; Canvas handles that presentation flow. Work from files, connected sources, existing results, or a problem stated in words."
---
# Data analysis and spreadsheets

## Required Python setup

For workbooks, `spreadsheets/QUICK_START.md` covers the Python setup; for other
Python computation, read `python/QUICK_START.md` first. Run every Python
command through its activation script and use the bundled packages; do not
install dependencies.

## Required spreadsheet setup

For any request that creates, modifies, inspects, or verifies an `.xlsx` workbook,
read `spreadsheets/QUICK_START.md` before calling any execution or file-writing
tool. This file is required even when the workbook task is simple. Do not begin
workbook authoring from memory.

Run statistics, modeling, simulation, and optimization in Python, save the
results as JSON or CSV, and read that exact file in the workbook script.

Use this workflow when the request requires computation, analytical manipulation,
model construction or verification, or spreadsheet operations. A dataset upload
is not required. Ordinary explanations, trivial arithmetic, unrelated application
development, and document authoring keep their existing workflows.

All relative references resolve from `/home/user/skills/data-analysis/`, including
references in supporting documents. Read only the references needed for the task.
Choose execution and delivery routes from the capabilities listed below.

## Work through the problem

1. Identify the outcome: understand, calculate, validate, transform, model, modify,
   or deliver. Preserve the referenced work on follow-up and choose an initial
   delivery format before expensive authoring.
2. Locate or construct the relevant inputs. Read `inputs.md` for uploads,
   connectors, saved tool results, extraction, or mixed sources. A problem stated
   in words can supply assumptions directly; label material assumptions and
   distinguish synthetic examples from observed facts.
3. Inspect what matters: structure, types, units, missingness, keys, time periods,
   or model constraints. Do not scan every directory or connector by default.
   For vague requests, choose a useful default and explain it briefly; ask only
   when missing information materially changes correctness or the deliverable.
4. Choose the necessary route from the capabilities below. Python computation:
   `python/QUICK_START.md`. Workbook operations: `spreadsheets/QUICK_START.md`,
   including targeted edits, formulas, and verification. Direct Google Sheets
   edits use a Google Sheets connector when available. Combine routes by
   saving verified JSON/CSV and reading that exact file in the workbook script.
5. Verify the result, with checks appropriate to the question. Use
   `methods/verification.md`, `methods/statistics-and-modeling.md`, or
   `methods/simulation-and-optimization.md` when those methods are needed.
   Inspect actual errors, patch the responsible script, and rerun the necessary
   step. Preserve useful work instead of restarting a model on a hunch.
6. Deliver the result using the policy below, with conclusions, relevant evidence,
   units, precision, uncertainty, and material assumptions. Do not force a report,
   workbook, or chart onto every request. Persist reusable scripts and data under
   `/home/user/tool-results/data-analysis/<run>/` for later changes.

Quantitative work includes preparation, reconciliation, exploration, experiments,
forecasting, simulation, optimization, symbolic and numerical mathematics, text
and network analysis, and the spreadsheet lifecycle.

## Choose delivery from intended use

Apply these priorities in order:

1. Follow explicit format, destination, application, and delivery instructions.
   Check actual support; explain an unavailable destination instead of claiming
   an export succeeded or silently replacing a requested format.
2. Preserve the existing workbook, dashboard, or other deliverable on follow-up,
   unless the user asks for conversion. Showing existing work does not require
   regenerating it.
3. Infer what the user needs to do: understand, inspect, edit, audit, explore,
   import, or share. Choose an experience and, separately, any portable file.
4. Check fit: volume, precision, editability, interaction, schema, and available
   renderers. Summarize large data for display without silently dropping rows
   from the complete result. React Canvas provides browser interaction, not a
   provisioned backend or live access to connector credentials.
5. Produce the smallest useful set of outputs. Companion data or image files are
   useful when requested or needed for reuse; do not create every output by default.

Use prose or a modest table for conclusions and exact values; Rich UI for compact
inline comparisons or trends; Spreadsheet Canvas for editable cells and auditable
formulas; React Canvas for filters, parameter changes, and interactive scenarios;
and Table Canvas only for a standalone editable table with at most 50 data rows.
Substantial narrative deliverables use a document or presentation authoring
capability when available.

Input format and computation language do not choose delivery. An XLSX input may
need only an explanation; Python can feed an interactive tool. Pass verified data
to the selected renderer, load its skill and actual schema, and follow its checks
and returned-link contract. For browser-side scenarios, verify calculations match
the analytical model. Compute and validate in the working directory.

For requested files, including CSV, TSV, JSON, PNG, and SVG, generate the
complete file with appropriate computation or authoring tools. Never write a
large tabular dataset row by row. Then follow the shared Canvas, Artifacts &
Deliverables instructions and load the `artifacts` skill.

## Available in this turn
- Python: workbooks follow `spreadsheets/QUICK_START.md`; for other Python computation, read `python/QUICK_START.md`, upgrade the execution environment, then source the activation script in every Python command.
- Workbook authoring (openpyxl) and Spreadsheet Canvas: read `spreadsheets/QUICK_START.md`.
- Compact inline charts: load `rich-ui` and its visualization reference.
- Interactive tools and dashboards: load `canvas` and `canvas-react`; follow their runtime and validation contracts.
