# Cloud Security Operations Capstone - Architecture Notes

## Purpose

Teach an integrated cloud security operations workflow.

This capstone ties together the Cloud Security Operations L2 Track:

- Cloud Security Operations Overview
- Cloud Event and Signal Classification
- IAM Activity Triage
- Workload and Network Signal Triage
- Cloud Control-Plane Incident Evidence
- Cloud Log Source and Evidence Mapping
- Cloud Incident Timeline and Escalation Narrative
- Cloud Response Decision and Handoff

## Product Context

SecureTheCloud Labs

## Track Context

Cloud Security Operations L2 Track

## Core Lesson

A mature cloud security operations workflow converts raw signals into an evidence-backed response handoff.

The analyst must show:

```text
what signal arrived
how it was classified
which identity, workload, network, and control-plane evidence matters
which logs support each claim
what happened in sequence
what is known and unknown
what response path is justified
what handoff package is ready for review
Capstone Question
Can the analyst produce a complete cloud security operations evidence package that classifies the signal, explains the timeline, maps evidence, preserves uncertainty, and recommends a bounded next action without executing live response?
Capstone Workflow
Signal received
-> event classified
-> IAM activity reviewed
-> workload and network context reviewed
-> control-plane evidence collected
-> log sources mapped to claims
-> timeline built
-> severity and confidence assigned
-> escalation narrative drafted
-> response decision selected
-> handoff package prepared
Scenario Inputs
Initial signal:
Suspicious cloud activity involving privileged role use, control-plane modification, workload exposure, and possible data access.

Evidence sources:
Audit logs, identity events, workload logs, network flow records, storage access records, security service findings, and configuration context.

Operational constraints:
No direct production mutation, no assumed compromise without evidence, no hidden uncertainty, and no unapproved containment action.

Capstone output:
Reviewer-safe cloud operations evidence package and response handoff.
Portfolio Evidence Package

A capstone evidence package should include:

executive summary
signal classification
affected scope
IAM activity triage
workload and network triage
control-plane evidence
log source evidence map
incident timeline
severity rationale
confidence rationale
known facts
unknowns
response options
recommended handoff owner
approval boundary
ticket-ready handoff summary
non-mutating governance boundary
High-Risk Anti-Pattern
Alert received
-> analyst jumps to compromise claim
-> weak evidence map
-> timeline is incomplete
-> unknowns are hidden
-> response recommendation is production-impacting
-> handoff does not identify owner or approval boundary

This is unsafe because operational security work must be evidence-backed, reproducible, bounded, and aligned with response authority.

Secure Capstone Pattern
Classify the signal
-> collect evidence
-> map evidence to claims
-> build timeline
-> record severity and confidence
-> preserve unknowns
-> select response option
-> hand off to accountable owner
-> avoid live mutation
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
No live incident simulation
No live response execution
No containment execution
No ticket creation
No notification execution
No runtime mutation
No autonomous production enforcement claim
No official enterprise deployment claim
