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
    "backend_exposure": False,
}

home = HOME.read_text(encoding="utf-8")
manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

required_home = [
    '<strong>69</strong><span>LAB modules</span>',
    '<strong>45</strong><span>Total AI modules</span>',
    '6 of 9 modules implemented',
]
for marker in required_home:
    if marker not in home:
        raise SystemExit(f"baseline marker missing: {marker}")

if any(item.get("id") == LAB["id"] for item in manifest["labs"]):
    raise SystemExit("Module 7 already registered")

tracks = [
    item for item in manifest["tracks"]
    if item.get("id") == "enterprise-agent-developer"
]
if len(tracks) != 1:
    raise SystemExit(f"unexpected track records: {len(tracks)}")

track = tracks[0]
if track.get("implemented_modules") != 6 or track.get("planned_modules") != 9:
    raise SystemExit(f"unexpected track state: {track}")

manifest["labs"].append(LAB)
track["implemented_modules"] = 7

home = home.replace(
    '<strong>69</strong><span>LAB modules</span>',
    '<strong>70</strong><span>LAB modules</span>',
    1,
)
home = home.replace(
    '<strong>45</strong><span>Total AI modules</span>',
    '<strong>46</strong><span>Total AI modules</span>',
    1,
)

anchor = '''          <article class="lab-card" data-search="ai red team scenario design capstone'''
card = '''          <article class="lab-card" data-search="opentelemetry slo cost and performance engineering opentelemetry-slo-cost-performance-engineering enterprise-agent-developer enterprise agentic ai l2 tracing metrics logs spans latency reliability error budget token usage cost caching fallback capacity throughput performance governance" data-cloud="enterprise-agent-developer" data-level="L2">
            <div class="lab-card-top">
              <div>
                <p class="lab-card-meta">ENTERPRISE AGENT DEVELOPER · Enterprise Agentic AI · L2</p>
                <h3>OpenTelemetry, SLO, Cost, and Performance Engineering</h3>
              </div>
              <span class="level-badge">L2</span>
            </div>
            <p>Design agent telemetry, traces, SLOs, error budgets, token and cost controls, caching, fallback, capacity, and performance evidence without executing live observability or runtime controls.</p>
            <p class="track-note">Track: enterprise-agent-developer</p>
            <a href="/labs/enterprise-agent-developer/opentelemetry-slo-cost-performance-engineering/">Open Lab →</a>
          </article>

'''
if anchor not in home:
    raise SystemExit("homepage catalog anchor missing")
home = home.replace(anchor, card + anchor, 1)

old_preview = '''Modules 1 through 6 establish the senior-consultant role architecture, controlled conversational behavior, governed enterprise RAG and tool use, deterministic orchestration, enterprise interoperability contracts, and OPA policy with Responsible AI controls before the track moves into observability, platform delivery, and the final capstone.'''
new_preview = '''Modules 1 through 7 establish the senior-consultant role architecture, controlled conversational behavior, governed enterprise RAG and tool use, deterministic orchestration, enterprise interoperability contracts, OPA policy with Responsible AI controls, and OpenTelemetry-driven reliability, cost, and performance engineering before the track moves into platform delivery and the final capstone.'''
if old_preview not in home:
    raise SystemExit("homepage preview baseline missing")
home = home.replace(old_preview, new_preview, 1)

old_status = 'Status: active track - 6 of 9 modules implemented - no live agent, model, routing, handoff, retrieval, tool, API, gateway, MCP, registry, policy, approval, Responsible AI evaluation, telemetry, or cloud execution.'
new_status = 'Status: active track - 7 of 9 modules implemented - no live agent, model, routing, handoff, retrieval, tool, API, gateway, MCP, registry, policy, approval, Responsible AI evaluation, telemetry export, SLO enforcement, load testing, cache mutation, fallback execution, autoscaling, or cloud execution.'
if old_status not in home:
    raise SystemExit("homepage status baseline missing")
home = home.replace(old_status, new_status, 1)

HOME.write_text(home, encoding="utf-8")
MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
print("PASS: Phase 267 homepage and manifest integration complete")