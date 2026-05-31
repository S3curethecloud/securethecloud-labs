# Cloud Log Source and Evidence Mapping - Architecture Notes

## Purpose

Teach cloud log source and evidence mapping for cloud security operations.

This module explains how to map cloud log sources to incident evidence needs, identify gaps, correlate event types, understand retention boundaries, and prepare reviewer-safe evidence packages.

## Product Context

SecureTheCloud Labs

## Track Context

Cloud Security Operations L2 Track

## Core Lesson

Security operations depends on knowing which log source proves which fact.

A cloud incident narrative should not simply say that logs exist. It should explain:

```text
which log source supports the claim
what event field proves the fact
what timestamp anchors the timeline
what identity or resource is involved
what evidence is missing
what confidence is justified
Log Source Mapping Question
Which log source proves this security claim, what field supports it, what context is missing, and how should the evidence be preserved for review?
Log Source Types
Audit logs:
Administrative API calls, control-plane changes, policy edits, resource creation, deletion, exposure, logging updates, and security control changes.

Identity logs:
Authentication, role assumption, federation, MFA changes, failed access, privilege changes, group membership, service account use, and session context.

Workload logs:
Application behavior, compute activity, container logs, serverless execution, service behavior, process activity, and workload errors.

Network logs:
Flow records, ingress, egress, source, destination, ports, protocols, rejected traffic, public exposure, lateral movement paths, and segmentation evidence.

Storage logs:
Object access, bucket access, database access, volume activity, public sharing, data movement, and access patterns.

Security service logs:
Detection findings, posture checks, vulnerability findings, configuration alerts, threat intelligence matches, and control status.

Evidence metadata:
Timestamp, account, project, region, resource identifier, actor, request ID, source IP, user agent, response code, correlation ID, owner, retention, and integrity context.
Evidence Mapping Workflow
Security claim identified
-> evidence need defined
-> relevant log source selected
-> event fields mapped
-> timestamp and resource context verified
-> related sources correlated
-> evidence gaps identified
-> retention and integrity reviewed
-> confidence assigned
-> reviewer-safe evidence map prepared
Evidence Gap Handling
A missing log source does not automatically prove safety or compromise.

It should be recorded as an evidence gap:
- what fact cannot be proven
- which log source would be needed
- whether the gap affects severity
- whether the gap affects confidence
- what next step is appropriate
High-Risk Anti-Pattern
Incident claim is written
-> log source is not named
-> event fields are not mapped
-> timeline is unsupported
-> evidence gaps are hidden
-> reviewer cannot reproduce the reasoning

This is unsafe because incident narratives without source-to-claim mapping are difficult to audit, defend, or improve.

Secure Evidence Mapping Pattern
State the security claim
-> identify required evidence
-> map claim to log source and field
-> correlate supporting sources
-> record gaps and retention limits
-> assign confidence
-> prepare reviewer-safe evidence map
Evidence Requirements

A log source evidence map should include:

security claim
required evidence
log source
event name or event type
timestamp
actor or identity field
resource field
source and destination context
request or correlation identifier
response status
related log sources
evidence gaps
retention boundary
integrity notes
confidence rationale
reviewer-safe summary
Governance Boundary
Static learning LAB only
No backend API exposure
No cloud provider integration
No SIEM integration
No ticketing integration
No alert pipeline
No live log ingestion
No customer data access
No live detector execution
No log pipeline mutation
No cloud provider mutation
No runtime mutation
No autonomous production enforcement claim
No official enterprise deployment claim
