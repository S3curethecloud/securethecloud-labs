# Phase 20 — AWS IAM Policy Evaluation L2 LAB Evidence Record

Status: Evidence Recorded / L2 LAB Verified

## 1. LAB Identity

LAB ID:

```text
aws-iam-policy-evaluation

Title:

AWS IAM Policy Evaluation

Maturity:

intermediate

Taxonomy level:

L2

Track:

AWS Identity Engineering

Purpose:

Intermediate LAB teaching AWS effective-permission reasoning across identity policies, resource policies, permission boundaries, session policies, SCPs, and explicit deny.
2. Repository Evidence

Repository:

securethecloud-labs

LAB files commit:

dc36c09

Commit message:

Add L2 AWS IAM policy evaluation lab

Manifest exposure commit:

8f05ad7

Commit message:

Expose L2 IAM policy evaluation lab in manifest

Files created:

labs/aws/identity/iam-policy-evaluation/metadata.json
labs/aws/identity/iam-policy-evaluation/architecture.md
labs/aws/identity/iam-policy-evaluation/index.html

Files updated:

manifest.json
assets/css/labs.css
3. LAB Artifact Evidence

Required LAB files:

metadata.json
architecture.md
index.html

Validation status:

metadata.json valid: true
manifest.json valid: true
architecture.md created: true
index.html created: true

LAB page path:

/labs/aws/identity/iam-policy-evaluation/

Production URL:

https://labs.securethecloud.dev/labs/aws/identity/iam-policy-evaluation/
4. Homepage Evidence

Homepage visible:

true

Homepage card expected:

AWS IAM Policy Evaluation

Homepage maturity badge:

INTERMEDIATE

Homepage manifest exposure:

true

Manifest fields:

id: aws-iam-policy-evaluation
cloud: aws
domain: identity
level: intermediate
maturity: intermediate
taxonomy_level: L2
principal_prerequisite: true
5. LAB Page Evidence

LAB page visible:

true

Verified page content includes:

AWS IAM Policy Evaluation
L2 Intermediate
Evaluation Model
Explicit deny overrides allow.
OPA = decision authority

LAB navigation present:

true

Governance boundary present:

true
6. Curriculum Evidence

This LAB bridges:

L1: AWS IAM Basics

to:

L3: AWS Principal Identity Track

Principal LAB prerequisite:

true

Principal LABs supported by this prerequisite:

aws-cross-account-role-escalation
aws-privilege-escalation-passrole
aws-role-chaining-escalation

Reason:

Effective-permission reasoning is required before safely teaching cross-account trust, iam:PassRole privilege escalation, and role chaining.
7. Shield / Aegis / Runtime Boundary

Shield finding created:

false

Aegis fixture required:

false

Runtime change required:

false

Intelligence Core change required:

false

OPA authority preserved:

true

Current status:

L2 learning bridge only.
No Shield finding required yet.
No Aegis Runtime fixture required yet.
No runtime or OPA logic change required.
8. Governance Boundary

This L2 LAB is read-only and deterministic.

It does not:

exploit AWS
mutate customer infrastructure
deploy live infrastructure
invoke AWS APIs against customer accounts
execute remediation
issue tokens
create runtime sessions
override OPA
treat Aegis as enforcement authority

Authority model:

Runtime = source of truth
OPA = decision authority
Aegis = bounded intelligence
Frontend = rendering only
9. Completion Verdict
PHASE 20 STATUS: COMPLETE
AWS IAM POLICY EVALUATION L2 LAB: VERIFIED
L2 LAB ID: aws-iam-policy-evaluation
MATURITY: intermediate
TAXONOMY LEVEL: L2
HOMEPAGE VISIBLE: true
LAB PAGE VISIBLE: true
PRINCIPAL LAB PREREQUISITE: true
SHIELD FINDING CREATED: false
AEGIS FIXTURE REQUIRED: false
RUNTIME CHANGE REQUIRED: false
OPA AUTHORITY: PRESERVED
ARCHITECTURE CHANGE REQUIRED: NO

