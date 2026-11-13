# Bring inputs into computation

Choose sources from the request. Preserve source names, timestamps, definitions,
units, identifiers, and uncertainty. Reconcile keys, granularity, periods, and
conflicting definitions before joining multiple sources.

## Uploads and existing files

Inspect `/home/user/uploads` when available and read any placeholder or skipped-file
notices. Some uploads expose extracted content through `read_file`; their paths
may contain a notice rather than original bytes. Only pass actual CSV/XLSX bytes
to a parser. If the original file is unavailable or exceeds the filesystem
limits, explain the limitation and use an accessible source when sufficient.
Preserve originals and write derived data in the run directory.

Select readers by format and observed structure. Preserve leading-zero IDs as
strings; specify encoding, delimiter, locale, dates, and missing-value rules.
Inspect workbook sheets/header rows before selecting them. Saved formula caches
can be absent or stale; openpyxl does not calculate formulas. For authored
workbooks, preserve formulas, structure, and formatting as described in
`spreadsheets/QUICK_START.md`.
For existing canvases/results, inspect and patch the requested portion.

## Connectors and URLs

Discover the exact connector function and schema, then fetch the required records
using its actual pagination contract. In `run_typescript`, save returned values
directly with the available filesystem write function, such as
`tools.file_system.write_file`, using its discovered schema. Do not retype data
into a later tool call. Save manageable pages rather than collecting unbounded
results in the isolate. Return a receipt with saved paths, counts, source, and
time range; Python can inspect and normalize those files after upgrade.

Do not assume generic `rows` or `nextCursor` fields. Authentication and external
writes stay in connector tools. Python has no harness credentials or `tools.*`
namespace. `run_typescript` orchestrates tools; it is not Node or Python.
A URL can identify a page, API, resource, or file: retrieve it through available
tools and inspect the actual response before choosing a parser.

## Saved tool results

Large outputs may return a saved path and truncated preview. Read the saved path,
inspect its JSON/type and real content or structured-content envelope, then
compute from the full saved result. A preview is not the dataset. If saving failed,
follow the error's recovery guidance and do not claim complete analysis.

## Text, documents, and problems without files

Structure pasted values with their labels, units, and locale without inventing
missing rows. Use available extraction/OCR/vision for PDF, scan, screenshot, or
document tables, and validate extraction against the source before computation.
Python alone does not supply OCR. For a mathematical problem or model described
in words, construct the calculation directly, record material assumptions, and
check units and boundary cases. No upload is required.
