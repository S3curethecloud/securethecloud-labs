# MCP Approval Gate and Human-in-the-Loop Controls — Architecture Note

## Purpose

This LAB teaches learners how to design and review MCP approval gates and human-in-the-loop controls.

It focuses on:

- Approval trigger identification
- Human reviewer authorization
- Sensitive action detection
- Decision scope
- Deny, approve, escalate, and timeout behavior
- Evidence minimization
- Separation of duties
- Immutable decision logging
- Revocation and rollback boundaries
- Reviewer-safe evidence capture

## Runtime Boundary

This LAB is static HTML/CSS/JSON content only.

```text
Backend exposure = false
MCP server execution = false
MCP client execution = false
Live MCP integration = false
Live tool invocation = false
Approval execution = false
Credential handling = false
Customer data access = false
Runtime mutation = false
Production enforcement claim = false
```

## Implementation Scope

Phase 238 implements module 6 of 9 for the MCP Security Engineering L2 Track.

Implemented:

```text
MCP Approval Gate and Human-in-the-Loop Controls LAB
MCP Approval Gate metadata
MCP Approval Gate architecture note
Track shell update to 6 of 9
Manifest update to 6 of 9
Homepage preview update to 6 of 9
```

Not implemented in this phase:

```text
MCP Agent Workflow and Tool Abuse Review
MCP Evidence Capture and Control Mapping
MCP Security Engineering Capstone
```

## Safety Model

The LAB uses synthetic examples only and does not expose, execute, invoke, approve, export, or mutate live MCP infrastructure, customer data, or connected tools.
