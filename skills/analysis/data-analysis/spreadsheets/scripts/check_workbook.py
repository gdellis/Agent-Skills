"""Recalculate a workbook's formulas in place and say what to fix.

Usage: check_workbook.py PATH [--timeout SECONDS] [--allow-external-links]

Prints one JSON object. The workbook is done when `verdict` is "clean"; every entry
in `problems` and `layout_notes` says in `how_to_fix` what to change. A `refused`
field means nothing was checked, and its text names the next step.
"""

import sys
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "library" / ".bundled"))

from check_workbook_impl import main

if __name__ == "__main__":
    main()
