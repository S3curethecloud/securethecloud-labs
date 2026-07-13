#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HOME = ROOT / "index.html"
MANIFEST = ROOT / "manifest.json"

LAB = {
    "id": "opentelemetry-slo-cost-performance-engineering",
    "title": "OpenTelemetry, SLO, Cost, and Performance Engineering",
    "cloud": "enterprise-agent-developer",
    "domain": "Enterprise Agentic AI",
    "track": "enterprise-agent-developer",
    "level": "L2",
    "status": "implemented",
    "path": "/labs/enterprise-agent-developer/opentelemetry-slo-cost-performance-engineering/",
    "backend_exposure":