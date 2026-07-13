#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config" / "lab_navigation_tracks.json"


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def main() -> None:
    data = json.loads(CONFIG.read_text(encoding="utf-8"))

    if data.get("phase") != 272:
        fail("unexpected phase identifier")

    tracks = data.get("tracks")
    standalone = data.get("standalone")
    counts = data.get("counts")

    if not isinstance(tracks, list) or not isinstance(standalone, list):
        fail("tracks and standalone must be lists")

    classified: list[str] = []
    ready_count = 0
    blocked_count = 0

    for track in tracks:
        status = track.get("status")
        if status not in {"ready", "blocked"}:
            fail(f"invalid track status: {track.get('id')}")

        keys = [key for key in ("modules", "module_paths", "candidate_paths") if key in track]
        if len(keys) != 1:
            fail(f"track must expose exactly one module-list key: {track.get('id')}")

        entries = track[keys[0]]
        if len(entries) != len(set(entries)):
            fail(f"duplicate module in track inventory: {track.get('id')}")

        if status == "ready" and keys[0] == "candidate_paths":
            fail(f"ready track cannot use candidate_paths: {track.get('id')}")
        if status == "blocked" and keys[0] != "candidate_paths":
            fail(f"blocked track must use candidate_paths: {track.get('id')}")
        if status == "blocked" and not track.get("reason"):
            fail(f"blocked track missing reason: {track.get('id')}")

        if keys[0] == "modules":
            prefix = ROOT / "labs" / track["id"]
            paths = [str((prefix / item).relative_to(ROOT)) for item in entries]
        else:
            paths = entries

        for relative in paths:
            page = ROOT / relative / "index.html"
            if not page.is_file():
                fail(f"missing LAB page: {page.relative_to(ROOT)}")

        classified.extend(paths)
        if status == "ready":
            ready_count += len(paths)
        else:
            blocked_count += len(paths)

    for relative in standalone:
        page = ROOT / relative / "index.html"
        if not page.is_file():
            fail(f"missing standalone LAB page: {page.relative_to(ROOT)}")

    classified.extend(standalone)

    if len(classified) != len(set(classified)):
        duplicates = sorted({item for item in classified if classified.count(item) > 1})
        fail(f"LAB classified more than once: {duplicates}")

    actual = sorted(
        str(path.parent.relative_to(ROOT))
        for path in (ROOT / "labs").glob("**/index.html")
    )
    expected = sorted(classified)

    if actual != expected:
        fail(
            "inventory mismatch; "
            f"missing={sorted(set(actual) - set(expected))}; "
            f"unexpected={sorted(set(expected) - set(actual))}"
        )

    observed = {
        "ready_tracked": ready_count,
        "blocked_tracked": blocked_count,
        "standalone": len(standalone),
        "total": len(classified),
    }
    if observed != counts:
        fail(f"count mismatch: expected={counts}, observed={observed}")

    if counts != {
        "ready_tracked": 48,
        "blocked_tracked": 25,
        "standalone": 3,
        "total": 76,
    }:
        fail("canonical Phase 272 counts changed unexpectedly")

    prohibited = [
        ROOT / "index.html",
        ROOT / "manifest.json",
        ROOT / "assets" / "css" / "labs.css",
    ]
    for path in prohibited:
        if not path.is_file():
            fail(f"expected production file missing: {path.relative_to(ROOT)}")

    print("PASS: Phase 272 inventory JSON is valid")
    print("PASS: all 76 LAB pages classified exactly once")
    print("PASS: 48 LABs belong to ready ordered tracks")
    print("PASS: 25 LABs remain in two explicitly blocked tracks")
    print("PASS: 3 LABs remain standalone")
    print("PASS: validator performed read-only checks")


if __name__ == "__main__":
    main()
