#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HOME = ROOT / "index.html"
MANIFEST = ROOT / "manifest.json"

LAB = {
    "id": "opa-policy-responsible-ai-controls",
    "title": "OPA Policy Enforcement and Responsible AI Controls",
    "cloud": "enterprise-agent-developer",
    "domain": "Enterprise Agentic AI",
    "track": "enterprise-agent-developer",
    "level": "L2",
    "status": "implemented",
    "path": "/labs/enterprise-agent-developer/opa-policy-responsible-ai-controls/",
    "backend_exposure": False,
}

home = HOME.read_text(encoding="utf-8")
manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

required_home = [
    '<strong>68</strong><span>LAB modules</span>',
    '<strong>44</strong><span>Total AI modules</span>',
    '5 of 9 modules implemented',
]
for marker in required_home:
    if marker not in home:
        raise SystemExit(f"baseline marker missing: {marker}")

if any(item.get("id") == LAB["id"] for item in manifest["labs"]):
    raise SystemExit("Module 6 already registered")

tracks = [
    item for item in manifest["tracks"]
    if item.get("id") == "enterprise-agent-developer"
]
if len(tracks) != 1:
    raise SystemExit(f"unexpected track records: {len(tracks)}")
track = tracks[0]
if track.get("implemented_modules") != 5 or track.get("planned_modules") != 9:
    raise SystemExit(f"unexpected track state: {track}")

manifest["labs"].append(LAB)
track["implemented_modules"] = 6

home = home.replace(
    '<strong>68</strong><span>LAB modules</span>',
    '<strong>69</strong><span>LAB modules</span>',
    1,
)
home = home.replace(
    '<strong>44</strong><span>Total AI modules</span>',
    '<strong>45</strong><span>Total AI modules</span>',
    1,
)

anchor = '''          <article class="lab-card" data-search="ai red team scenario design capstone'''
card = '''          <article class="lab-card" data-search="opa policy enforcement and responsible ai controls opa-policy-responsible-ai-controls enterprise-agent-developer enterprise agentic ai l2 opa rego policy decision point default deny approval residency rate limit provenance explainability fairness bias human oversight appeal audit evidence" data-cloud="enterprise-agent-developer" data-level="L2">
            <div class="lab-card-top">
              <div>
                <p class="lab-card-meta">ENTERPRISE AGENT DEVELOPER · Enterprise Agentic AI · L2</p>
                <h3>OPA Policy Enforcement and Responsible AI Controls</h3>
              </div>
              <span class="level-badge">L2</span>
            </div>
            <p>Design typed OPA/Rego policy decisions, deterministic enforcement boundaries, approvals, residency and rate-limit controls, provenance, explanation, fairness review, appeal, and audit evidence.</p>
            <p class="track-note">Track: enterprise-agent-developer</p>
            <a href="/labs/enterprise-agent-developer/opa-policy-responsible-ai-controls/">Open Lab →</a>
          </article>

'''
if anchor not in home:
    raise SystemExit("homepage catalog anchor missing")
home = home.replace(anchor, card + anchor, 1)

old_preview = '''Modules 1 through 5 establish the senior-consultant role architecture, controlled conversational behavior, governed enterprise RAG and tool use, deterministic orchestration, and enterprise gateway, MCP, registry, and API contract design before the track moves into policy, observability, platform delivery, and the final capstone.'''
new_preview = '''Modules 1 through 6 establish the senior-consultant role architecture, controlled conversational behavior, governed enterprise RAG and tool use, deterministic orchestration, enterprise interoperability contracts, and OPA policy with Responsible AI controls before the track moves into observability, platform delivery, and the final capstone.'''
if old_preview not in home:
    raise SystemExit("homepage preview baseline missing")
home = home.replace(old_preview, new_preview, 1)
home = home.replace(
    'Status: active track - 5 of 9 modules implemented - no live agent, model, routing, handoff, retrieval, tool, API, gateway, MCP, registry, policy, telemetry, or cloud execution.',
    'Status: active track - 6 of 9 modules implemented - no live agent, model, routing, handoff, retrieval, tool, API, gateway, MCP, registry, policy, approval, Responsible AI evaluation, telemetry, or cloud execution.',
    1,
)

HOME.write_text(home, encoding="utf-8")
MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
print("PASS: Phase 265 homepage and manifest integration complete")
