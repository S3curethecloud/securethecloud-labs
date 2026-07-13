#!/usr/bin/env python3
from __future__ import annotations

import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
START_HERE = ROOT / "start-here" / "index.html"
CONFIG = ROOT / "config" / "lab_navigation_tracks.json"
PLAN = ROOT / "docs" / "planning" / "PHASE_272_REPOSITORY_WIDE_LAB_MODULE_NAVIGATION_CONTRACT_AND_REPAIR_PLAN.md"
TRACK_ID = "enterprise-agent-developer"
START_MARKER = "<!-- PHASE 273 TRACK NAVIGATION START -->"
END_MARKER = "<!-- PHASE 273 TRACK NAVIGATION END -->"
HOME_START = "<!-- PHASE 275 ENTERPRISE AGENT DELIVERY UMBRELLA START -->"
HOME_END = "<!-- PHASE 275 ENTERPRISE AGENT DELIVERY UMBRELLA END -->"
CSS_START = "/* PHASE 275 ENTERPRISE AGENT DELIVERY UMBRELLA START */"
CSS_END = "/* PHASE 275 ENTERPRISE AGENT DELIVERY UMBRELLA END */"


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def read(path: Path) -> str:
    if not path.is_file():
        fail(f"missing file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def write_if_changed(path: Path, before: str, after: str) -> bool:
    if before == after:
        return False
    path.write_text(after, encoding="utf-8")
    return True


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        fail(f"{label}: expected one match, found {count}")
    return text.replace(old, new, 1)


def track_data() -> tuple[list[str], dict[str, str]]:
    data = json.loads(read(CONFIG))
    track = next((item for item in data["tracks"] if item["id"] == TRACK_ID), None)
    if not track or track.get("status") != "ready":
        fail("enterprise-agent-developer track is not ready")
    modules = track.get("modules")
    if not isinstance(modules, list) or len(modules) != 9 or len(set(modules)) != 9:
        fail("enterprise-agent-developer module inventory is not exactly nine unique modules")
    titles: dict[str, str] = {}
    for slug in modules:
        page = ROOT / "labs" / TRACK_ID / slug / "index.html"
        text = read(page)
        matches = re.findall(r"<h1>(.*?)</h1>", text, flags=re.IGNORECASE | re.DOTALL)
        if len(matches) != 1:
            fail(f"expected one h1 in {page.relative_to(ROOT)}")
        titles[slug] = html.unescape(re.sub(r"\s+", " ", matches[0])).strip()
    return modules, titles


def compact_navigation(modules: list[str], titles: dict[str, str], position: int) -> str:
    slug = modules[position - 1]
    previous_html = (
        '<span class="track-module-navigation__disabled" aria-disabled="true">&larr; Previous Module</span>'
        if position == 1
        else f'<a rel="prev" href="/labs/{TRACK_ID}/{modules[position - 2]}/">&larr; Previous Module</a>'
    )
    next_html = (
        '<span class="track-module-navigation__disabled" aria-disabled="true">Next Module &rarr;</span>'
        if position == len(modules)
        else f'<a rel="next" href="/labs/{TRACK_ID}/{modules[position]}/">Next Module &rarr;</a>'
    )
    return f'''{START_MARKER}
    <nav class="track-module-navigation" aria-label="Enterprise Agent Developer L2 Track module navigation">
      <div class="track-module-navigation__header">
        <strong>Enterprise Agent Delivery &amp; Consulting</strong>
        <span class="track-module-navigation__position">Module {position} of {len(modules)} · {html.escape(titles[slug])}</span>
      </div>
      <div class="track-module-navigation__controls">
        {previous_html}
        <a href="/tracks/enterprise-agent-developer/">Back to Track</a>
        {next_html}
      </div>
    </nav>
    {END_MARKER}'''


def repair_lab_pages(modules: list[str], titles: dict[str, str]) -> list[Path]:
    changed: list[Path] = []
    for position, slug in enumerate(modules, start=1):
        path = ROOT / "labs" / TRACK_ID / slug / "index.html"
        before = read(path)
        if before.count(START_MARKER) != 1 or before.count(END_MARKER) != 1:
            fail(f"incomplete Phase 273 markers: {path.relative_to(ROOT)}")
        pattern = re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER)
        after, count = re.subn(
            pattern,
            compact_navigation(modules, titles, position),
            before,
            count=1,
            flags=re.DOTALL,
        )
        if count != 1:
            fail(f"unable to replace track map: {path.relative_to(ROOT)}")
        after = after.replace(
            '<p class="mobile-study-menu-title">Study Menu</p>',
            '<p class="mobile-study-menu-title">This Module\'s Outline</p>',
            1,
        )
        after = after.replace(
            '<strong>LAB Navigation</strong>',
            '<strong>This Module\'s Outline</strong>',
            1,
        )
        if "View complete Module Map" in after:
            fail(f"full map remains in individual LAB: {path.relative_to(ROOT)}")
        if after.count('href="/tracks/enterprise-agent-developer/"') != 1:
            fail(f"Back to Track link count invalid: {path.relative_to(ROOT)}")
        if write_if_changed(path, before, after):
            changed.append(path)
    return changed


def repair_homepage() -> Path:
    before = read(INDEX)
    if HOME_START in before or CSS_START in before:
        fail("Phase 275 homepage markers already exist")

    old_card_pattern = re.compile(
        r'\s*<article class="track-card">\s*'
        r'<span>L2 · active</span>\s*'
        r'<h3>Enterprise Agent Developer L2 Track</h3>.*?'
        r'<a href="/tracks/enterprise-agent-developer/">Open Track →</a>\s*'
        r'</article>',
        flags=re.DOTALL,
    )
    replacement_card = '''
          <article class="track-card">
            <span>Deliver · complete L2 path</span>
            <h3>Enterprise Agent Delivery &amp; Consulting</h3>
            <p>Client-facing architecture, agent engineering, RAG, tool use, orchestration, gateway and MCP integration, policy, Responsible AI, observability, cloud delivery, and consulting leadership.</p>
            <a href="/tracks/enterprise-agent-developer/">Open Delivery Path →</a>
          </article>'''
    after, count = old_card_pattern.subn(replacement_card, before, count=1)
    if count != 1:
        fail(f"homepage track card replacement count was {count}")

    first_token = '<article class="lab-card" data-search="enterprise agent developer role architecture'
    last_link = '<a href="/labs/enterprise-agent-developer/senior-consultant-enterprise-agent-delivery-capstone/">Open Lab →</a>'
    start = after.find(first_token)
    if start < 0:
        fail("unable to locate first Enterprise Agent Developer catalog card")
    article_start = after.rfind("          <article", 0, start + len(first_token))
    if article_start < 0:
        fail("unable to locate first Enterprise Agent Developer article boundary")
    last = after.find(last_link, article_start)
    if last < 0:
        fail("unable to locate final Enterprise Agent Developer catalog card")
    article_end = after.find("</article>", last)
    if article_end < 0:
        fail("unable to locate final Enterprise Agent Developer article boundary")
    article_end += len("</article>")
    module_cards = after[article_start:article_end]
    if module_cards.count('Track: enterprise-agent-developer') != 9:
        fail("catalog block does not contain exactly nine Enterprise Agent Developer cards")

    umbrella = f'''{HOME_START}
<section class="lab-section delivery-path-section" id="enterprise-agent-delivery-consulting">
  <div class="section-heading">
    <p class="eyebrow">Deliver · Applied Client Path</p>
    <h2>Enterprise Agent Delivery &amp; Consulting</h2>
    <p>Apply governed AI architecture in client-facing delivery work—from discovery and workflow design through agent engineering, integration, cloud delivery, executive communication, and evidence-backed readiness decisions.</p>
  </div>
  <article class="delivery-path-card">
    <div>
      <p class="lab-card-meta">ENTERPRISE AGENT DEVELOPER · COMPLETE L2 TRACK</p>
      <h3>Enterprise Agent Developer L2 Track</h3>
      <p>One coherent nine-module learning path. Open the track for the complete curriculum map, or expand the catalog list below only when you need a specific LAB.</p>
    </div>
    <a class="primary-link" href="/tracks/enterprise-agent-developer/">Open Enterprise Agent Delivery Path →</a>
  </article>
  <details class="delivery-path-modules">
    <summary>View 9 individual LAB modules</summary>
    <div class="lab-grid">
{module_cards}
    </div>
  </details>
</section>
{HOME_END}'''
    after = after[:article_start] + umbrella + after[article_end:]

    css = f'''\n{CSS_START}
.delivery-path-section {{
  grid-column: 1 / -1;
  margin: 1.5rem 0 2rem;
  padding: clamp(1rem, 3vw, 1.5rem);
  border: 1px solid rgba(56, 189, 248, 0.28);
  border-radius: 24px;
  background: linear-gradient(135deg, rgba(8, 47, 73, 0.36), rgba(15, 23, 42, 0.82));
}}
.delivery-path-card {{
  display: grid;
  grid-template-columns: minmax(0, 1fr) auto;
  gap: 1.25rem;
  align-items: center;
  padding: 1.25rem;
  border: 1px solid rgba(148, 163, 184, 0.18);
  border-radius: 20px;
  background: rgba(2, 6, 23, 0.5);
}}
.delivery-path-card p {{ margin-bottom: 0; }}
.delivery-path-modules {{ margin-top: 1rem; }}
.delivery-path-modules > summary {{
  cursor: pointer;
  color: #38bdf8;
  font-weight: 900;
  padding: 0.85rem 0;
}}
.delivery-path-modules .lab-grid {{ margin-top: 0.75rem; }}
@media (max-width: 760px) {{
  .delivery-path-card {{ grid-template-columns: 1fr; }}
}}
{CSS_END}\n'''
    closing_style = after.find("</style>")
    if closing_style < 0:
        fail("homepage closing style tag not found")
    after = after[:closing_style] + css + after[closing_style:]

    if after.count(HOME_START) != 1 or after.count(HOME_END) != 1:
        fail("homepage umbrella marker count invalid")
    if after.count('Track: enterprise-agent-developer') != 9:
        fail("homepage lost Enterprise Agent Developer catalog cards")
    if write_if_changed(INDEX, before, after):
        return INDEX
    fail("homepage did not change")


def repair_start_here() -> Path:
    before = read(START_HERE)
    after = before
    after = replace_once(
        after,
        '<div><span>Next Step</span><strong>AI Security Engineering</strong></div>',
        '<div><span>Progression</span><strong>Govern → Secure → Deliver → Operate</strong></div>',
        "Start Here status progression",
    )
    recommended_pattern = re.compile(
        r'<div class="artifact-grid">\s*'
        r'<a class="artifact-card" href="/tracks/ai-governance-command-center/">.*?'
        r'</div>\s*'
        r'</section>',
        flags=re.DOTALL,
    )
    recommended = '''<div class="artifact-grid">
            <a class="artifact-card" href="/tracks/ai-governance-command-center/">
              <strong>1. Govern — AI Governance Command Center</strong>
              <span>Learn authority, risk tiering, policy gates, human approval, audit evidence, cost governance, and executive boundaries.</span>
            </a>
            <a class="artifact-card" href="/tracks/ai-security-engineering/">
              <strong>2. Secure — AI Security Engineering L2 Track</strong>
              <span>Engineer prompt, tool, retrieval, output, runtime, abuse-control, and testing boundaries for secure AI systems.</span>
            </a>
            <a class="artifact-card" href="/tracks/enterprise-agent-developer/">
              <strong>3. Deliver — Enterprise Agent Delivery &amp; Consulting</strong>
              <span>Apply architecture in client-facing discovery, agent engineering, integration, governance, cloud delivery, stakeholder communication, and readiness decisions.</span>
            </a>
            <a class="artifact-card" href="/tracks/cloud-security-operations/">
              <strong>4. Operate — Cloud Security Operations L2 Track</strong>
              <span>Continue into detection, triage, IAM activity review, workload signals, incident evidence, escalation narratives, and executive security summaries.</span>
            </a>
          </div>
        </section>'''
    after, count = recommended_pattern.subn(recommended, after, count=1)
    if count != 1:
        fail(f"Start Here recommended-flow replacement count was {count}")
    old_cascade = '''Start Here
→ AI Governance Command Center
→ AI Security Engineering L2 Track
→ next specialized cloud/security track
→ evidence-backed portfolio narrative'''
    new_cascade = '''Start Here
→ Govern: AI Governance Command Center
→ Secure: AI Security Engineering L2 Track
→ Deliver: Enterprise Agent Delivery &amp; Consulting
→ Operate: Cloud Security Operations L2 Track
→ evidence-backed portfolio narrative'''
    after = replace_once(after, old_cascade, new_cascade, "Start Here portfolio cascade")
    after = after.replace(
        '<span class="pill">2 AI learning paths</span>',
        '<span class="pill">Govern → Secure → Deliver → Operate</span>',
        1,
    )
    if after.count("Enterprise Agent Delivery &amp; Consulting") < 2:
        fail("Start Here delivery path not represented")
    if write_if_changed(START_HERE, before, after):
        return START_HERE
    fail("Start Here did not change")


def repair_contract_files() -> list[Path]:
    changed: list[Path] = []
    before = read(CONFIG)
    data = json.loads(before)
    data["phase"] = 275
    data["contract"] = {
        "track_page": "complete ordered module map",
        "tracked_lab": "previous + position + back_to_track + next + unique_module_outline",
        "current_module_not_linked": True,
        "full_track_map_on_individual_lab": False,
        "javascript_required": False,
        "runtime_change": False,
    }
    after = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    if write_if_changed(CONFIG, before, after):
        changed.append(CONFIG)

    before = read(PLAN)
    after = before
    after = replace_once(
        after,
        "Every tracked LAB must expose:",
        "Every tracked LAB must expose compact sequence navigation and its own unique in-page outline:",
        "planning contract heading",
    )
    old_contract = '''Track title
Module X of Y
Previous Module
All Modules
Next Module
Expandable full Module Map
Current module identified and not self-linked
Existing Study Menu retained
Existing LAB Navigation retained'''
    new_contract = '''Umbrella or track title
Module X of Y
Previous Module
Back to Track
Next Module
Unique This Module's Outline derived from the LAB's existing sections
No full-track module map on an individual LAB
Complete ordered module map retained only on the track page
Existing LAB content retained'''
    after = replace_once(after, old_contract, new_contract, "planning contract body")
    after = after.replace(
        "The full module map must use native HTML `details` and `summary`. JavaScript is not required.",
        "The complete module map belongs on the track page only. Individual LAB pages must not repeat it. Native HTML and CSS remain sufficient; JavaScript is not required.",
        1,
    )
    phase_note = '''\n## Phase 275 Information Architecture Correction\n\nThe approved learner progression is:\n\n```text\nGovern → Secure → Deliver → Operate\n```\n\nEnterprise Agent Developer is presented under the **Enterprise Agent Delivery & Consulting** umbrella. Its nine LAB URLs, files, metadata, architecture documents, evidence, and curriculum order remain unchanged. The homepage groups the nine LAB cards behind one delivery-path disclosure. The track page remains the sole owner of the complete nine-module map.\n'''
    if "## Phase 275 Information Architecture Correction" not in after:
        after += phase_note
    if write_if_changed(PLAN, before, after):
        changed.append(PLAN)
    return changed


def main() -> None:
    modules, titles = track_data()
    changed = []
    changed.extend(repair_lab_pages(modules, titles))
    changed.append(repair_homepage())
    changed.append(repair_start_here())
    changed.extend(repair_contract_files())

    unique = sorted({path.relative_to(ROOT) for path in changed}, key=str)
    expected = 13
    if len(unique) != expected:
        fail(f"expected {expected} changed production/planning files, observed {len(unique)}: {unique}")

    print("PASS: Govern → Secure → Deliver → Operate hierarchy applied")
    print("PASS: Enterprise Agent Delivery & Consulting umbrella created")
    print("PASS: nine LAB URLs and content preserved")
    print("PASS: complete nine-module map retained on track page only")
    print("PASS: individual LABs now use compact previous/back/next navigation")
    print("PASS: individual LABs retain unique in-page outlines")
    print("PASS: no JavaScript, backend, runtime, manifest, metadata, or architecture changes")
    for path in unique:
        print(f"CHANGED: {path}")


if __name__ == "__main__":
    main()
