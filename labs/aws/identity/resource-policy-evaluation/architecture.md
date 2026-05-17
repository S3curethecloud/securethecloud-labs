# AWS Resource Policy Evaluation

## 1. LAB Purpose

This L2 Intermediate LAB teaches how AWS resource-based policies participate in authorization decisions.

A resource policy is attached to a resource.

It defines who may access that resource and under which conditions.

---

## 2. Why This Matters

Many AWS authorization decisions are not controlled by identity policies alone.

Resource policies often decide whether a principal can access:

- S3 buckets and objects
- KMS keys
- SQS queues
- SNS topics
- Lambda functions
- Secrets Manager secrets
- IAM role trust relationships

This is especially important for cross-account access.

---

## 3. Core Concept

```text
Identity policy = what the principal is allowed to request

Resource policy = what the resource allows or denies

Permission boundary = maximum authority for the principal

SCP = maximum authority available to the account or OU

Effective permission = identity-side allow + resource-side allow + boundary/SCP survival + no explicit deny

A request may be allowed by an identity policy but denied by a resource policy.

A request may also be allowed by a resource policy but still fail if the principal lacks the required identity-side permission or is constrained by another guardrail.

4. Resource Policy Does Not Replace IAM Evaluation

A resource policy is part of the authorization decision.

It does not remove the need to evaluate:

principal
action
resource
context
identity policy
resource policy
permission boundary
SCP
explicit deny
5. Visual Model
Principal
    ↓
Identity Policy
    ↓
Resource Policy
    ↓
Boundary / SCP Guardrails
    ↓
Explicit Deny Check
    ↓
Effective Decision

Decision logic:

Identity allows + resource allows + guardrails allow = possible allow

Identity allows + resource denies = deny

Resource allows + identity does not allow = deny in most identity-based flows

Explicit deny anywhere = deny
6. Example Scenario

An IAM role has an identity policy allowing access to an S3 bucket:

{
  "Effect": "Allow",
  "Action": "s3:GetObject",
  "Resource": "arn:aws:s3:::example-bucket/*"
}

But the S3 bucket policy denies access unless the request comes through a specific VPC endpoint:

{
  "Effect": "Deny",
  "Principal": "*",
  "Action": "s3:GetObject",
  "Resource": "arn:aws:s3:::example-bucket/*",
  "Condition": {
    "StringNotEquals": {
      "aws:sourceVpce": "vpce-1234567890abcdef0"
    }
  }
}

If the request does not use the approved VPC endpoint, the final result is:

DENY

The identity policy allowed the action, but the resource policy denied it.

7. Relationship to Principal LABs

Resource policy evaluation prepares learners for Principal LABs because advanced identity paths often depend on resource-side trust.

Relevant Principal LAB connections:

Cross-account role escalation
iam:PassRole privilege escalation
Role chaining escalation

Cross-account role escalation depends directly on the target role trust policy.

A role trust policy is a resource-based policy attached to an IAM role.

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
Visual resource-policy model exists
manifest.json exposes the lab
AWS Intermediate Identity Track links the lab
homepage renders the lab with INTERMEDIATE maturity
