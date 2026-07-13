#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import shutil
import subprocess
from pathlib import Path

ROOT = Path.cwd()
MANIFEST = ROOT / "manifest.json"
HOMEPAGE = ROOT / "index.html"
TRACK = ROOT / "tracks/enterprise-agent-developer/index.html"
MODULE = ROOT / "labs/enterprise-agent-developer/task-oriented-conversational-agent-design/index.html"
METADATA = ROOT / "labs/enterprise-agent-developer/task-oriented-conversational-agent-design/metadata.json"
ARCHITECTURE = ROOT / "labs/enterprise-agent-developer/task-oriented-conversational-agent-design/architecture.md"

LAB_ID = "task-oriented-conversational-agent-design"
TRACK_ID = "enterprise-agent-developer"
EXPECTED_BRANCH = "agent/task-oriented-conversational-agent-design-l2"

LAB_RECORD = {
    "id": LAB_ID,
    "title": "Task-Oriented and Conversational Agent Design",
    "cloud": TRACK_ID,
    "domain": "Enterprise Agentic AI",
    "track": TRACK_ID,
    "level": "L2",
    "status": "implemented",
    "path": "/labs/enterprise-agent-developer/task-oriented-conversational-agent-design/",
    "backend_exposure": False,
}

CATALOG_CARD = '''
          <article class="lab-card" data-search="task-oriented and conversational agent design task-oriented-conversational-agent-design enterprise-agent-developer enterprise agentic ai l2 task contract conversation structured output json schema state memory intent confidence function calling refusal escalation loop limits human handoff" data-cloud="enterprise-agent-developer" data-level="L2">
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

OLD_PREVIEW_COPY = "Module 1 establishes the complete senior-consultant role architecture before the track moves into agent construction, RAG, orchestration, interoperability, policy, observability, platform delivery, and the final capstone."
NEW_PREVIEW_COPY = "Modules 1 and 2 establish the senior-consultant role architecture and controlled task-oriented and conversational agent behavior before the track moves into RAG, orchestration, interoperability, policy, observability, platform delivery, and the final capstone."

OLD_STATUS = "Status: active track - 1 of 9 modules implemented - no live agent, model, gateway, MCP, policy, telemetry, or cloud execution."
NEW_STATUS = "Status: active track - 2 of 9 modules implemented - no live agent, model, gateway, MCP, policy, telemetry, or cloud execution."

REQUIRED_MODULE_MARKERS = (
    '/assets/css/labs.css',
    'lab-detail-shell',
    'lab-status-grid',
    'mobile-study-menu',
    'lab-detail-layout',
    'lab-side-nav',
    'lab-main-panels',
    'Concept Deep Dives',
    'Governance Boundary',
    'Backend exposure = false',
    'Live LLM inference = false',
    'Agent runtime execution = false',
    'Runtime mutation = false',
    'Production enforcement claim = false',
)

FORBIDDEN_MODULE_MARKERS = (
    '<style',
    'class="lab-shell"',
    'class="lab-toc"',
    'comparison-grid',
    'boundary-table',
    'badge-false',
)


def fail(message: str) -> None:
    raise SystemExit(f"ERROR: {message}")


def current_branch() -> str:
    result = subprocess.run(
        ["git", "branch", "--show-current"],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def replace_once_or_already(text: str, old: str, new: str, label: str) -> str:
    if new in text:
        print(f"PASS: {label} already applied")
        return text

    count = text.count(old)
    if count != 1:
        fail(f"{label} expected one old marker, found {count}")

    print(f"UPDATE: {label}")
    return text.replace(old, new, 1)


if current_branch() != EXPECTED_BRANCH:
    fail(
        f"current branch must be {EXPECTED_BRANCH}; found {current_branch()}"
    )

for required_file in (MANIFEST, HOMEPAGE, TRACK, MODULE, METADATA, ARCHITECTURE):
    if not required_file.is_file():
        fail(f"required file not found: {required_file.relative_to(ROOT)}")

status = subprocess.run(
    ["git", "status", "--porcelain"],
    check=True,
    capture_output=True,
    text=True,
).stdout.strip()

if status:
    fail("working tree must be clean before Phase 257 integration")

module_html = MODULE.read_text(encoding="utf-8")
for marker in REQUIRED_MODULE_MARKERS:
    if marker not in module_html:
        fail(f"module marker missing: {marker}")

for marker in FORBIDDEN_MODULE_MARKERS:
    if marker in module_html:
        fail(f"forbidden module marker present: {marker}")

metadata = json.loads(METADATA.read_text(encoding="utf-8"))
if metadata.get("id") != LAB_ID:
    fail("metadata LAB id is incorrect")
if metadata.get("backend_exposure") is not False:
    fail("metadata backend_exposure must be false")
if metadata.get("production_enforcement_claim") is not False:
    fail("metadata production_enforcement_claim must be false")

track_html = TRACK.read_text(encoding="utf-8")
for marker in (
    '<strong>2 of 9</strong>',
    'LAB modules implemented = 2 of 9',
    '/labs/enterprise-agent-developer/task-oriented-conversational-agent-design/',
):
    if marker not in track_html:
        fail(f"track-shell marker missing: {marker}")

shutil.copy2(MANIFEST, Path("/tmp/phase257-manifest.json.bak"))
shutil.copy2(HOMEPAGE, Path("/tmp/phase257-index.html.bak"))

manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
labs = manifest.get("labs")
tracks = manifest.get("tracks")

if not isinstance(labs, list) or not isinstance(tracks, list):
    fail("manifest must contain labs[] and tracks[]")

lab_matches = [record for record in labs if record.get("id") == LAB_ID]
if len(lab_matches) > 1:
    fail(f"duplicate LAB id: {LAB_ID}")
if lab_matches:
    lab_matches[0].update(LAB_RECORD)
    print("PASS: manifest LAB record updated in place")
else:
    labs.append(LAB_RECORD)
    print("ADD: manifest LAB record")

track_matches = [record for record in tracks if record.get("id") == TRACK_ID]
if len(track_matches) != 1:
    fail(f"expected one Enterprise Agent Developer track record, found {len(track_matches)}")

track_record = track_matches[0]
track_record["status"] = "active"
track_record["implemented_modules"] = 2
track_record["planned_modules"] = 9
track_record["backend_exposure"] = False
track_record["production_enforcement_claim"] = False
manifest["last_updated"] = "2026-07-12"

MANIFEST.write_text(
    json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
    encoding="utf-8",
)

html = HOMEPAGE.read_text(encoding="utf-8")
html = replace_once_or_already(
    html,
    '<div class="stat"><strong>64</strong><span>LAB modules</span></div>',
    '<div class="stat"><strong>65</strong><span>LAB modules</span></div>',
    "homepage LAB count 64 -> 65",
)
html = replace_once_or_already(
    html,
    '<div class="stat"><strong>40</strong><span>Total AI modules</span></div>',
    '<div class="stat"><strong>41</strong><span>Total AI modules</span></div>',
    "homepage total AI count 40 -> 41",
)

if '<strong>6</strong><span>Learning paths</span>' not in html:
    fail("homepage learning-path count must remain 6")

if 'data-search="task-oriented and conversational agent design' not in html:
    module1_start = html.find(
        '<article class="lab-card" data-search="enterprise agent developer role architecture'
    )
    if module1_start == -1:
        fail("could not find Module 1 homepage catalog card")

    module1_end = html.find('</article>', module1_start)
    if module1_end == -1:
        fail("could not find Module 1 homepage catalog card end")

    insertion_point = module1_end + len('</article>')
    html = html[:insertion_point] + "\n" + CATALOG_CARD + html[insertion_point:]
    print("ADD: Module 2 homepage catalog card")
else:
    print("PASS: Module 2 homepage catalog card already present")

html = replace_once_or_already(
    html,
    OLD_PREVIEW_COPY,
    NEW_PREVIEW_COPY,
    "active-track preview narrative",
)
html = replace_once_or_already(
    html,
    OLD_STATUS,
    NEW_STATUS,
    "active-track preview progress 1 -> 2",
)

HOMEPAGE.write_text(html, encoding="utf-8")

updated_manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
if sum(record.get("id") == LAB_ID for record in updated_manifest["labs"]) != 1:
    fail("postcondition failed: Module 2 manifest record count")

updated_track = next(
    record for record in updated_manifest["tracks"]
    if record.get("id") == TRACK_ID
)
if updated_track.get("implemented_modules") != 2:
    fail("postcondition failed: track implemented_modules must be 2")
if updated_track.get("planned_modules") != 9:
    fail("postcondition failed: track planned_modules must be 9")

final_html = HOMEPAGE.read_text(encoding="utf-8")
for marker in (
    '<strong>65</strong><span>LAB modules</span>',
    '<strong>6</strong><span>Learning paths</span>',
    '<strong>41</strong><span>Total AI modules</span>',
    'data-search="task-oriented and conversational agent design',
    '/labs/enterprise-agent-developer/task-oriented-conversational-agent-design/',
    NEW_STATUS,
):
    if marker not in final_html:
        fail(f"homepage postcondition missing: {marker}")

subprocess.run(["git", "diff", "--check"], check=True)

changed = subprocess.run(
    ["git", "status", "--short"],
    check=True,
    capture_output=True,
    text=True,
).stdout.strip().splitlines()

expected = {" M index.html", " M manifest.json"}
if set(changed) != expected:
    fail(f"unexpected working-tree scope: {changed}")

print("PASS: Phase 257 homepage and manifest integration applied")
print("EXPECTED CHANGES: index.html and manifest.json only")
print("BACKUPS: /tmp/phase257-index.html.bak and /tmp/phase257-manifest.json.bak")
