
AI Security Engineering L2 Track — Module Roadmap

Status: Planning Baseline

Proposed Module Sequence
Module 1 — AI Security Engineering Overview

Purpose:

Introduce secure AI system design, core threats, control layers, and engineering boundaries.
Module 2 — Secure AI Application Architecture

Purpose:

Teach secure architecture patterns for AI apps, including frontend/backend separation, model boundary, API boundary, policy boundary, and evidence boundary.
Module 3 — Prompt Boundary Engineering

Purpose:

Teach how to separate system instructions, developer instructions, user input, retrieved content, and tool outputs.
Module 4 — Tool Permission Engineering

Purpose:

Teach scoped tool permissions, action classification, mutating vs non-mutating tools, approval gates, and self-approval prevention.
Module 5 — Retrieval Security Engineering

Purpose:

Teach secure RAG design: source authority, tenant boundaries, sensitivity filtering, retrieval poisoning defenses, and evidence capture.
Module 6 — Agent Runtime Guardrails

Purpose:

Teach runtime controls for agent loops, action limits, retry caps, escalation, kill switches, and safe terminal states.
Module 7 — AI Abuse, Cost, and Rate Limit Controls

Purpose:

Teach operational controls for token budgets, model calls, retrieval calls, tool retries, rate limits, quota ceilings, and abuse detection.
Module 8 — AI Security Testing Harness

Purpose:

Teach how to test AI workflows for prompt injection, tool hijacking, retrieval poisoning, data leakage, approval bypass, and runaway loops.
Module 9 — AI Security Evidence Package

Purpose:

Teach how to package engineering evidence for security review, audit review, executive review, and readiness gates.
Planned Quality Gates

Each implemented module should follow the same discipline:

Build
→ evidence
→ production verification
→ quality gate
Boundary

This roadmap is planning only.

No module is implemented by this file.
