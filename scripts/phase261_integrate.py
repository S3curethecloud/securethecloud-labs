#!/usr/bin/env python3
"""Fail-closed Phase 261 homepage and manifest integration."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HOMEPAGE = ROOT / "index.html"
MANIFEST = ROOT / "manifest.json"

LAB_ID = "deterministic-routing-multi-agent-orchestration"
LAB_PATH = "/labs/enterprise-agent-developer/deterministic-routing-multi-agent-orchestration/"
TRACK_ID = "enterprise-agent-developer"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"FAIL: expected exactly one {label}; found {count}")
    return text.replace(old, new, 1)


def update_homepage() -> None:
    text = HOMEPAGE.read_text(encoding="utf-8")

    if LAB_ID in text or LAB_PATH in text:
        raise SystemExit("FAIL: Module 4 already appears in homepage")

    text = replace_once(
        text,
        '<div class="stat"><strong>66</strong><span>LAB modules</span></div>',
        '<div class="stat"><strong>67</strong><span>LAB modules</span></div>',
        "LAB module count",
    )
    text = replace_once(
        text,
        '<div class="stat"><strong>42</strong><span>Total AI modules</span></div>',
        '<div class="stat"><strong>43</strong><span>Total AI modules</span></div>',
        "total AI module count",
    )

    module3_card = '''          <article class="lab-card" data-search="enterprise rag and tool-use engineering enterprise-rag-tool-use-engineering enterprise-agent-developer enterprise agentic ai l2 source authority ingestion chunking metadata tenant filters embeddings vector search hybrid retrieval reranking context assembly citations provenance freshness prompt injection tool schema least privilege approval idempotency evaluation" data-cloud="enterprise-agent-developer" data-level="L2">
            <div class="lab-card-top">
              <div>
                <p class="lab-card-meta">ENTERPRISE AGENT DEVELOPER · Enterprise Agentic AI · L2</p>
                <h3>Enterprise RAG and Tool-Use Engineering</h3>
              </div>
              <span class="level-badge">L2</span>
            </div>
            <p>Design governed RAG and tool-use workflows using source authority, metadata and tenant filters, hybrid retrieval, context validation, provenance, injection defenses, schema-validated tools, least privilege, approvals, and evaluation evidence.</p>
            <p class="track-note">Track: enterprise-agent-developer</p>
            <a href="/labs/enterprise-agent-developer/enterprise-rag-tool-use-engineering/">Open Lab →</a>
          </article>'''

    module4_card = '''          <article class="lab-card" data-search="deterministic routing and multi-agent orchestration deterministic-routing-multi-agent-orchestration enterprise-agent-developer enterprise agentic ai l2 deterministic router model-assisted classification supervisor specialist agents handoff envelope state ownership sequential parallel orchestration retries loops deadlock livelock idempotency fallback escalation trace evaluation" data-cloud="enterprise-agent-developer" data-level="L2">
            <div class="lab-card-top">
              <div>
                <p class="lab-card-meta">ENTERPRISE AGENT DEVELOPER · Enterprise Agentic AI · L2</p>
                <h3>Deterministic Routing and Multi-Agent Orchestration</h3>
              </div>
              <span class="level-badge">L2</span>
            </div>
            <p>Design controlled routing and multi-agent workflows using deterministic rules, bounded model classification, supervisor and specialist contracts, typed handoffs, external state ownership, hard limits, fallbacks, duplicate prevention, and trace evidence.</p>
            <p class="track-note">Track: enterprise-agent-developer</p>
            <a href="/labs/enterprise-agent-developer/deterministic-routing-multi-agent-orchestration/">Open Lab →</a>
          </article>'''

    text = replace_once(
        text,
        module3_card,
        module3_card + "\n\n" + module4_card,
        "Module 3 catalog card anchor",
    )

    text = replace_once(
        text,
        "Modules 1 through 3 establish the senior-consultant role architecture, controlled conversational behavior, and governed enterprise RAG and tool-use engineering before the track moves into orchestration, interoperability, policy, observability, platform delivery, and the final capstone.",
        "Modules 1 through 4 establish the senior-consultant role architecture, controlled conversational behavior, governed enterprise RAG and tool use, and deterministic routing with bounded multi-agent orchestration before the track moves into interoperability, policy, observability, platform delivery, and the final capstone.",
        "active-track preview description",
    )
    text = replace_once(
        text,
        "Status: active track - 3 of 9 modules implemented - no live agent, model, retrieval, tool, gateway, MCP, policy, telemetry, or cloud execution.",
        "Status: active track - 4 of 9 modules implemented - no live agent, model, routing, handoff, retrieval, tool, gateway, MCP, policy, telemetry, or cloud execution.",
        "active-track preview status",
    )

    required = [
        '<strong>67</strong><span>LAB modules</span>',
        '<strong>6</strong><span>Learning paths</span>',
        '<strong>43</strong><span>Total AI modules</span>',
        '<h3>Deterministic Routing and Multi-Agent Orchestration</h3>',
        LAB_PATH,
        "4 of 9 modules implemented",
    ]
    for marker in required:
        if marker not in text:
            raise SystemExit(f"FAIL: homepage postcondition missing: {marker}")

    if text.count('<h3>Deterministic Routing and Multi-Agent Orchestration</h3>') != 1:
        raise SystemExit("FAIL: duplicate Module 4 homepage card")
    if text.count(LAB_PATH) != 1:
        raise SystemExit("FAIL: unexpected Module 4 homepage path count")

    HOMEPAGE.write_text(text, encoding="utf-8")
    print("PASS: homepage integrated")


def update_manifest() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    labs = manifest.get("labs")
    tracks = manifest.get("tracks")
    if not isinstance(labs, list) or not isinstance(tracks, list):
        raise SystemExit("FAIL: manifest labs/tracks arrays missing")

    if any(item.get("id") == LAB_ID for item in labs):
        raise SystemExit("FAIL: Module 4 already appears in manifest")

    module3_indexes = [
        index
        for index, item in enumerate(labs)
        if item.get("id") == "enterprise-rag-tool-use-engineering"
    ]
    if len(module3_indexes) != 1:
        raise SystemExit(f"FAIL: expected one Module 3 manifest anchor; found {len(module3_indexes)}")

    lab_record = {
        "id": LAB_ID,
        "title": "Deterministic Routing and Multi-Agent Orchestration",
        "cloud": "enterprise-agent-developer",
        "domain": "Enterprise Agentic AI",
        "track": TRACK_ID,
        "level": "L2",
        "status": "implemented",
        "path": LAB_PATH,
        "backend_exposure": False,
    }
    labs.insert(module3_indexes[0] + 1, lab_record)

    matching_tracks = [item for item in tracks if item.get("id") == TRACK_ID]
    if len(matching_tracks) != 1:
        raise SystemExit(f"FAIL: expected one Enterprise Agent Developer track; found {len(matching_tracks)}")

    track = matching_tracks[0]
    if track.get("status") != "active":
        raise SystemExit(f"FAIL: unexpected track status: {track.get('status')}")
    if track.get("implemented_modules") != 3:
        raise SystemExit(
            f"FAIL: expected implemented_modules=3; found {track.get('implemented_modules')}"
        )
    if track.get("planned_modules") != 9:
        raise SystemExit(f"FAIL: expected planned_modules=9; found {track.get('planned_modules')}")
    if track.get("backend_exposure") is not False:
        raise SystemExit("FAIL: track backend_exposure must remain false")
    if track.get("production_enforcement_claim") is not False:
        raise SystemExit("FAIL: track production_enforcement_claim must remain false")

    track["implemented_modules"] = 4

    if sum(item.get("id") == LAB_ID for item in labs) != 1:
        raise SystemExit("FAIL: Module 4 manifest record count is not one")
    if track["implemented_modules"] != 4:
        raise SystemExit("FAIL: track did not advance to four modules")

    MANIFEST.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print("PASS: manifest integrated")


def main() -> None:
    update_homepage()
    update_manifest()
    print("PASS: Phase 261 integration complete")


if __name__ == "__main__":
    main()
