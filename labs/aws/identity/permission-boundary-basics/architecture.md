# AWS Permission Boundary Basics

## 1. LAB Purpose

This L2 Intermediate LAB teaches how AWS permission boundaries constrain the maximum permissions an IAM principal can receive.

A permission boundary does not grant access by itself.

It limits what an identity policy can successfully allow.

---

## 2. Why This Matters

Permission boundaries are often misunderstood.

A principal can have an identity policy that appears to allow an action, but the final effective permission may still be denied if the permission boundary does not allow that action.

This matters for:

- delegated administration
- developer-created roles
- CI/CD roles
- sandbox environments
- service teams that need limited autonomy
- privilege-escalation prevention

---

## 3. Core Concept

```text
Identity policy = what the principal is asking to do

Permission boundary = the maximum authority the principal may ever receive

Effective permission = identity policy allow AND boundary allow

If the identity policy allows an action but the boundary does not allow it, the final result is deny.

4. Boundary Does Not Grant Access

A permission boundary is not an allow-list by itself.

For access to succeed:

Identity policy must allow the action
AND
Permission boundary must allow the action
AND
No explicit deny may apply
5. Visual Model
Principal
    ↓
Identity Policy
    ↓
Requested Allow
    ↓
Permission Boundary
    ↓
Maximum Authority Check
    ↓
Effective Decision

Decision logic:

Identity policy allows + boundary allows = possible allow

Identity policy allows + boundary does not allow = deny

Boundary allows + identity policy does not allow = deny

Explicit deny anywhere = deny
6. Example Scenario

A developer role has an identity policy that allows IAM role creation:

{
  "Effect": "Allow",
  "Action": "iam:CreateRole",
  "Resource": "*"
}

But the permission boundary allows only non-administrative role creation patterns.

If the developer attempts to create a role with administrative permissions outside the boundary, the final result is:

DENY

The identity policy tried to allow it, but the boundary limited the maximum authority.

7. Relationship to Principal LABs

Permission boundaries are important preparation for Principal LABs.

They help explain why an identity path may or may not become an escalation path.

Relevant Principal LAB connections:

iam:PassRole privilege escalation
Cross-account role escalation
Role chaining escalation

Permission boundaries can reduce escalation risk when they are attached consistently and designed correctly.

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
Visual boundary model exists
manifest.json exposes the lab
AWS Intermediate Identity Track links the lab
homepage renders the lab with INTERMEDIATE maturity
