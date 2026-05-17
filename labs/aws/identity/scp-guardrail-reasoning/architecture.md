# AWS SCP Guardrail Reasoning

## 1. LAB Purpose

This L2 Intermediate LAB teaches how AWS Service Control Policies constrain the maximum permissions available to AWS accounts and organizational units.

An SCP does not grant access by itself.

It defines the outer authorization boundary for accounts within AWS Organizations.

---

## 2. Why This Matters

SCPs are organization-level guardrails.

They help security teams define what accounts are not allowed to do, even if an identity policy inside the account attempts to allow the action.

This matters for:

- multi-account governance
- delegated account administration
- sandbox account control
- region restrictions
- service restrictions
- privileged IAM action restrictions
- organization-wide blast-radius reduction

---

## 3. Core Concept

```text
Identity policy = what the principal is asking to do

Permission boundary = the maximum authority for a principal

SCP = the maximum authority available to an account or OU

Effective permission = identity allow AND boundary allow AND SCP allow AND no explicit deny

If an SCP does not allow an action, or explicitly denies it, the account cannot perform that action even when an identity policy appears to allow it.

4. SCP Does Not Grant Access

An SCP is not an allow-list that grants permissions directly.

For access to succeed:

Identity policy must allow the action
AND
Permission boundary must allow the action if attached
AND
SCP must allow the action
AND
No explicit deny may apply
5. Visual Model
Principal
    ↓
Identity Policy
    ↓
Permission Boundary
    ↓
Account / OU SCP
    ↓
Organization Guardrail Check
    ↓
Effective Decision

Decision logic:

Identity policy allows + SCP allows = possible allow

Identity policy allows + SCP denies = deny

SCP allows + identity policy does not allow = deny

Explicit deny anywhere = deny
6. Example Scenario

A developer role has an identity policy allowing S3 bucket creation:

{
  "Effect": "Allow",
  "Action": "s3:CreateBucket",
  "Resource": "*"
}

But the account is in an OU with an SCP that denies S3 bucket creation outside approved regions:

{
  "Effect": "Deny",
  "Action": "s3:CreateBucket",
  "Resource": "*",
  "Condition": {
    "StringNotEquals": {
      "aws:RequestedRegion": "us-east-1"
    }
  }
}

If the request is made outside the approved region, the final result is:

DENY

The identity policy allowed the action, but the organization guardrail blocked it.

7. Relationship to Principal LABs

SCPs are important preparation for Principal LABs because they help learners understand when an identity path is blocked by organization-level governance.

Relevant Principal LAB connections:

iam:PassRole privilege escalation
Cross-account role escalation
Role chaining escalation

SCPs can reduce escalation risk when they constrain privileged IAM actions, region usage, account boundaries, or service creation paths.

8. Shield / Aegis Boundary

This L2 LAB is Shield-aware but does not create a Shield finding by itself.

Current status:

Shield finding required: false
Aegis runtime fixture required: false
Runtime change required: false
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
Mobile Study Menu exists
Concept Deep Dives exist
Visual SCP guardrail model exists
manifest.json exposes the lab
AWS Intermediate Identity Track links the lab
homepage renders the lab with INTERMEDIATE maturity
