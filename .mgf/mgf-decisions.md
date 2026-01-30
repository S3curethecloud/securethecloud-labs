# MGF DECISIONS — SecureTheCloud Labs

## ADR-0001 — Static-First Labs Platform
- Decision:
All SecureTheCloud labs are implemented using static HTML, CSS, and JavaScript.
- Status: LOCKED
- Consequence:
No React, Next.js, Vue, or backend rendering in this repo.

## ADR-0002 — No Infrastructure Code
- Decision:
Infrastructure (Terraform, CloudFormation, etc.) does not live in this repo.
- Status: LOCKED
- Consequence:
Labs consume infrastructure, they do not define it.
