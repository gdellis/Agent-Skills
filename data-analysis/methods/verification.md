# Verification

Choose checks that can falsify the result. Reconcile input/output row counts,
totals, join cardinality, unique keys, units, and missingness after transformations.
For numerical work, inspect residuals, tolerances, boundary cases, and an independent
calculation where practical. Explain approximations and avoid false precision.

Workbook work is verified by a clean `spreadsheets/scripts/check_workbook.py` run plus a read-back of key output cells; saved caches
alone do not prove correctness. Mixed Python/workbook/interactive results must
consume the same verified data and agree on scenarios and rounding. A successful
script or renderer call does not establish that the underlying analysis is valid.

When a check fails, inspect the actual error and fix its root cause in the local
script. Preserve inputs and working sections. Report missing data or an unavailable
capability rather than fabricating results or silently sampling the dataset.
