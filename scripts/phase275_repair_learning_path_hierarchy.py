#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

INDEX = ROOT / "index.html"
START_HERE = ROOT / "start-here" / "index.html"
TRACK = ROOT / "tracks" / "enterprise-agent-developer" / "index.html"
CONFIG = ROOT / "config" / "lab_navigation_tracks.json"
PLAN = (
    ROOT
    / "docs"
   