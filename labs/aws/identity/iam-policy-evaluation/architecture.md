# AWS IAM Policy Evaluation

## 1. LAB Purpose

This L2 Intermediate LAB teaches how AWS IAM evaluates permissions when multiple policy types apply to a request.

The goal is to help learners move beyond basic IAM vocabulary into deterministic security reasoning.

This lab is the bridge between:

```text
L1: AWS IAM Basics

and:

L3: AWS Principal Identity Track
2. Why This Matters

Most AWS identity risks are not caused by one policy alone.

Real authorization outcomes often depend on the interaction between:

identity-based policies
resource-based policies
permission boundaries
session policies
service control policies
explicit deny conditions

A security engineer must be able to reason about the final effective decision.

3. IAM Evaluation Model

Simplified request model:

Principal
  +
Action
  +
Resource
  +
Context
  =
Authorization Decision

Evaluation flow:

Request received
    ↓
Check explicit deny
    ↓
Evaluate applicable identity policies
    ↓
Evaluate applicable resource policies
    ↓
Apply permission boundaries
    ↓
Apply session policies
    ↓
Apply service control policies
    ↓
Final decision: Allow or Deny
4. Core Rule

The most important IAM rule:

Explicit deny overrides allow.

If any applicable policy produces an explicit deny, the final decision is deny.

5. Example Scenario

A user has an identity policy that allows S3 object reads:

{
  "Effect": "Allow",
  "Action": "s3:GetObject",
  "Resource": "arn:aws:s3:::example-bucket/*"
}

But an organization SCP denies S3 reads outside an approved region:

{
  "Effect": "Deny",
  "Action": "s3:GetObject",
  "Resource": "*",
  "Condition": {
    "StringNotEquals": {
      "aws:RequestedRegion": "us-east-1"
    }
  }
}

If the request is made outside us-east-1, the final result is:

DENY

Even though the identity policy allowed the action.

6. Effective Permission Reasoning

Learners should ask:

Who is the principal?
What action is requested?
Which resource is targeted?
Which policy types apply?
Is there an explicit deny?
Is there at least one allow?
Do boundaries, session policies, or SCPs reduce the permission?
What is the final decision?
7. Relationship to Principal LABs

This L2 lab prepares learners for the AWS Principal Identity Track.

The Principal LABs require understanding how effective permissions create deterministic paths:

Cross-account role escalation
iam:PassRole privilege escalation
Role chaining escalation

Those paths cannot be reasoned about safely without understanding IAM policy evaluation.

8. Shield / Aegis Boundary

This L2 LAB is Shield-aware but does not create a Shield finding by itself.

It may support future Aegis Runtime interpretation because effective-permission reasoning is relevant to identity integrity signals.

Current status:

Shield finding required: false
Aegis runtime fixture required: false
OPA authority boundary: preserved
9. Governance Boundary

This LAB is read-only and deterministic.

It does not:

exploit AWS
mutate a customer environment
deploy live infrastructure
invoke AWS APIs against customer accounts
execute remediation
issue tokens
create runtime sessions
override OPA

Authority boundary:

Runtime = source of truth
OPA = decision authority
Aegis = bounded intelligence
Frontend = rendering only
10. Completion Criteria

This LAB is complete when:

metadata.json exists and is valid
architecture.md exists
index.html renders the L2 page
manifest.json exposes the lab
homepage renders the lab with INTERMEDIATE maturity
LAB taxonomy identifies L2 as the next learning layer

---

## 11. Visual Learning Model

This LAB includes a visual evaluation model to help learners reason through IAM authorization as an interconnected decision path.

The visual model emphasizes:

- principal
- action
- resource
- request context
- identity policy
- resource policy
- permission boundary
- SCP
- explicit deny
- effective permission
- final allow or deny decision

The model is rendered with native HTML and CSS.

No external image dependency is used.

No runtime logic is introduced.
