# Cloud Event and Signal Classification - Architecture Notes

## Purpose

Teach cloud event and signal classification for cloud security operations.

This module explains how to classify cloud security signals before triage, escalation, or incident narrative creation.

## Product Context

SecureTheCloud Labs

## Track Context

Cloud Security Operations L2 Track

## Core Lesson

Cloud security operations begins with classification.

Before an alert can be triaged, the analyst must understand what kind of signal it is, where it came from, who or what caused it, which asset is involved, what action occurred, and how much confidence the evidence supports.

## Classification Question

```text
What is this signal, where did it come from, who acted, what changed, which asset is affected, how severe is it, and what evidence supports that conclusion?
Classification Dimensions
Event source:
Cloud audit log, identity log, workload log, network log, configuration event, detection rule, or external alert.

Actor:
Human user, service account, role, workload identity, automation, third-party integration, or unknown actor.

Asset:
Account, subscription, project, role, policy, compute instance, container, serverless function, bucket, database, network, or control-plane resource.

Action:
Login, role assumption, policy change, resource creation, deletion, exposure, access, data movement, network change, or configuration update.

Severity:
Informational, low, medium, high, critical, or unknown pending evidence.

Confidence:
Low, medium, high, or pending based on signal quality, corroboration, and context.

Tenant or scope:
Which environment, account, business unit, project, workload, or owner is affected.

Evidence quality:
Raw event only, correlated event set, enriched context, owner-confirmed behavior, or reviewer-validated evidence.
Classification Workflow
Signal observed
-> source identified
-> actor identified
-> asset identified
-> action classified
-> tenant and owner context reviewed
-> expected behavior compared
-> severity estimated
-> confidence assigned
-> evidence quality recorded
-> triage path selected
Severity vs Confidence
Severity:
How bad the impact could be if the signal represents real risk.

Confidence:
How strongly the evidence supports the interpretation.

A high-severity signal with low confidence should not be ignored.
A low-severity signal with high confidence may still need documentation.
High-Risk Anti-Pattern
Alert fires
-> no source classification
-> actor is assumed
-> asset scope is unclear
-> severity is copied from the tool
-> confidence is not recorded
-> triage decision is weak

This pattern is unsafe because it turns cloud operations into alert forwarding instead of evidence-based analysis.

Secure Classification Pattern
Classify source
-> identify actor
-> identify asset
-> classify action
-> determine scope
-> estimate severity
-> assign confidence
-> record evidence quality
-> route to triage
Evidence Requirements

A classification record should include:

event source
event timestamp
actor
affected asset
action observed
tenant or environment scope
severity rationale
confidence rationale
evidence quality
related event references
unknowns
recommended triage path
Governance Boundary
Static learning LAB only
No backend API exposure
No cloud provider integration
No SIEM integration
No ticketing integration
No alert pipeline
No customer data access
No live detector execution
No cloud provider mutation
No runtime mutation
No autonomous production enforcement claim
No official enterprise deployment claim
