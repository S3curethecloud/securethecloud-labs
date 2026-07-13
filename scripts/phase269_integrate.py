#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HOME = ROOT / "index.html"
MANIFEST = ROOT / "manifest.json"

LAB = {
    "id": "cloud-delivery-containers-cicd-platform-collaboration",
    "title": "Cloud Delivery, Containers, CI/CD, and Platform Collaboration",
    "cloud": "enterprise-agent-developer",
    "domain": "Enterprise Agentic AI",
    "track": "enterprise-agent-developer",
    "level": "L2",
    "status": "implemented",
    "path": "/labs/enterprise-agent-developer/cloud-delivery-containers-cicd-platform-collaboration/",
    "backend_exposure": False,
}

OLD_STATS = (
    '          <div class="stat"><strong>70</strong><span>LAB modules</span></div>\n'
    '          <div class="stat"><strong>6</strong><span>Learning paths</span></div>\n'
    '          <div class="stat"><strong>46</strong><span>Total AI modules</span></div>'
)
NEW_STATS = (
    '          <div class="stat"><strong>71</strong><span>LAB modules</span></div>\n'
    '          <div class="stat"><strong>6</strong><span>Learning paths</span></div>\n'
    '          <div class="stat"><strong>47</strong><span>Total AI modules</span></div>'
)
