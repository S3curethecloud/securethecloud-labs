#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config" / "lab_navigation_tracks.json"
CSS = ROOT / "assets" / "css" / "labs.css"
TRACK_ID = "enterprise-agent-developer"
TRACK_TITLE = "Enterprise Agent Developer L2 Track"
TRACK_PATH = "/tracks/enterprise-agent-developer/"
START_MARKER = "<!-- PHASE 273 TRACK NAVIGATION START -->"
END_MARKER = "<!-- PHASE 273 TRACK NAVIGATION END -->"
CSS_START = "/* PHASE 273 ENTERPRISE AGENT LAB MODULE NAVIGATION START */"
CSS_END = "/* PHASE 273 ENTERPRISE AGENT LAB MODULE NAVIGATION END */"

TITLES = {
    "enterprise-agent-developer-role-architecture": "Enterprise Agent Developer Role Architecture",
    "task-oriented-conversational-agent-design": "Task-Oriented and Conversational Agent Design",
    "enterprise-rag-tool-use-engineering": "Enterprise RAG and Tool-Use Engineering",
    "deterministic-routing-multi-agent-orchestration": "Deterministic Routing and Multi-Agent Orchestration",
    "enterprise-gateway-mcp-registry-api-contracts": "Enterprise Gateway, MCP, Registry, and API Contracts",
    "opa-policy-responsible-ai-controls": "OPA Policy Enforcement and Responsible AI Controls",
    "opentelemetry-slo-cost-performance-engineering": "OpenTelemetry, SLO, Cost, and Performance Engineering",
    "cloud-delivery-containers-cicd-platform-collaboration": "Cloud Delivery, Containers, CI/CD, and Platform Collaboration",
    "senior-consultant-enterprise-agent-delivery-capstone": "Senior Consultant Enterprise Agent Delivery Capstone",
}

CSS_BLOCK = r'''/* PHASE 273 ENTERPRISE AGENT LAB MODULE NAVIGATION START */
.track-module-navigation {
  margin: 1rem 0 1.5rem;
  padding: 1rem;
  border: 1px solid rgba(56, 189, 248, 0.28);
  border-radius: 1rem;
  background: rgba(15, 23, 42, 0.76);
}

.track-module-navigation__header {
  display: flex;
  justify-content: space-between;
  gap: 1rem;
  align-items: baseline;
  margin-bottom: 0.85rem;
}

.track-module-navigation__header strong {
  color: #f8fafc;
}

.track-module-navigation__position {
  color: #38bdf8;
  font-size: 0.86rem;
  font-weight: 800;
}

.track-module-navigation__controls {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 0.65rem;
}

.track-module-navigation__controls a,
.track-module-navigation__controls span {
  display: flex;
  min-height: 2.8rem;
  align-items: center;
  justify-content: center;
  border: 1px solid rgba(148, 163, 184, 0.26);
  border-radius: 0.75rem;
  padding: 0.65rem 0.8rem;
  text-align: center;
  text-decoration: none;
  background: rgba(2, 6, 23, 0.42);
}

.track-module-navigation__controls a:hover {
  border-color: rgba(56, 189, 248, 0.72);
  color: #e0f2fe;
  text-decoration: none;
}

.track-module-navigation__disabled {
  color: #64748b;
  cursor: not-allowed;
}

.track-module-navigation details {
  margin-top: 0.8rem;
  border-top: 1px solid rgba(148, 163, 184, 0.18);
  padding-top: 0.8rem;
}

.track-module-navigation summary {
  cursor: pointer;
  color: #dbeafe;
  font-weight: 800;
}

.track-module-navigation__map {
  display: grid;
  gap: 0.5rem;
  margin-top: 0.75rem;
}

.track-module-navigation__map a,
.track-module-navigation__current {
  display: block;
  border-radius: 0.65rem;
  padding: 0.6rem 0.75rem;
  text-decoration: none;
}

.track-module-navigation__map a {
  border: 1px solid rgba(148, 163, 184, 0.18);
  background: rgba(2, 6, 23, 0.3);
}

.track-module-navigation__map a:hover {
  border-color: rgba(56, 189, 248, 0.6);
  text-decoration: none;
}

.track-module-navigation__current {
  border: 1px solid rgba(34, 211, 238, 0.75);
  background: rgba(8, 47, 73, 0.45);
  color: #ecfeff;
  font-weight: 800;
}

@media (max-width: 680px) {
  .track-module-navigation__header {
    display: block;
  }

  .track-module-navigation__position {
    display: block;
    margin-top: 0.25rem;
  }

  .track-module-navigation__controls {
    grid-template-columns: 1fr;
  }
}
/* PHASE 273 ENTERPRISE AGENT LAB MODULE NAVIGATION END */'''


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def module_url(slug: str) -> str:
    return f"/labs/{TRACK_ID}/{slug}/"


def module_map(modules: list[str], current: str) -> str:
    rows = []
    for number, slug in enumerate(modules, start=1):
        label = f"{number}. {TITLES[slug]}"
        if slug == current:
            rows.append(
                f'        <span class="track-module-navigation__current" aria-current="page">{label}</span>'
            )
        else:
            rows.append(f'        <a href="{module_url(slug)}">{label}</a>')
    return "\n".join(rows)


def nav_block(modules: list[str], current: str) -> str:
    index = modules.index(current)
    number = index + 1
    previous = modules[index - 1] if index > 0 else None
    following = modules[index + 1] if index + 1 < len(modules) else None

    previous_control = (
        f'<a rel="prev" href="{module_url(previous)}">&larr; Previous Module</a>'
        if previous
        else '<span class="track-module-navigation__disabled" aria-disabled="true">&larr; Previous Module</span>'
    )
    next_control = (
        f'<a rel="next" href="{module_url(following)}">Next Module &rarr;</a>'
        if following
        else '<span class="track-module-navigation__disabled" aria-disabled="true">Next Module &rarr;</span>'
    )

    return f'''{START_MARKER}
    <nav class="track-module-navigation" aria-label="{TRACK_TITLE} module navigation">
      <div class="track-module-navigation__header">
        <strong>{TRACK_TITLE}</strong>
        <span class="track-module-navigation__position">Module {number} of {len(modules)}</span>
      </div>
      <div class="track-module-navigation__controls">
        {previous_control}
        <a href="{TRACK_PATH}">All Modules</a>
        {next_control}
      </div>
      <details>
        <summary>View complete Module Map</summary>
        <div class="track-module-navigation__map">
{module_map(modules, current)}
        </div>
      </details>
    </nav>
    {END_MARKER}'''


def insert_after_mobile_menu(text: str, block: str, path: Path) -> str:
    marker = '<section class="mobile-study-menu">'
    start = text.find(marker)
    if start < 0:
        fail(f"mobile study menu marker missing: {path.relative_to(ROOT)}")
    close = text.find("</section>", start)
    if close < 0:
        fail(f"mobile study menu closing tag missing: {path.relative_to(ROOT)}")
    close += len("</section>")
    return text[:close] + "\n\n    " + block + text[close:]


def main() -> None:
    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    matches = [item for item in config["tracks"] if item.get("id") == TRACK_ID]
    if len(matches) != 1:
        fail("Enterprise Agent Developer track inventory must exist exactly once")
    track = matches[0]
    if track.get("status") != "ready":
        fail("Enterprise Agent Developer track inventory is not ready")
    modules = track.get("modules")
    if modules != list(TITLES):
        fail("track order and canonical title order differ")
    if len(modules) != 9 or len(set(modules)) != 9:
        fail("expected nine unique modules")

    changed = []
    for slug in modules:
        page = ROOT / "labs" / TRACK_ID / slug / "index.html"
        if not page.is_file():
            fail(f"missing page: {page.relative_to(ROOT)}")
        text = page.read_text(encoding="utf-8")
        if START_MARKER in text or END_MARKER in text:
            fail(f"navigation already present: {page.relative_to(ROOT)}")
        if "<script" in text.lower():
            fail(f"JavaScript marker found before repair: {page.relative_to(ROOT)}")
        updated = insert_after_mobile_menu(text, nav_block(modules, slug), page)
        if updated.count(START_MARKER) != 1 or updated.count(END_MARKER) != 1:
            fail(f"navigation marker count invalid: {page.relative_to(ROOT)}")
        page.write_text(updated, encoding="utf-8")
        changed.append(str(page.relative_to(ROOT)))

    css = CSS.read_text(encoding="utf-8")
    if CSS_START in css or CSS_END in css:
        fail("Phase 273 CSS block already present")
    CSS.write_text(css.rstrip() + "\n\n" + CSS_BLOCK + "\n", encoding="utf-8")
    changed.append(str(CSS.relative_to(ROOT)))

    if len(changed) != 10:
        fail(f"unexpected changed-file count: {len(changed)}")

    print("PASS: inserted canonical navigation into 9 Enterprise Agent Developer LABs")
    print("PASS: module position, previous, all modules, next, and expandable map added")
    print("PASS: current module rendered as non-link with aria-current=page")
    print("PASS: responsive CSS block appended")
    print("PASS: no JavaScript added")
    for item in changed:
        print(f"CHANGED: {item}")


if __name__ == "__main__":
    main()
