# Phase 40 — AWS Resource Policy Evaluation L2 LAB Evidence Record

Status: Evidence Recorded / L2 LAB Verified

## 1. LAB Identity

LAB ID:

```text
aws-resource-policy-evaluation

LAB title:

AWS Resource Policy Evaluation

Maturity:

intermediate

Taxonomy level:

L2

Track:

AWS Intermediate Identity Track

Purpose:

Teach how AWS resource-based policies participate in authorization decisions alongside identity policies, boundaries, SCPs, and explicit deny.
2. Repository Evidence

Implementation commit:

849f0ff

Commit message:

Add L2 AWS resource policy evaluation lab

Repository:

securethecloud-labs

Files created:

labs/aws/identity/resource-policy-evaluation/metadata.json
labs/aws/identity/resource-policy-evaluation/architecture.md
labs/aws/identity/resource-policy-evaluation/index.html

Files updated:

manifest.json
tracks/aws-intermediate-identity/index.html
docs/LAB_LEVEL_TAXONOMY.md
3. LAB Page Evidence

LAB page path:

/labs/aws/identity/resource-policy-evaluation/

Production URL:

https://labs.securethecloud.dev/labs/aws/identity/resource-policy-evaluation/

LAB page visible:

true

Verified page markers:

AWS Resource Policy Evaluation
Study Menu
Concept Deep Dives
What is a resource policy?
Visual Resource Policy Model
Runtime = source of truth
4. UX Evidence

Mobile Study Menu:

true

Concept Deep Dives:

true

Visual Resource Policy Model:

true

Visual learning included:

true

Native HTML/CSS only:

true

No JavaScript dependency:

true
5. Manifest Evidence

Manifest exposed:

true

Manifest fields:

id: aws-resource-policy-evaluation
level: intermediate
maturity: intermediate
path: /labs/aws/identity/resource-policy-evaluation/
6. Track Evidence

AWS Intermediate Track linked:

true

Track page:

/tracks/aws-intermediate-identity/

Track now includes:

AWS IAM Policy Evaluation
AWS Permission Boundary Basics
AWS SCP Guardrail Reasoning
AWS Resource Policy Evaluation

Curriculum ladder:

L1: AWS IAM Basics
    ↓
L2: AWS Intermediate Identity Track
    ├── AWS IAM Policy Evaluation
    ├── AWS Permission Boundary Basics
    ├── AWS SCP Guardrail Reasoning
    └── AWS Resource Policy Evaluation
    ↓
L3: AWS Principal Identity Track
7. Deployment Verification

pages.dev verified:

true

custom domain verified:

true

Production manifest verified:

true

Production LAB page verified:

true

Production AWS Intermediate Track linkage verified:

true

custom domain cache status:

DYNAMIC

No cache drift detected:

true
8. Runtime / Shield / Aegis Boundary

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
9. Governance Boundary

This phase added a static L2 LAB only.

It did not:

exploit AWS
mutate customer infrastructure
deploy live cloud resources
invoke AWS APIs against customer accounts
execute remediation
issue runtime tokens
create runtime sessions
override OPA
create a Shield finding
create an Aegis Runtime fixture
modify OPA policy logic
10. Completion Verdict
PHASE 40 STATUS: COMPLETE
AWS RESOURCE POLICY EVALUATION L2 LAB: VERIFIED
COMMIT: 849f0ff
LAB ID: aws-resource-policy-evaluation
MATURITY: intermediate
TAXONOMY LEVEL: L2
MOBILE STUDY MENU: true
CONCEPT DEEP DIVES: true
VISUAL RESOURCE POLICY MODEL: true
MANIFEST EXPOSED: true
AWS INTERMEDIATE TRACK LINKED: true
PAGES.DEV VERIFIED: true
CUSTOM DOMAIN VERIFIED: true
RUNTIME CHANGE REQUIRED: false
SHIELD FINDING CREATED: false
AEGIS FIXTURE REQUIRED: false
OPA AUTHORITY: PRESERVED

