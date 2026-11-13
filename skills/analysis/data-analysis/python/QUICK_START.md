# Python computation

Use Python for data preparation, analysis, statistics, prediction, simulation,
optimization, symbolic/numerical mathematics, and result-only exports.

## Execute

Unless the execution environment is already upgraded, call the top-level
`upgrade_execution_environment` tool before the first Python or Node command.
Once upgraded, save scripts and data
under `/home/user/tool-results/data-analysis/<run>/`, where `<run>` is the actual
working-directory name. Execute through ordinary bash. Every Python command must
source activation in the **same shell command**:

```sh
. /home/user/skills/data-analysis/python/library/activate.sh &&
python /home/user/tool-results/data-analysis/<run>/analysis.py
```

Environment exports and Python variables do not persist across separate tool
calls/processes. Persist scripts, parameters, and data, then rerun the necessary
computation when assumptions change. Keep commands in the foreground.

The bundle provides NumPy, pandas, openpyxl, SciPy, statsmodels, numpy-financial,
scikit-learn, SymPy, matplotlib, xlrd, and networkx. Use Python's standard
library for ordinary parsing and algorithms. Do not install dependencies.
Parquet/Arrow readers and writers, GIS engines, pretrained NLP models and corpora,
OCR, advanced imaging, PDF/Office authoring libraries, LightGBM, seaborn, Plotly,
XlsxWriter, Jupyter kernels, and widgets are not supplied. Use an actually
available tool/skill for those capabilities or explain the limitation.

## Inspect and compute

Use `inputs.md` to acquire full inputs. Inspect available files under
`/home/user/uploads`; confirm they contain original bytes rather than placeholder
notices before parsing them. Choose CSV parsing rules,
sheet/header rows, identifier dtypes, locale, units, and missing-value behavior
from the source. For example, adapt this to the real filename and columns:

```python
from pathlib import Path
import pandas as pd

work = Path("/home/user/tool-results/data-analysis/sales")
work.mkdir(parents=True, exist_ok=True)
data = pd.read_csv("/home/user/uploads/sales.csv", dtype={"customer_id": "string"})
print("Rows and columns:", data.shape)
print(data.dtypes)
print(data.head().to_string(index=False))
print("Missing:", data.isna().sum().to_dict())
data["amount"] = pd.to_numeric(data["amount"], errors="raise")
summary = data.groupby("category", dropna=False, as_index=False)["amount"].sum()
assert abs(summary["amount"].sum() - data["amount"].sum()) < 1e-6
summary.to_json(work / "summary.json", orient="records", indent=2)
print(summary.to_string(index=False))
```

Inspect XLSX with `pd.ExcelFile(..., engine="openpyxl")` and XLS with `xlrd`.
Formula caches can be missing/stale and openpyxl
does not calculate formulas.

For a problem without files, construct the computation directly. Verify units,
constraints, residuals, baselines, uncertainty, and boundary cases as appropriate;
read the relevant `methods/` reference. Label assumptions and synthetic data.

## Hand off verified results

Save intermediate and complete results as JSON or CSV in the working directory so
other routes can read the exact values. For static plots use matplotlib, label
units, save into the working directory, and close figures.

Follow the root skill's delivery policy. Use available inline/Canvas renderers
and their own skills; do not return a workbook solely because the input was XLSX.
For downloadable files, follow the shared Canvas, Artifacts & Deliverables
instructions and load the `artifacts` skill when publication is available.
