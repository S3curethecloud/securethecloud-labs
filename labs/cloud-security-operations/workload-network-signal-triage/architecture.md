# Workload and Network Signal Triage - Architecture Notes

## Purpose

Teach workload and network signal triage for cloud security operations.

This module explains how to review compute, storage, service, and network activity signals; classify workload behavior; evaluate exposure; gather evidence; separate severity from confidence; and prepare bounded escalation narratives.

## Product Context

SecureTheCloud Labs

## Track Context

Cloud Security Operations L2 Track

## Core Lesson

Workload and network signals show how cloud resources behave.

A workload or network event should not be treated as automatically malicious. Analysts must classify the signal, identify the affected workload or path, compare expected behavior, assess exposure, and preserve evidence before escalation.

## Workload and Network Triage Question

```text
Does this workload or network signal represent expected behavior, misconfiguration, suspicious activity, exposure risk, lateral movement, data access risk, or an incident candidate?
Signal Types
Compute activity:
Instance start, stop, creation, image changes, unusual process behavior, unexpected service behavior, or suspicious workload lifecycle activity.

Storage access:
Bucket/object access, database reads, unusual volume access, public exposure, large access patterns, or abnormal data interaction.

Network path:
Ingress, egress, unusual destination, lateral movement path, exposed service, security group change, routing change, or segmentation concern.

Service behavior:
Serverless execution, container behavior, managed service activity, queue usage, API behavior, or unexpected service-to-service communication.

Exposure signal:
Public endpoint, internet-facing workload, permissive rule, unexpected open port, exposed storage, or reachable sensitive service.

Evidence signal:
Audit log, flow log, workload log, configuration snapshot, related identity event, asset owner confirmation, or reviewer-validated evidence.
Triage Workflow
Workload or network signal observed
-> source classified
-> workload or network path identified
-> affected asset and owner identified
-> expected behavior reviewed
-> exposure and reachability assessed
-> related identity and control-plane events reviewed
-> severity estimated
-> confidence assigned
-> evidence package prepared
-> escalation path selected
Severity vs Confidence
Severity:
Potential impact if the workload or network signal represents real risk.

Confidence:
How strongly the available evidence supports the interpretation.

A public exposure signal may be high severity even before confidence is complete.
A known maintenance network change may be low risk but still worth documenting.
High-Risk Anti-Pattern
Network alert fires
-> analyst assumes intrusion
-> workload owner is not checked
-> exposure scope is unclear
-> related identity events are ignored
-> severity is copied from the tool
-> escalation summary overstates certainty

This is unsafe because workload and network signals are context-heavy. Weak triage can miss real exposure or create false incidents.

Secure Workload and Network Triage Pattern
Classify signal source
-> identify workload, service, path, and asset owner
-> assess exposure and reachability
-> compare against expected behavior
-> review related identity, workload, and control-plane events
-> estimate impact
-> record confidence and unknowns
-> escalate with bounded evidence
Evidence Requirements

A workload and network triage evidence package should include:

event source
event timestamp
workload or service identity
affected asset
network path or exposure detail
source and destination context
related identity events
related control-plane events
expected behavior comparison
exposure or reachability assessment
severity rationale
confidence rationale
known unknowns
escalation recommendation
reviewer-safe summary
Governance Boundary
Static learning LAB only
No backend API exposure
No cloud provider integration
No SIEM integration
No ticketing integration
No alert pipeline
No customer data access
No live detector execution
No workload mutation
No network mutation
No cloud provider mutation
No runtime mutation
No autonomous production enforcement claim
No official enterprise deployment claim
