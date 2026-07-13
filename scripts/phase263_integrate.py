from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HOMEPAGE = ROOT / "index.html"
MANIFEST = ROOT / "manifest.json"

LAB_ID = "enterprise-gateway-mcp-registry-api-contracts"
LAB_PATH = "/labs/enterprise-agent-developer/enterprise-gateway-mcp-registry-api-contracts/"
TRACK_ID = "enterprise-agent-developer"

LAB_RECORD = {
    "id": LAB_ID,
    "title": "Enterprise Gateway, MCP, Registry, and API Contracts",
    "cloud": "enterprise-agent-developer",
    "domain": "Enterprise Agentic AI",
    "track": TRACK_ID,
    "level": "L2",
    "status": "implemented",
    "path": LAB_PATH,
    "backend_exposure": False,
}

CARD = '''          <article class="lab-card" data-search="enterprise gateway mcp registry and api contracts enterprise-gateway-mcp-registry-api-contracts enterprise-agent-developer enterprise agentic ai l2 gateway policy mcp client server resource prompt tool registry openapi json schema rest versioning compatibility authentication authorization least privilege rate limit idempotency trace" data-cloud="enterprise-agent-developer" data-level="L2">
            <div class="lab-card-top">
              <div>
                <p class="lab-card-meta">ENTERPRISE AGENT DEVELOPER · Enterprise Agentic AI · L2</p>
                <h3>Enterprise Gateway, MCP, Registry, and API Contracts</h3>
              </div>
              <span class="level-badge">L2</span>
            </div>
            <p>Design governed enterprise integration using gateway policy boundaries, MCP trust and capability contracts, persistent registry lifecycle, OpenAPI and JSON Schema validation, least privilege, versioning, compatibility, limits, rollback, and trace evidence.</p>
            <p class="track-note">Track: enterprise-agent-developer</p>
            <a href="/labs/enterprise-agent-developer/enterprise-gateway-mcp-registry-api-contracts/">Open Lab →</a>
          </article>

'''

OLD_CARD_ANCHOR = '''          <article class="lab-card" data-search="ai red team scenario design capstone'''

OLD_PREVIEW_BODY = "Modules 1 through 4 establish the senior-consultant role architecture, controlled conversational behavior, governed enterprise RAG and tool use, and deterministic routing with bounded multi-agent orchestration before the track moves into interoperability, policy, observability, platform delivery, and the final capstone."
NEW_PREVIEW_BODY = "Modules 1 through 5 establish the senior-consultant role architecture, controlled conversational behavior, governed enterprise RAG and tool use, deterministic orchestration, and enterprise gateway, MCP, registry, and API contract design before the track moves into policy, observability, platform delivery, and the final capstone."

OLD_PREVIEW_STATUS = "Status: active track - 4 of 9 modules implemented - no live agent, model, routing, handoff, retrieval, tool, gateway, MCP, policy, telemetry, or cloud execution."
NEW_PREVIEW_STATUS = "Status: active track - 5 of 9 modules implemented - no live agent, model, routing, handoff, retrieval, tool, API, gateway, MCP, registry, policy, telemetry, or cloud execution."


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one match, found {count}")
    return text.replace(old, new, 1)


def update_homepage() -> None:
    text = HOMEPAGE.read_text(encoding="utf-8")

    if text.count(f"<h3>{LAB_RECORD['title']}</h3>") != 0:
        raise RuntimeError("Module 5 homepage card already exists")
    if text.count(LAB_PATH) != 0:
        raise RuntimeError("Module 5 homepage path already exists")

    text = replace_once(
        text,
        '<div class="stat"><strong>67</strong><span>LAB modules</span></div>',
        '<div class="stat"><strong>68</strong><span>LAB modules</span></div>',
        "LAB module count",
    )
    text = replace_once(
        text,
        '<div class="stat"><strong>43</strong><span>Total AI modules</span></div>',
        '<div class="stat"><strong>44</strong><span>Total AI modules</span></div>',
        "AI module count",
    )
    text = replace_once(text, OLD_CARD_ANCHOR, CARD + OLD_CARD_ANCHOR, "catalog anchor")
    text = replace_once(text, OLD_PREVIEW_BODY, NEW_PREVIEW_BODY, "track preview body")
    text = replace_once(text, OLD_PREVIEW_STATUS, NEW_PREVIEW_STATUS, "track preview status")

    HOMEPAGE.write_text(text, encoding="utf-8")


def update_manifest() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    labs = manifest.get("labs")
    tracks = manifest.get("tracks")
    if not isinstance(labs, list) or not isinstance(tracks, list):
        raise RuntimeError("manifest labs or tracks collection missing")

    if any(item.get("id") == LAB_ID for item in labs):
        raise RuntimeError("Module 5 manifest record already exists")

    track_matches = [item for item in tracks if item.get("id") == TRACK_ID]
    if len(track_matches) != 1:
        raise RuntimeError(f"expected one Enterprise Agent Developer track, found {len(track_matches)}")

    track = track_matches[0]
    if track.get("implemented_modules") != 4:
        raise RuntimeError(f"expected implemented_modules=4, found {track.get('implemented_modules')}")
    if track.get("planned_modules") != 9:
        raise RuntimeError("planned_modules must remain 9")
    if track.get("status") != "active":
        raise RuntimeError("track must remain active")
    if track.get("backend_exposure") is not False:
        raise RuntimeError("track backend_exposure must remain false")
    if track.get("production_enforcement_claim") is not False:
        raise RuntimeError("track production_enforcement_claim must remain false")

    labs.append(LAB_RECORD)
    track["implemented_modules"] = 5

    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def validate() -> None:
    homepage = HOMEPAGE.read_text(encoding="utf-8")
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    assert homepage.count(f"<h3>{LAB_RECORD['title']}</h3>") == 1
    assert homepage.count(LAB_PATH) == 1
    assert "<strong>68</strong><span>LAB modules</span>" in homepage
    assert "<strong>6</strong><span>Learning paths</span>" in homepage
    assert "<strong>44</strong><span>Total AI modules</span>" in homepage
    assert NEW_PREVIEW_STATUS in homepage

    labs = [item for item in manifest["labs"] if item.get("id") == LAB_ID]
    tracks = [item for item in manifest["tracks"] if item.get("id") == TRACK_ID]
    assert labs == [LAB_RECORD]
    assert len(tracks) == 1
    assert tracks[0]["implemented_modules"] == 5
    assert tracks[0]["planned_modules"] == 9
    assert tracks[0]["status"] == "active"
    assert tracks[0]["backend_exposure"] is False
    assert tracks[0]["production_enforcement_claim"] is False


if __name__ == "__main__":
    update_homepage()
    update_manifest()
    validate()
    print("PASS: Phase 263 homepage and manifest integration complete")
