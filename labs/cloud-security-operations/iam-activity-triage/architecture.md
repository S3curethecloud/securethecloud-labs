# IAM Activity Triage - Architecture Notes

## Purpose

Teach IAM activity triage for cloud security operations.

This module explains how to review identity activity, classify suspicious IAM behavior, gather evidence, separate severity from confidence, and prepare bounded escalation narratives.

## Product Context

SecureTheCloud Labs

## Track Context

Cloud Security Operations L2 Track

## Core Lesson

IAM is one of the highest-value control planes in cloud security operations.

IAM activity triage asks:

```text
Who acted?
What identity was used?
What permission changed?
What resource or account was affected?
Was the behavior expected?
What evidence supports the interpretation?
What escalation path is appropriate?
IAM Triage Question
Does this IAM activity represent expected administration, misconfiguration, suspicious access, privilege escalation, credential misuse, or an incident candidate?
IAM Signal Types
Role assumption:
Temporary privilege use, cross-account access, elevated role use, unusual source, unexpected session name.

Privilege change:
Policy attachment, policy edit, role permission expansion, group membership change, admin grant.

Access key activity:
New key creation, old key reuse, unusual source, abnormal API calls, unexpected service access.

Failed access:
Repeated denied actions, impossible or unusual access attempts, policy probing.

Identity configuration:
MFA changes, trust policy changes, federation updates, external identity provider changes.

Service identity behavior:
Automation role use, workload identity activity, service account actions, unexpected machine-to-machine behavior.
IAM Triage Workflow
IAM event observed
-> identity classified
-> action classified
-> affected scope identified
-> expected behavior checked
-> related events reviewed
-> privilege impact estimated
-> confidence assigned
-> evidence package prepared
-> escalation path selected
Severity vs Confidence
Severity:
Potential impact of the IAM event if it represents real risk.

Confidence:
How strongly the available evidence supports the interpretation.

A privilege escalation event may be high severity even before confidence is high.
A known scheduled admin change may be low risk but still worth documenting.
High-Risk Anti-Pattern
IAM alert fires
-> analyst assumes compromise
-> role context is not reviewed
-> policy change impact is not understood
-> source and owner are not checked
-> escalation summary overstates certainty

This is unsafe because identity events often require context. Bad IAM triage can miss real privilege escalation or create false incidents.

Secure IAM Triage Pattern
Classify identity
-> classify IAM action
-> identify affected account, role, policy, and resource
-> compare to approved change or expected behavior
-> review source, time, session, owner, and related events
-> estimate privilege impact
-> record confidence and unknowns
-> escalate with bounded language
Evidence Requirements

An IAM triage evidence package should include:

event source
event timestamp
identity or role
actor type
IAM action
affected policy, role, group, account, project, or resource
source context
session context
related events
expected behavior comparison
privilege impact
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
No IAM mutation
No cloud provider mutation
No runtime mutation
No autonomous production enforcement claim
No official enterprise deployment claim
