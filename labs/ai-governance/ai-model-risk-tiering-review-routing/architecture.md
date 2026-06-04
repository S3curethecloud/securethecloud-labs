# AI Model Risk Tiering and Review Routing — Architecture Notes

Status: Implemented LAB / Static Educational Content

## Purpose

Teach how AI governance teams route AI use cases to the correct review path based on model risk, data sensitivity, autonomy, business impact, customer impact, regulatory exposure, and operational authority.

## Product Context

SecureTheCloud AI Governance Command Center

## Course Context

AI Governance Command Center Track

## Core Lesson

AI governance is not complete when a use case is documented.

The next decision is:

```text
What risk tier applies, and who must review before this AI workflow can proceed?
Risk Tiering Model
Low Risk
→ public or low-sensitivity content
→ no material customer, employee, financial, legal, safety, or regulated impact
→ standard owner review

Moderate Risk
→ internal business context or limited operational assistance
→ no autonomous mutation
→ security or architecture review may be required

High Risk
→ confidential data, customer impact, employee impact, financial impact, operational decision support, or regulated workflow influence
→ security, privacy, legal, architecture, and business-owner review may be required

Restricted Risk
→ credentials, secrets, payment data, health data, legal records, autonomous execution, safety impact, high-risk customer impact, or production mutation authority
→ executive review, formal approval, and strong denial / escalation defaults
Review Routing Questions

A governed AI workflow must answer:

What is the AI system supposed to do?
What data classification applies?
Will the AI affect customers, employees, finances, legal decisions, safety, or compliance?
Can the AI recommend, draft, submit, approve, or execute actions?
Does the workflow touch production systems?
Does it require security review?
Does it require privacy review?
Does it require legal review?
Does it require architecture review?
Does it require executive approval?
What evidence proves the routing decision?
Safe Control Pattern
AI use case
→ data classification
→ autonomy classification
→ impact classification
→ risk tier
→ required reviewers
→ approval / denial / escalation route
→ evidence record
Example

A public documentation chatbot may be low risk.

An internal assistant summarizing business procedures may be moderate risk.

A workflow using customer records, employee records, payment context, legal material, or operational decision support may be high risk.

An AI agent with autonomous execution authority, credentials, regulated records, or production mutation ability should be restricted unless explicitly authorized through a governed approval process.

Governance Boundary

Static learning LAB only
No backend API exposure
No live enterprise integration
No live reviewer workflow
No model provider integration
No runtime mutation
No autonomous production enforcement claim
No official enterprise deployment claim
