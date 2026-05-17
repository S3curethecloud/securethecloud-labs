# AWS S3 Public Access Risk

## 1. LAB Purpose

This applied L2 LAB teaches how S3 public access risk emerges from multiple authorization and exposure controls working together.

S3 public access is not usually explained by one setting alone.

It may involve:

- bucket policy
- object ACL history
- Block Public Access settings
- identity-side permissions
- resource-side permissions
- organization guardrails
- explicit deny conditions
- cross-account trust and ownership context

---

## 2. Why This Matters

S3 public exposure remains one of the easiest cloud risks for students, interns, engineers, and executives to understand visually.

It is also a strong applied case study because it combines the L2 authorization model:

```text
IAM Policy Evaluation
Permission Boundary Basics
SCP Guardrail Reasoning
Resource Policy Evaluation

S3 public access risk demonstrates how authorization theory becomes practical exposure analysis.

3. Core Concept
Public access risk = resource exposure + policy authorization + missing guardrails

A bucket may become publicly reachable when a policy or ACL allows broad access and no protective control blocks the request.

Important layers:

Identity policy = who can change or access the bucket

Resource policy = what the bucket allows

Block Public Access = S3 public-access safety layer

SCP = account or organization ceiling

Explicit deny = hard stop

Effective exposure = final reachable public path
4. S3 Public Access Is a Decision Path

A public bucket is not only a bucket with a policy.

A reviewer should ask:

Does the bucket policy allow public access?
Do ACLs create public object access?
Are Block Public Access settings enabled?
Does an SCP prevent public bucket policy changes?
Does an explicit deny block non-approved access?
Can any principal modify the exposure state?
5. Visual Model
Internet Principal
    ↓
S3 Bucket Policy / ACL
    ↓
Block Public Access Check
    ↓
SCP / Guardrail Check
    ↓
Explicit Deny Check
    ↓
Effective Exposure Decision

Decision logic:

Public allow + no block + no deny = public exposure possible

Public allow + Block Public Access enabled = blocked

Public allow + SCP denies public policy changes = prevented

No public allow = not publicly reachable

Explicit deny anywhere = deny
6. Example Scenario

A bucket policy allows anyone to read objects:

{
  "Effect": "Allow",
  "Principal": "*",
  "Action": "s3:GetObject",
  "Resource": "arn:aws:s3:::example-public-bucket/*"
}

If Block Public Access is disabled and no explicit deny applies, the bucket may expose objects publicly.

Final result:

PUBLIC EXPOSURE POSSIBLE

If Block Public Access blocks public policies, the same policy intent is blocked.

Final result:

DENY / PUBLIC ACCESS BLOCKED
7. Relationship to L2 Authorization Model

This lab applies the four core L2 authorization layers:

IAM Policy Evaluation:
Can a principal read or modify S3 access?

Permission Boundary Basics:
Can a delegated principal exceed approved authority?

SCP Guardrail Reasoning:
Can the account create public S3 exposure?

Resource Policy Evaluation:
Does the bucket policy or ACL allow access?
8. Relationship to Principal LABs

S3 public access risk prepares learners for Principal LABs because exposure often depends on identity control.

Relevant Principal LAB connections:

iam:PassRole privilege escalation
Cross-account role escalation
Role chaining escalation

A principal that can modify bucket policy, disable guardrails, or pass a role with S3 authority can change exposure state.

9. Shield / Aegis Boundary

This L2 LAB is Shield-aware but does not create a Shield finding by itself.

Current status:

Shield finding required: false
Aegis runtime fixture required: false
Runtime change required: false
OPA authority boundary: preserved
10. Governance Boundary

This LAB is read-only and deterministic.

It does not:

exploit AWS
mutate a customer environment
deploy live infrastructure
invoke AWS APIs against customer accounts
enumerate real buckets
access public objects
execute remediation
issue tokens
create runtime sessions
override OPA

Authority boundary:

Runtime = source of truth
OPA = decision authority
Aegis = bounded intelligence
Frontend = rendering only
11. Completion Criteria

This LAB is complete when:

metadata.json exists and is valid
architecture.md exists
index.html renders the applied L2 page
Mobile Study Menu exists
Concept Deep Dives exist
Visual S3 exposure model exists
manifest.json exposes the lab
AWS Intermediate Identity Track links the lab
homepage renders the lab with INTERMEDIATE maturity
