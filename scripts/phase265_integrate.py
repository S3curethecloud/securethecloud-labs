#!/usr/bin/env python3
"""Integrate Enterprise Agent Developer Module 6 into homepage and manifest.

Fail closed unless the repository matches the verified Phase 264 baseline.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HOME = ROOT / "index.html"
MANIFEST = ROOT / "manifest.json"

LAB_ID = "opa