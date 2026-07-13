#!/usr/bin/env python3
from __future__ import annotations

import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config" / "lab_navigation_tracks.json"
CSS = ROOT / "assets" / "css" / "labs.css"
TRACK_ID = "ai-security-engineering"
TRACK_TITLE = "AI Security Engineering L2 Track"
TRACK_PATH = "/tracks/ai-security-engineering/"
START_MARKER = "<!-- PHASE 274 TRACK NAVIGATION START -->"
END_MARKER = "<!-- PHASE 274 TRACK NAVIGATION END -->"
SHARED_CSS_MARKER = ".track-module-navigation {"


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def module_url(slug: str) -> str:
    return f"/labs/{TRACK_ID}/{slug}/"


def extract_title(text: str, path: Path) -> str:
    matches = re.findall(r"<h1>(.*?)</h1>", text, flags=re.IGNORECASE | re.DOTALL)
    if len(matches) != 1:
        fail(f"expected exactly one h1: {path.relative_to(ROOT)}")
    title = html.unescape(re.sub(r"\s+", " ", matches[0])).strip()
    if not title:
        fail(f"empty h1 title: {path.relative_to(ROOT)}")
    return title


def module_map(modules: list[str], titles: dict[str, str], current: str) -> str:
    rows: list[str] = []
    for number, slug in enumerate(modules, start=1):
        label = f"{number}. {titles[slug]}"
        if slug == current:
            rows.append(
                f'        <span class="track-module-navigation__current" aria-current="page">{label}</span>'
            )
        else:
            rows.append(f'        <a href="{module_url(slug)}">{label}</a>')
    return "\n".join(rows)


def nav_block(
    modules: list[str],
    titles: dict[str, str],
    current: str,
) -> str:
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
{module_map(modules, titles, current)}
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
        fail("AI Security Engineering track inventory must exist exactly once")

    track = matches[0]
    if track.get("status") != "ready":
        fail("AI Security Engineering track inventory is not ready")
    if track.get("title") != TRACK_TITLE:
        fail("track title differs from the approved inventory")
    if track.get("path") != TRACK_PATH:
        fail("track path differs from the approved inventory")

    modules = track.get("modules")
    if not isinstance(modules, list):
        fail("track modules must be a list")
    if len(modules) != 9 or len(set(modules)) != 9:
        fail("expected nine unique AI Security Engineering modules")

    css = CSS.read_text(encoding="utf-8")
    if SHARED_CSS_MARKER not in css:
        fail("shared track-module-navigation CSS is missing")
    if "@media (max-width: 680px)" not in css:
        fail("shared mobile navigation CSS is missing")

    page_text: dict[str, str] = {}
    titles: dict[str, str] = {}

    for slug in modules:
        page = ROOT / "labs" / TRACK_ID / slug / "index.html"
        if not page.is_file():
            fail(f"missing page: {page.relative_to(ROOT)}")
        text = page.read_text(encoding="utf-8")
        if START_MARKER in text or END_MARKER in text:
            fail(f"Phase 274 navigation already present: {page.relative_to(ROOT)}")
        if '<nav class="track-module-navigation"' in text:
            fail(f"another track navigation block already present: {page.relative_to(ROOT)}")
        if "<script" in text.lower():
            fail(f"JavaScript marker found before repair: {page.relative_to(ROOT)}")
        page_text[slug] = text
        titles[slug] = extract_title(text, page)

    changed: list[str] = []
    for slug in modules:
        page = ROOT / "labs" / TRACK_ID / slug / "index.html"
        updated = insert_after_mobile_menu(
            page_text[slug],
            nav_block(modules, titles, slug),
            page,
        )
        if updated.count(START_MARKER) != 1 or updated.count(END_MARKER) != 1:
            fail(f"navigation marker count invalid: {page.relative_to(ROOT)}")
        if updated.count('aria-current="page"') != 1:
            fail(f"current-module marker count invalid: {page.relative_to(ROOT)}")
        page.write_text(updated, encoding="utf-8")
        changed.append(str(page.relative_to(ROOT)))

    if len(changed) != 9:
        fail(f"unexpected changed-file count: {len(changed)}")

    print("PASS: inserted canonical navigation into 9 AI Security Engineering LABs")
    print("PASS: module position, previous, all modules, next, and expandable map added")
    print("PASS: current module rendered as non-link with aria-current=page")
    print("PASS: existing responsive shared CSS reused without modification")
    print("PASS: no JavaScript added")
    for item in changed:
        print(f"CHANGED: {item}")


if __name__ == "__main__":
    main()
