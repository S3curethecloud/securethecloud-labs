#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HOME = ROOT / "index.html"
MANIFEST = ROOT / "manifest.json"

LAB = {
    "id": "senior-consultant-enterprise-agent-delivery-capstone",
    "title": "Senior Consultant Enterprise Agent Delivery Capstone",
    "cloud": "enterprise-agent-developer",
    "domain": "Enterprise Agentic AI",
    "track": "enterprise-agent-developer",
    "level": "L2",
    "status": "implemented",
    "path": "/labs/enterprise-agent-developer/senior-consultant-enterprise-agent-delivery-capstone/",
    "backend_exposure": False,
}

OLD_STATS = (
    '          <div class="stat"><strong>71</strong><span>LAB modules</span></div>\n'
    '          <div class="stat"><strong>6</strong><span>Learning paths</span></div>\n'
    '          <div