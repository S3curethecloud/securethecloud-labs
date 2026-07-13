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

OLD_STATS = '<strong>70</strong><span>LAB modules</span>'
NEW_STATS = '<strong>71</strong><span>LAB modules</span>'
OLD_AI = '<strong>46</strong><span>Total AI modules</span>'
NEW_AI = '<strong>47</strong><span>Total AI modules</span>'
OLD_PREVIEW = (
    'Modules 1 through 7 establish the senior-consultant role architecture, controlled conversational behavior, governed enterprise RAG and tool use, deterministic orchestration, enterprise interoperability contracts, OPA policy with Responsible AI controls, and OpenTelemetry-driven reliability, cost, and performance engineering before the track moves into platform delivery and the final capstone.'
)
NEW_PREVIEW = (
    'Modules 1 through 8 establish the senior-consultant role architecture, controlled conversational behavior, governed enterprise RAG and tool use, deterministic orchestration, enterprise interoperability contracts, OPA policy with Responsible AI controls, OpenTelemetry-driven reliability, cost and performance engineering, and controlled cloud delivery with container, CI/CD, supply-chain, and platform-collaboration contracts before the final capstone.'
)
OLD_STATUS = (
    'Status: active track - 7 of 9 modules implemented - no live agent, model, routing, handoff, retrieval, tool, API, gateway, MCP, registry, policy, approval, Responsible AI evaluation, telemetry export, SLO enforcement, load testing, cache mutation, fallback execution, autoscaling, or cloud execution.'
)
NEW_STATUS = (
    'Status: active track - 8 of 9 modules implemented - no live agent, model, routing, handoff, retrieval, tool, API, gateway, MCP, registry, policy, approval, Responsible AI evaluation, telemetry export, SLO enforcement, container build, image push, registry mutation, artifact signing, scanning, CI/CD execution, infrastructure provisioning, Kubernetes execution, Bedrock deployment, Foundry deployment, secret retrieval, or cloud execution.'
)
CARD_ANCHOR = '          <article class="lab-card" data-search="ai red team scenario design capstone'
CARD = '''          <article class="lab-card" data-search="cloud delivery containers cicd ci cd platform collaboration cloud-delivery-containers-cicd-platform-collaboration enterprise-agent-developer enterprise agentic ai l2 container supply chain sbom provenance signing vulnerability scan pipeline promotion workload identity aws bedrock microsoft foundry kubernetes rollback raci" data-cloud="enterprise-agent-developer" data-level="L2">
            <div class="lab-card-top"><div><p class="lab-card-meta">ENTERPRISE AGENT DEVELOPER · Enterprise Agentic AI · L2</p><h3>Cloud Delivery, Containers, CI/CD, and Platform Collaboration</h3></div><span class="level-badge">L2</span></div>
            <p>Design immutable container packaging, software-supply-chain evidence, CI/CD gates, environment promotion, workload identity, rollback, cloud deployment contracts, paved roads, and cross-team ownership without executing live delivery operations.</p>
            <p class="track-note">Track: enterprise-agent-developer</p>
            <a href="/labs/enterprise-agent-developer/cloud-delivery-containers-cicd-platform-collaboration/">Open Lab →</a>
          </article>

'''


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"FAIL: {label} expected once, found {count}")
    return text.replace(old, new, 1)


home = HOME.read_text(encoding="utf-8")
if LAB["path"] in home or LAB["title"] in home:
    raise SystemExit("FAIL: Module 8 homepage registration already exists")
home = replace_once(home, OLD_STATS, NEW_STATS, "LAB count")
home = replace_once(home, OLD_AI, NEW_AI, "AI count")
home = replace_once(home, OLD_PREVIEW, NEW_PREVIEW, "track preview")
home = replace_once(home, OLD_STATUS, NEW_STATUS, "track status")
home = replace_once(home, CARD_ANCHOR, CARD + CARD_ANCHOR, "catalog anchor")
HOME.write_text(home, encoding="utf-8")

manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
labs = manifest.get("labs", [])
tracks = manifest.get("tracks", [])
if any(item.get("id") == LAB["id"] for item in labs):
    raise SystemExit("FAIL: Module 8 manifest registration already exists")
track_matches = [item for item in tracks if item.get("id") == "enterprise-agent-developer"]
if len(track_matches) != 1:
    raise SystemExit(f"FAIL: enterprise track count = {len(track_matches)}")
track = track_matches[0]
if track.get("implemented_modules") != 7 or track.get("planned_modules") != 9:
    raise SystemExit(f"FAIL: unexpected track baseline = {track}")
labs.append(LAB)
track["implemented_modules"] = 8
MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

print("PASS: homepage advanced to 71 LAB modules, 6 learning paths, and 47 total AI modules")
print("PASS: Module 8 catalog card added exactly once")
print("PASS: Module 8 manifest record added exactly once")
print("PASS: Enterprise Agent Developer track advanced to 8 of 9")
