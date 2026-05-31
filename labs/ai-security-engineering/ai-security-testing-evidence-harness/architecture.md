# AI Security Testing and Evidence Harness - Architecture Notes

## Purpose

Teach AI security testing and evidence harness design for AI applications.

This module explains how to design repeatable security tests across prompt boundaries, tool permissions, retrieval security, output safety, runtime guardrails, abuse controls, and evidence capture.

## Product Context

SecureTheCloud Labs

## Track Context

AI Security Engineering L2 Track

## Core Lesson

AI security controls are only useful if they can be tested, explained, and evidenced.

A secure AI engineering program needs deterministic test cases, expected outcomes, failure-path validation, negative tests, evidence records, and audit-ready summaries.

## Security Testing Question

```text
How do we prove that AI security controls work across prompt, tool, retrieval, output, runtime, abuse, and evidence boundaries?
Test Harness Classes
Prompt boundary test:
Verifies that untrusted user, retrieved, or tool content cannot override trusted instructions.

Tool permission test:
Verifies that tools are classified, scoped, denied, approved, and evidenced correctly.

Retrieval security test:
Verifies tenant scope, source authority, sensitivity filtering, freshness, and poisoning resistance.

Output safety test:
Verifies response classification, grounding, redaction, refusal, escalation, and unsafe-output blocking.

Runtime guardrail test:
Verifies loop limits, retry limits, timeouts, deny-path enforcement, circuit breakers, degraded modes, and escalation.

Abuse and cost test:
Verifies token budgets, rate-limit keys, quota scopes, repeated attempt detection, throttling, denial, and cost evidence.

Evidence integrity test:
Verifies that every decision records enough context to explain what happened and why.
High-Risk Anti-Pattern
AI controls exist
-> tests are informal or manual
-> expected outcomes are undefined
-> failures are not captured
-> evidence is incomplete
-> control effectiveness cannot be proven

This pattern is unsafe because it creates security theater instead of verifiable AI security engineering.

Secure Testing Harness Pattern
Test case defined
-> control boundary selected
-> input and threat condition prepared
-> expected decision declared
-> execution simulated or reviewed
-> pass/fail outcome recorded
-> evidence package generated
-> summary prepared for reviewer
Required Test Harness Boundaries
Test case boundary:
Defines the scenario, input, threat, control, expected result, and evidence requirement.

Expected outcome boundary:
Declares whether the request should allow, deny, redact, throttle, escalate, or fail closed.

Negative test boundary:
Confirms that unsafe, unauthorized, overscoped, or unsupported behavior is blocked.

Evidence boundary:
Records inputs, control checks, decision, reason, outcome, timestamp, and reviewer summary.

Regression boundary:
Keeps tests repeatable so future changes do not silently weaken controls.

Reviewer boundary:
Converts technical evidence into audit-ready explanations without inventing production claims.
Engineering Requirements

A secure AI testing and evidence harness should:

define test cases for every major AI security boundary
include positive and negative tests
define expected outcomes before review
test prompt injection and instruction hierarchy boundaries
test tool permission and approval gates
test retrieval scope, source authority, sensitivity, freshness, and poisoning resistance
test output safety, grounding, refusal, redaction, and escalation
test runtime loop limits, retries, timeouts, deny paths, and circuit breakers
test abuse, cost, quota, and rate-limit decisions
produce evidence records for every pass, fail, deny, throttle, and escalation
summarize results for engineering, governance, and audit stakeholders
Example

A test case attempts to make retrieved content override tool permissions.

The harness should classify the retrieved instruction as untrusted context, deny the unauthorized tool path, preserve the decision reason, record the control evidence, and generate a reviewer-safe summary.

Governance Boundary
Static learning LAB only
No backend API exposure
No live model integration
No live tool execution
No live retrieval execution
No vector database access
No enterprise data access
No provider quota mutation
No runtime mutation
No autonomous production enforcement claim
No official enterprise deployment claim
