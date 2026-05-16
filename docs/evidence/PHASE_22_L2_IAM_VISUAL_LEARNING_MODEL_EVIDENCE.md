# Phase 22 — L2 IAM Visual Learning Model Evidence Record

Status: Evidence Recorded / Visual Learning Model Verified

## 1. LAB Identity

LAB ID:

```text
aws-iam-policy-evaluation

LAB title:

AWS IAM Policy Evaluation

Taxonomy level:

L2

Maturity:

intermediate
2. Visual Learning Commit

Visual learning commit:

1950cda

Commit message:

Add visual learning model to L2 IAM policy lab

Files changed:

assets/css/labs.css
labs/aws/identity/iam-policy-evaluation/index.html
labs/aws/identity/iam-policy-evaluation/architecture.md
3. Visual Model Evidence

Visual model added:

true

Visual model type:

native HTML/CSS box-and-arrow decision model

No external image dependency:

true

Visual model includes:

Principal
Action
Resource
Context
Identity Policy
Resource Policy
Permission Boundary
SCP
Explicit Deny
Effective Permission
Allow / Deny
4. Production Verification

Production LAB page:

https://labs.securethecloud.dev/labs/aws/identity/iam-policy-evaluation/

Production page contains:

Visual Evaluation Model: true
Explicit Deny?: true
Effective Permission: true
IAM evaluation learning rule: true

Production CSS contains:

visual-flow: true
visual-flow-row: true
visual-node: true
visual-arrow: true
visual-note: true
5. Learning Rule

The visual model teaches:

IAM evaluation is not “find an allow.”
It is “check for deny, then prove an allow survives every boundary.”

Purpose:

Help students, interns, and engineers reason through IAM authorization as a deterministic decision path.
6. Curriculum Placement

This visual model strengthens the L2 bridge between:

L1: AWS IAM Basics

and:

L3: AWS Principal Identity Track

Principal LAB preparation:

aws-cross-account-role-escalation
aws-privilege-escalation-passrole
aws-role-chaining-escalation
7. Runtime / Shield / Aegis Boundary

Runtime change required:

false

Shield finding created:

false

Aegis fixture required:

false

Shield/Aegis/OPA logic change:

false

OPA authority preserved:

true

Authority model:

Runtime = source of truth
OPA = decision authority
Aegis = bounded intelligence
Frontend = rendering only
8. Governance Boundary

This phase changed visual learning content only.

It did not:

exploit AWS
mutate customer infrastructure
deploy live infrastructure
invoke AWS APIs against customer accounts
execute remediation
issue runtime tokens
create runtime sessions
override OPA
treat Aegis as enforcement authority
9. Completion Verdict
PHASE 22 STATUS: COMPLETE
L2 IAM VISUAL LEARNING MODEL: VERIFIED
LAB: aws-iam-policy-evaluation
VISUAL MODEL ADDED: true
EXPLICIT DENY VISUALIZED: true
EFFECTIVE PERMISSION VISUALIZED: true
NO EXTERNAL IMAGE DEPENDENCY: true
MANIFEST VALID: true
RUNTIME CHANGE REQUIRED: false
SHIELD FINDING CREATED: false
AEGIS FIXTURE REQUIRED: false
OPA AUTHORITY: PRESERVED

