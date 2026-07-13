#!/usr/bin/env python3
"""Fail-closed Phase 259 homepage and manifest integration utility."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "manifest.json"
INDEX_PATH = ROOT / "index.html"

LAB_ID = "enterprise-rag-tool-use-engineering"
TRACK_ID = "enterprise-agent-developer"

LAB_RECORD = {
    "id": LAB_ID,
    "title": "Enterprise RAG and Tool-Use Engineering",
    "cloud": "enterprise-agent-developer",
    "domain": "Enterprise Agentic AI",
    "track": TRACK_ID,
    "level": "L2",
    "status": "implemented",
    "path": "/labs/enterprise-agent-developer/enterprise-rag-tool-use-engineering/",
    "backend_exposure": False,
}

MODULE2_CARD = '''          <article class="lab-card" data-search="task-oriented and conversational agent design task-oriented-conversational-agent-design enterprise-agent-developer enterprise agentic ai l2 task contract conversation structured output json schema state memory intent confidence function calling refusal escalation loop limits human handoff" data-cloud="enterprise-agent-developer" data-level="L2">
            <div class="lab-card-top">
              <div>
                <p class="lab-card-meta">ENTERPRISE AGENT DEVELOPER · Enterprise Agentic AI · L2</p>
                <h3>Task-Oriented and Conversational Agent Design</h3>
              </div>
              <span class="level-badge">L2</span>
            </div>
            <p>Design controlled conversational agents using explicit task contracts, structured outputs, state and memory boundaries, deterministic approvals, refusal paths, loop limits, and human handoff.</p>
            <p class="track-note">Track: enterprise-agent-developer</p>
            <a href="/labs/enterprise-agent-developer/task-oriented-conversational-agent-design/">Open Lab →</a>
          </article>
'''

MODULE3_CARD = '''
          <article class="lab-card" data-search="enterprise rag and tool-use engineering enterprise-rag-tool-use-engineering enterprise-agent-developer enterprise agentic ai l2 source authority ingestion chunking metadata tenant filters embeddings vector search hybrid retrieval reranking context assembly citations provenance freshness prompt injection tool schema least privilege approval idempotency evaluation" data-cloud="enterprise-agent-developer" data-level="L2">
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
          </article>
'''

OLD_PREVIEW_BODY = "Modules 1 and 2 establish the senior-consultant role architecture and controlled task-oriented and conversational agent behavior before the track moves into RAG, orchestration, interoperability, policy, observability, platform delivery, and the final capstone."
NEW_PREVIEW_BODY = "Modules 1 through 3 establish the senior-consultant role architecture, controlled conversational behavior, and governed enterprise RAG and tool-use engineering before the track moves into orchestration, interoperability, policy, observability, platform delivery, and the final capstone."

OLD_PREVIEW_STATUS = "Status: active track - 2 of 9 modules implemented - no live agent, model, gateway, MCP, policy, telemetry, or cloud execution."
NEW_PREVIEW_STATUS = "Status: active track - 3 of 9 modules implemented - no live agent, model, retrieval, tool, gateway, MCP, policy, telemetry, or cloud execution."


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def integrate_manifest() -> None:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    require(isinstance(manifest.get("labs"), list), "manifest labs array missing")
    require(isinstance(manifest.get("tracks"), list), "manifest tracks array missing")

    existing_labs = [item for item in manifest["labs"] if item.get("id") == LAB_ID]
    require(len(existing_labs) == 0, f"expected no existing {LAB_ID} LAB record")

    tracks = [item for item in manifest["tracks"] if item.get("id") == TRACK_ID]
    require(len(tracks) == 1, "expected exactly one Enterprise Agent Developer track record")
    track = tracks[0]
    require(track.get("status") == "active", "track status must remain active")
    require(track.get("implemented_modules") == 2, "track must start at 2 implemented modules")
    require(track.get("planned_modules") == 9, "track must remain planned at 9 modules")
    require(track.get("backend_exposure") is False, "track backend exposure must be false")
    require(track.get("production_enforcement_claim") is False, "production enforcement claim must be false")

    manifest["labs"].append(LAB_RECORD)
    track["implemented_modules"] = 3

    MANIFEST_PATH.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    require(count == 1, f"expected one {label}; found {count}")
    return text.replace(old, new, 1)


def integrate_homepage() -> None:
    html = INDEX_PATH.read_text(encoding="utf-8")

    html = replace_once(
        html,
        '<div class="stat"><strong>65</strong><span>LAB modules</span></div>',
        '<div class="stat"><strong>66</strong><span>LAB modules</span></div>',
        "LAB module count",
    )
    html = replace_once(
        html,
        '<div class="stat"><strong>41</strong><span>Total AI modules</span></div>',
        '<div class="stat"><strong>42</strong><span>Total AI modules</span></div>',
        "total AI module count",
    )
    require(
        html.count('<div class="stat"><strong>6</strong><span>Learning paths</span></div>') == 1,
        "learning-path count must remain 6",
    )

    require(LAB_ID not in html, "Module 3 homepage record already exists")
    html = replace_once(
        html,
        MODULE2_CARD,
        MODULE2_CARD + MODULE3_CARD,
        "Module 2 catalog card anchor",
    )
    html = replace_once(html, OLD_PREVIEW_BODY, NEW_PREVIEW_BODY, "active preview body")
    html = replace_once(html, OLD_PREVIEW_STATUS, NEW_PREVIEW_STATUS, "active preview status")

    INDEX_PATH.write_text(html, encoding="utf-8")


def validate() -> None:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    labs = [item for item in manifest["labs"] if item.get("id") == LAB_ID]
    tracks = [item for item in manifest["tracks"] if item.get("id") == TRACK_ID]
    require(len(labs) == 1, "Module 3 LAB record validation failed")
    require(labs[0] == LAB_RECORD, "Module 3 LAB record differs from canonical record")
    require(len(tracks) == 1, "track record validation failed")
    require(tracks[0].get("implemented_modules") == 3, "track did not advance to 3")
    require(tracks[0].get("planned_modules") == 9, "planned modules changed")
    require(tracks[0].get("status") == "active", "track status changed")

    html = INDEX_PATH.read_text(encoding="utf-8")
    required = [
        "66</strong><span>LAB modules",
        "6</strong><span>Learning paths",
        "42</strong><span>Total AI modules",
        "Enterprise RAG and Tool-Use Engineering",
        "/labs/enterprise-agent-developer/enterprise-rag-tool-use-engineering/",
        "3 of 9 modules implemented",
    ]
    for marker in required:
        require(marker in html, f"homepage marker missing: {marker}")

    require(html.count("enterprise-rag-tool-use-engineering") >= 2, "Module 3 homepage integration incomplete")


def main() -> None:
    integrate_manifest()
    integrate_homepage()
    validate()
    print("PASS: Phase 259 manifest and homepage integration complete")
    print("PASS: LAB modules = 66")
    print("PASS: Learning paths = 6")
    print("PASS: Total AI modules = 42")
    print("PASS: Enterprise Agent Developer track = active, 3 of 9")
    print("PASS: Backend exposure = false")
    print("PASS: Production enforcement claim = false")


if __name__ == "__main__":
    main()
