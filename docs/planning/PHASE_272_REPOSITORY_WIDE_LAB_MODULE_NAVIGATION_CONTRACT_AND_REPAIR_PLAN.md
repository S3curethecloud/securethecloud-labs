# Phase 272 — Repository-Wide LAB Module Navigation Contract and Repair Plan

Status: Planning Gate

## Purpose

Define one deterministic navigation contract for every SecureTheCloud LAB before any production LAB page is modified.

The repository audit established:

```text
LAB pages = 76
Track pages = 8
LABs with Module Map = 0
LABs with Study Menu = 76
LABs with Back to Track = 61
LABs with Previous Module = 0
LABs with Next Module = 0
```

## Root Cause

Track pages expose module lists. Individual LAB pages expose only in-page Study Menu and LAB Navigation links. Cross-module navigation was never standardized in the LAB contract.

## Canonical Tracked-LAB Contract

Every tracked LAB must expose compact sequence navigation and its own unique in-page outline:

```text
Umbrella or track title
Module X of Y
Previous Module
Back to Track
Next Module
Unique This Module's Outline derived from the LAB's existing sections
No full-track module map on an individual LAB
Complete ordered module map retained only on the track page
Existing LAB content retained
```

First module behavior:

```text
Previous Module = unavailable text, not a broken link
```

Last module behavior:

```text
Next Module = unavailable text, not a broken link
```

The complete module map belongs on the track page only. Individual LAB pages must not repeat it. Native HTML and CSS remain sufficient; JavaScript is not required.

## Canonical Standalone-LAB Contract

A standalone LAB must not receive fabricated previous/next links. It must expose:

```text
Back to Labs or learning home
Standalone LAB label
Related learning tracks when explicitly supported
No invented module number
No invented track ownership
```

## Source of Truth

`config/lab_navigation_tracks.json` is the Phase 272 navigation inventory.

The inventory classifies all 76 LAB pages:

```text
Ready tracked LABs = 48
Blocked tracked LABs = 25
Standalone LABs = 3
Total = 76
```

## Ready Tracks

The following track sequences are unambiguous and eligible for later implementation phases:

1. Enterprise Agent Developer — 9 LABs
2. MCP Security Engineering — 9 LABs
3. AI Security Engineering — 9 LABs
4. AI Red Team Scenario Design — 9 LABs
5. AWS Intermediate Identity — 9 LABs
6. AWS Principal Identity — 3 LABs

## Blocked Tracks

### AI Governance Command Center

The track page declares 12 modules but links 14 LAB pages. No generator may select or reorder modules until the canonical track scope and order are reconciled.

### Cloud Security Operations

The track page contains a duplicate overview link and competing module 6–9 sequences. No generator may create previous/next navigation until one canonical ordered sequence is approved.

## Required HTML Markers

Later implementation phases must use stable markers so navigation can be validated and safely replaced:

```html
<!-- STC_TRACK_NAV_START -->
<section class="track-progress-nav" aria-label="Track progress">
  ...
</section>
<!-- STC_TRACK_NAV_END -->
```

The section must include:

```text
track-progress-title
track-progress-position
track-progress-actions
track-module-map
track-module-current
track-module-link
track-module-unavailable
```

## CSS Contract

Later implementation may add shared rules only to `assets/css/labs.css`.

Requirements:

- responsive layout
- keyboard-visible focus
- no color-only current-state indicator
- no horizontal overflow on mobile
- previous/all/next controls remain readable at 320px width
- native details/summary behavior
- no JavaScript dependency
- no inline style blocks

## Fail-Closed Rules

Generation or injection must stop when:

- a LAB belongs to more than one track
- a tracked LAB is absent from the repository
- a track page contains duplicate candidate paths
- declared count differs from the approved ordered sequence
- a blocked track is requested for implementation
- existing STC navigation markers are incomplete
- the current module cannot be located exactly once
- previous or next target does not exist
- a standalone LAB is assigned sequence navigation

## Repair Sequence

```text
Phase 273 — Enterprise Agent Developer navigation repair
Phase 274 — MCP Security Engineering navigation repair
Phase 275 — AI Security Engineering navigation repair
Phase 276 — AI Red Team Scenario Design navigation repair
Phase 277 — AWS Intermediate and Principal Identity navigation repair
Phase 278 — AI Governance canonical module-map reconciliation
Phase 279 — AI Governance navigation repair
Phase 280 — Cloud Security Operations canonical module-map reconciliation
Phase 281 — Cloud Security Operations navigation repair
Phase 282 — Standalone AWS, Azure, and GCP navigation repair
Phase 283 — Repository-wide navigation production quality gate
Phase 284 — Senior Consultant Capstone and complete-track evidence
```

Phase numbers after 272 supersede the earlier provisional sequence because the audit exposed two source-map reconciliation phases.

## Phase 272 Change Boundary

This phase may add only:

```text
config/lab_navigation_tracks.json
docs/planning/PHASE_272_REPOSITORY_WIDE_LAB_MODULE_NAVIGATION_CONTRACT_AND_REPAIR_PLAN.md
scripts/validate_lab_navigation_inventory.py
```

This phase must not modify:

```text
index.html
manifest.json
assets/css/labs.css
tracks/**
labs/**
```

## Governance Boundary

```text
Production LAB changed = false
Production track changed = false
Homepage changed = false
Manifest changed = false
CSS changed = false
Backend exposure changed = false
Runtime execution = false
Cloud deployment = false
Navigation generation execution = false
Planning and read-only validation only = true
```

## Exit Criteria

Phase 272 passes only when:

- inventory JSON is valid
- all 76 LAB pages are classified exactly once
- ready-track sequences contain no duplicate LABs
- blocked tracks remain explicitly blocked
- three standalone LABs are preserved as standalone
- validator is read-only
- repository diff contains only the three approved Phase 272 artifacts

## Phase 275 Information Architecture Correction

The approved learner progression is:

```text
Govern → Secure → Deliver → Operate
```

Enterprise Agent Developer is presented under the **Enterprise Agent Delivery & Consulting** umbrella. Its nine LAB URLs, files, metadata, architecture documents, evidence, and curriculum order remain unchanged. The homepage groups the nine LAB cards behind one delivery-path disclosure. The track page remains the sole owner of the complete nine-module map.
