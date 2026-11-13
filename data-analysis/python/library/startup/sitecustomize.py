# Generated from scripts/python-activation/sitecustomize.py by `pnpm generate:python-activation`; do not edit.
"""Put the running script's folder after installed modules, so a script named like one cannot shadow it."""

import os
import sys

if getattr(sys.flags, "safe_path", False):
    script = sys.argv[0] if sys.argv else ""
    try:
        folder = os.getcwd() if script in ("", "-", "-c", "-m") else os.path.dirname(os.path.realpath(script))
    except FileNotFoundError:
        # The working directory was deleted, so there is no folder to add.
        folder = None
    if folder is not None and folder not in sys.path:
        sys.path.append(folder)
