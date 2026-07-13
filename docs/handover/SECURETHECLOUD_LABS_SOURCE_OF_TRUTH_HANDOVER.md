# SecureTheCloud Labs — Source of Truth and Agent Handover

Status: Canonical Handover Document  
Repository: securethecloud-labs  
Production Site: https://labs.securethecloud.dev  
GitHub Remote: https://github.com/S3curethecloud/securethecloud-labs.git  
Branch: main  

---

## 1. Project Mission

SecureTheCloud Labs is a production-facing learning platform for cloud security, AI security, Zero Trust, governance, and enterprise architecture labs.

The platform exists to demonstrate the ability to:

- Build structured cloud and AI security learning tracks.
- Convert advanced security architecture concepts into repeatable LAB modules.
- Maintain production-grade governance boundaries.
- Validate every change through deterministic quality gates.
- Preserve evidence for major milestones.
- Keep backend exposure at zero unless explicitly approved.
- Build recruiter-visible and interview-ready technical artifacts.

This repository should be treated as a portfolio-grade learning operating system, not a simple static website.

---

## 2. Current Confirmed Platform State

The MCP Security Engineering L2 Track is the canonical completed example.

Confirmed production state:

```text
LAB modules = 63
Learning paths = 5
Total AI modules = 39
Complete learning paths = 5
Backend exposure = 0

Confirmed MCP state:

MCP Security Engineering L2 Track = complete
Implemented modules = 9 of 9
Locked modules = 9 of 9
Homepage visual state = complete
Backend exposure = false
Live MCP integration = false
Runtime mutation = false
Production enforcement claim = false
3. Major Milestone Achieved
Milestone: MCP Security Engineering L2 Track Completed

The repository successfully completed a 9-module MCP Security Engineering L2 learning path.

Final module list:

1. MCP Security Engineering Overview
2. MCP Server Trust Boundary Design
3. MCP Tool Authority and Permission Scope
4. MCP Context Injection Risk Design
5. MCP Data Exposure Scenario Design
6. MCP Approval Gate and Human-in-the-Loop Controls
7. MCP Agent Workflow and Tool Abuse Review
8. MCP Evidence Capture and Control Mapping
9. MCP Security Engineering Capstone

The MCP track is now the gold-standard reference for future SecureTheCloud Labs learning paths.

4. Core Repository Structure

Important repo paths:

index.html
manifest.json
assets/css/labs.css
tracks/
  mcp-security-engineering/
    index.html
labs/
  mcp-security-engineering/
    <module-slug>/
      index.html
      metadata.json
      architecture.md
docs/
  evidence/
  handover/

LAB module pages must use the shared Cloud Ops stylesheet:

<link rel="stylesheet" href="/assets/css/labs.css" />

Do not use inline style blocks for LAB pages.

5. Cloud Ops LAB Page Standard

Every production LAB page must use the Cloud Ops layout.

Required markers:

/assets/css/labs.css
lab-detail-shell
lab-status-grid
mobile-study-menu
lab-detail-layout
lab-side-nav
lab-main-panels
lab-panel
Concept Deep Dives
Governance Boundary

Old/problem markers must be absent:

lab-shell
lab-toc
comparison-grid
boundary-table
badge-false
<style>

If a module page returns <style> in production verification, it may indicate an old route, fallback page, or missing production module file.

6. Governance Boundary Standard

Every LAB module must clearly state what it does and does not do.

Required boundary language:

Backend exposure = false
Public backend exposed = false
MCP server execution = false
MCP client execution = false
Live MCP integration = false
Live tool invocation = false
Live API call execution = false
Customer data access = false
Credential handling = false
Secret handling = false
Runtime mutation = false
Production enforcement claim = false

Module-specific examples:

Data export execution = false
Approval execution = false
Tool abuse execution = false
Evidence capture execution = false
Capstone runtime execution = false

The repo must not imply production enforcement, live agent runtime, customer data processing, credential handling, or backend integration unless explicitly implemented and verified.

7. How to Create a New Learning Track

Use MCP Security Engineering L2 Track as the model.

Before creating files, define:

Track name
Track level
Domain
Audience
Number of modules
Final capstone or assessment
Runtime boundary
Backend exposure rule
Production claim rule

Example:

Track name: MCP Security Engineering L2 Track
Level: L2
Domain: AI Security
Modules: 9
Final module: Capstone
Runtime: read-only learning
Backend exposure: false
Production enforcement claim: false

Recommended 9-module learning arc:

1. Foundation / Overview
2. Core architecture boundary
3. Authority, access, or permission model
4. Main risk pattern
5. Data risk or exposure scenario
6. Governance or approval control
7. Abuse, misuse, or operational risk
8. Evidence and control mapping
9. Capstone
8. How to Create a Detailed LAB Module

Each module requires three files:

labs/<track-slug>/<module-slug>/index.html
labs/<track-slug>/<module-slug>/metadata.json
labs/<track-slug>/<module-slug>/architecture.md

A strong LAB module should include:

Hero
Status grid
Mobile study menu
Side navigation
Overview
Concept Deep Dives
Visual Model
Example Scenario
High-Risk Anti-Pattern
Governance Boundary

A capstone module should include:

Overview
Concept Deep Dives
Visual Capstone Model
Capstone Scenario
Expected Deliverable
Governance Boundary

Concept Deep Dives should answer:

What is the concept?
Why does it matter?
What can go wrong?
What should reviewers inspect?
What controls reduce the risk?
What evidence should be captured?
9. Visual Model Pattern

Use existing HTML/CSS classes.

Example pattern:

<div class="workflow-board">
  <div class="workflow-node">
    <strong>Step Name</strong>
    <span>Description</span>
  </div>
  <span class="workflow-arrow">→</span>
  <div class="workflow-node warning">
    <strong>Risk Step</strong>
    <span>Description</span>
  </div>
  <span class="workflow-arrow">→</span>
  <div class="workflow-node success">
    <strong>Safe Outcome</strong>
    <span>Description</span>
  </div>
</div>

Allowed semantic node classes:

workflow-node
workflow-node warning
workflow-node danger
workflow-node success
10. Scenario Pattern

Use a structured scenario grid.

Recommended structure:

<div class="scenario-grid">
  <div class="scenario-card">
    <strong>Objective</strong>
    <p>...</p>
  </div>
  <div class="scenario-card">
    <strong>Scope</strong>
    <p>...</p>
  </div>
  <div class="scenario-card">
    <strong>Expected Control</strong>
    <p>...</p>
  </div>
  <div class="scenario-card">
    <strong>Evidence</strong>
    <p>...</p>
  </div>
</div>

Each scenario should explain:

Objective
Scope
Expected control
Evidence
Risk boundary
11. Metadata Standard

Each module must have a metadata.json.

MCP-style example:

{
  "id": "mcp-evidence-capture-control-mapping",
  "title": "MCP Evidence Capture and Control Mapping",
  "cloud": "mcp-security-engineering",
  "domain": "AI Security",
  "track": "mcp-security-engineering",
  "level": "L2",
  "status": "implemented",
  "runtime": "read-only",
  "path": "/labs/mcp-security-engineering/mcp-evidence-capture-control-mapping/",
  "backend_exposure": false,
  "mcp_server_execution": false,
  "mcp_client_execution": false,
  "live_tool_invocation": false,
  "evidence_capture_execution": false,
  "credential_handling": false,
  "customer_data_access": false,
  "runtime_mutation": false,
  "production_enforcement_claim": false
}
12. Architecture Note Standard

Each module must have an architecture.md.

Required sections:

# <Module Title> — Architecture Note

## Purpose

## Runtime Boundary

## Implementation Scope

## Safety Model

The architecture note should explicitly state:

This LAB is static HTML/CSS/JSON content only.
Backend exposure = false
No live server is started.
No live tool is invoked.
No credentials are handled.
No customer data is accessed.
No production enforcement is claimed.
13. Manifest Update Standard

Every module must be added to manifest.json.

Module record pattern:

{
  "id": "<module-slug>",
  "title": "<Module Title>",
  "cloud": "<track-slug>",
  "domain": "<Domain>",
  "track": "<track-slug>",
  "level": "L2",
  "status": "implemented",
  "path": "/labs/<track-slug>/<module-slug>/",
  "backend_exposure": false
}

Track record must update:

{
  "id": "<track-slug>",
  "implemented_modules": <current-count>,
  "planned_modules": <total-count>,
  "status": "active",
  "backend_exposure": false
}

When a track is complete:

{
  "status": "complete",
  "implemented_modules": 9,
  "planned_modules": 9,
  "backend_exposure": false
}
14. Track Shell Update Standard

Each learning path has a track shell:

tracks/<track-slug>/index.html

The track shell must update:

Status
Module count
Mobile study menu links
Desktop module cards
Boundary block

Active track example:

<div><span>Status</span><strong>Active Track</strong></div>
<div><span>Modules</span><strong>8 of 9</strong></div>

Complete track example:

<div><span>Status</span><strong>Complete Track</strong></div>
<div><span>Modules</span><strong>9 of 9</strong></div>

Track shell boundary block must include:

LAB modules implemented = 9 of 9
MCP server execution = false
MCP client execution = false
Live tool invocation = false
Credential handling = false
Customer data access = false
Runtime mutation = false
Production enforcement claim = false
15. Homepage Update Standard

Homepage counts change only when modules or track completion status changes.

For normal module addition:

LAB modules +1
Total AI modules +1
Learning paths unchanged
Complete learning paths unchanged
Backend exposure unchanged

For final capstone that completes a learning path:

LAB modules +1
Total AI modules +1
Complete learning paths +1
Learning paths unchanged
Backend exposure unchanged

MCP final state:

LAB modules = 63
Learning paths = 5
Total AI modules = 39
Complete learning paths = 5
Backend exposure = 0

Active homepage state:

ACTIVE LEARNING PATH
ACTIVE
MCP SECURITY - ACTIVE TRACK
Status: active track - X of 9 modules implemented - no live MCP integration.

Complete homepage state:

COMPLETE LEARNING PATH
COMPLETE
MCP SECURITY - COMPLETE TRACK
Status: complete track - 9 of 9 modules implemented - no live MCP integration.

Do not forget to update both the visible heading and the badge.

16. Standard Phase Lifecycle
Implementation Phase

Example:

Phase 250 — Add MCP Security Engineering Capstone L2 LAB

Implementation does:

Create module directory
Create index.html
Create metadata.json
Create architecture.md
Update track shell
Update manifest
Update homepage
Run local QA
Commit
Push
Run production verification
Evidence Phase

Example:

Phase 251 — Record MCP Security Engineering Capstone L2 LAB Evidence

Evidence does:

Create docs/evidence/PHASE_<N>_*.md
Record production verification
Record source commit
Record governance boundaries
Record manifest state
Commit evidence only
Push
Production Quality Gate Phase

Example:

Phase 253 — MCP Security Engineering Complete Track Production Quality Gate

Production quality gate does:

No code changes
Verify homepage
Verify track shell
Verify all module pages
Verify all governance boundaries
Verify manifest
Verify no old classes
Verify git clean
Production Quality Gate Evidence Phase

Example:

Phase 254 — Record MCP Security Engineering Complete Track Production Quality Gate Evidence

Evidence records:

Complete production gate results
Track completion state
Manifest verification
Governance boundaries
Module quality checks
No backend exposure
17. Local QA Standard

Minimum local QA:

cd ~/securethecloud-labs

python3 -m json.tool manifest.json >/tmp/manifest.qa.json && echo "manifest valid"

find labs/<track-slug>/<module-slug> -maxdepth 2 -type f | sort

grep -n "labs.css\|lab-detail-shell\|lab-status-grid\|mobile-study-menu\|lab-detail-layout\|lab-side-nav\|lab-main-panels\|Concept Deep Dives\|Governance Boundary" labs/<track-slug>/<module-slug>/index.html

grep -n "Backend exposure = false\|Credential handling = false\|Customer data access = false\|Runtime mutation = false\|Production enforcement claim = false" labs/<track-slug>/<module-slug>/index.html

grep -n "<module-slug>\|implemented_modules" manifest.json

git diff --stat
git status --short
18. Commit Standard

Implementation commit:

git add index.html
git add manifest.json
git add tracks/<track-slug>/index.html
git add labs/<track-slug>/<module-slug>/

git commit -m "Add <Module Title> L2 lab"

git push origin main

git log -1 --stat
git status --short

Evidence commit:

git add docs/evidence/PHASE_<N>_<NAME>_EVIDENCE.md

git commit -m "Record <Module Title> L2 lab evidence"

git push origin main

git log -1 --stat
git status --short
19. Production Verification Standard

Use cache-busted URLs:

curl -s "https://labs.securethecloud.dev/?phaseXYZ=$(date +%s)"

Always verify:

Homepage counts
Homepage track preview
Track shell
Module page layout
Module page boundaries
Old/problem classes absent
Manifest valid
Manifest records correct
Final git status clean

Production manifest verification:

curl -s "https://labs.securethecloud.dev/manifest.json?phaseXYZ=$(date +%s)" \
  | python3 -m json.tool >/tmp/production_manifest_phaseXYZ.json \
  && echo "production manifest valid"

Then parse with Python to confirm:

Track exists
Module exists
implemented_modules correct
planned_modules correct
status correct
backend_exposure false
all module backend_exposure false
20. Common Failure Modes
Production behind local commit

Symptom:

Local commit shows module present.
Production manifest still missing module.
Production route returns old page or fallback.

Response:

Confirm HEAD equals origin/main.
Wait briefly.
Rerun production verification.
Do not declare locked until production passes.
Partial commit

Symptom:

Homepage and manifest changed.
Module directory missing.
Track shell not updated.

Response:

Create missing module files.
Repair track shell.
Commit recovery.
Rerun production verification.
Homepage status correct but badge wrong

Symptom:

Status says complete track - 9 of 9.
But card still says ACTIVE LEARNING PATH or ACTIVE badge.

Response:

Repair homepage heading and badge.
Commit repair.
Verify production MCP block has no ACTIVE label.
Old route or fallback page

Symptom:

Production module page contains <style>.

Response:

Check module index.html exists.
Check commit includes module route.
Push if needed.
Rerun production verification.
21. Future Goals

Immediate next goal:

Ensure Phase 254 evidence is committed if it has not already been committed.

Future recommended tracks:

LLM Application Security L2 Track
Enterprise RAG Security L2 Track
Agentic Workflow Security L2 Track
AI Governance and Responsible AI L2 Track
Model Evaluation and Observability L2 Track
Cloud AI Platform Security L2 Track

Strategic platform goal:

Build SecureTheCloud Labs into a complete AI/cloud security curriculum system with production-quality LAB pages, governance-first architecture, evidence-backed delivery, and recruiter-visible milestones.
22. Agent Handover Rules

Next agent must follow these rules:

Do not drift from the active phase.
Do not change unrelated files.
Do not change counts unless a module or track status actually changes.
Do not mark a phase locked without production proof.
Do not remove governance boundaries.
Do not introduce backend exposure without explicit approval.
Do not use inline styles on LAB pages.
Do not claim production enforcement unless it exists.
Use MCP Security Engineering L2 Track as the golden example.
23. Final Handover Summary

The repository has reached a major milestone.

MCP Security Engineering L2 Track is complete.
The track has 9 of 9 modules.
The homepage shows it as complete.
The manifest shows it as complete.
Production quality gate passed.
Backend exposure remains zero.

The next agent should first verify whether Phase 254 evidence has been committed. After that, all future learning paths should follow the MCP track structure and quality bar.
