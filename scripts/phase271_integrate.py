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
    '          <div class="stat"><strong>47</strong><span>Total AI modules</span></div>'
)
NEW_STATS = (
    '          <div class="stat"><strong>72</strong><span>LAB modules</span></div>\n'
    '          <div class="stat"><strong>6</strong><span>Learning paths</span></div>\n'
    '          <div class="stat"><strong>48</strong><span>Total AI modules</span></div>'
)

OLD_COMPLETE_PATHS = '          <div class="stat"><strong>5</strong><span>Complete learning paths</span></div>'
NEW_COMPLETE_PATHS = '          <div class="stat"><strong>6</strong><span>Complete learning paths</span></div>'

CATALOG_ANCHOR = '''          <article class="lab-card" data-search="ai red team scenario design capstone'''
CAPSTONE_CARD = '''          <article class="lab-card" data-search="senior consultant enterprise agent delivery capstone senior-consultant-enterprise-agent-delivery-capstone enterprise-agent-developer enterprise agentic ai l2 discovery process mapping stakeholder architecture decision record roadmap governance evidence executive communication mentorship operating model readiness">
            <div class="lab-card-top"><div><p class="lab-card-meta">ENTERPRISE AGENT DEVELOPER · Enterprise Agentic AI · L2</p><h3>Senior Consultant Enterprise Agent Delivery Capstone</h3></div><span class="level-badge">L2</span></div>
            <p>Lead a synthetic enterprise agent engagement from discovery and process mapping through architecture, governance, delivery planning, executive communication, mentorship, operating-model design, and evidence-backed readiness decisions.</p>
            <p class="track-note">Track: enterprise-agent-developer</p>
            <a href="/labs/enterprise-agent-developer/senior-consultant-enterprise-agent-delivery-capstone/">Open Lab →</a>
          </article>

'''

OLD_PREVIEW = '''      <p>Modules 1 through 8 establish the senior-consultant role architecture, controlled conversational behavior, governed enterprise RAG and tool use, deterministic orchestration, enterprise interoperability contracts, OPA policy with Responsible AI controls, OpenTelemetry-driven reliability, cost and performance engineering, and controlled cloud delivery with container, CI/CD, supply-chain, and platform-collaboration contracts before the final capstone.</p>
      <p class="track-note">Status: active track - 8 of 9 modules implemented - no live agent, model, routing, handoff, retrieval, tool, API, gateway, MCP, registry, policy, approval, Responsible AI evaluation, telemetry export, SLO enforcement, container build, image push, registry mutation, artifact signing, scanning, CI/CD execution, infrastructure provisioning, Kubernetes execution, Bedrock deployment, Foundry deployment, secret retrieval, or cloud execution.</p>'''
NEW_PREVIEW = '''      <p>Modules 1 through 9 complete the Enterprise Agent Developer L2 curriculum across role architecture, conversational agents, RAG and tools, deterministic orchestration, gateway and MCP contracts, policy and Responsible AI, observability, cloud delivery, and senior-consultant engagement leadership.</p>
      <p class="track-note">Status: complete track - 9 of 9 modules implemented - static educational content only; no real client engagement, stakeholder outreach, live demonstration, agent or model execution, tool or API invocation, production decision, cloud deployment, external communication, or production enforcement.</p>'''


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"FAIL: expected exactly one {label}; found {count}")
    return text.replace(old, new, 1)


home = HOME.read_text(encoding="utf-8")

if LAB["path"] in home or f'<h3>{LAB["title"]}</h3>' in home:
    raise SystemExit("FAIL: capstone homepage registration already exists")

home = replace_once(home, OLD_STATS, NEW_STATS, "homepage statistics baseline")
home = replace_once(home, OLD_COMPLETE_PATHS, NEW_COMPLETE_PATHS, "complete learning-path count")
home = replace_once(home, CATALOG_ANCHOR, CAPSTONE_CARD + CATALOG_ANCHOR, "catalog insertion anchor")
home = replace_once(home, OLD_PREVIEW, NEW_PREVIEW, "Enterprise Agent Developer preview")
HOME.write_text(home, encoding="utf-8")

manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

labs = manifest.get("labs")
tracks = manifest.get("tracks")
if not isinstance(labs, list) or not isinstance(tracks, list):
    raise SystemExit("FAIL: manifest labs or tracks collection missing")

if any(item.get("id") == LAB["id"] for item in labs):
    raise SystemExit("FAIL: capstone manifest record already exists")

matching_tracks = [item for item in tracks if item.get("id") == "enterprise-agent-developer"]
if len(matching_tracks) != 1:
    raise SystemExit(f"FAIL: expected one Enterprise Agent Developer track record; found {len(matching_tracks)}")

track = matching_tracks[0]
expected = {
    "status": "active",
    "implemented_modules": 8,
    "planned_modules": 9,
    "backend_exposure": False,
    "production_enforcement_claim": False,
}
for key, value in expected.items():
    if track.get(key) != value:
        raise SystemExit(f"FAIL: unexpected track baseline for {key}: {track.get(key)!r}")

labs.append(LAB)
track["status"] = "complete"
track["implemented_modules"] = 9

MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

print("PASS: homepage advanced to 72 LAB modules, 6 learning paths, 48 total AI modules, and 6 complete learning paths")
print("PASS: capstone catalog card registered once")
print("PASS: capstone manifest record registered once")
print("PASS: Enterprise Agent Developer track advanced to complete at 9 of 9")
