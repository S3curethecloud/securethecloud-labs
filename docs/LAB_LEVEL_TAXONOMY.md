# SecureTheCloud LAB Level Taxonomy

Status: Active / Curriculum Authority

## Purpose

SecureTheCloud Labs are organized into a level-based curriculum that supports students, interns, mentors, security engineers, and executive security leaders.

The level model prevents the platform from becoming a flat list of labs. It defines a progression from foundational understanding to intermediate reasoning, principal-level attack-path modeling, and future executive decision intelligence.

---

## LAB Levels

### L1 — Foundation LABs

Purpose:

```text
Teach core cloud security primitives, identity concepts, and policy reasoning.

Audience:

students
interns
new cloud security engineers
interview preparation

Characteristics:

concept-first
beginner-safe
read-only
no live mutation
no exploitation
no runtime dependency required
teaches vocabulary and mental models

Examples:

aws-iam-basics
azure-entra-id-basics
gcp-iam-basics
L2 — Intermediate LABs

Purpose:

Teach realistic cloud misconfiguration reasoning and deterministic evaluation paths.

Audience:

students moving beyond basics
interns entering real-world cloud security
security engineers building evidence reasoning
mentors teaching practical cloud security

Characteristics:

scenario-driven
deterministic reasoning
cloud control-plane focused
explains effective permissions
introduces evidence mapping
may be Shield-aligned
may be Aegis Runtime-eligible
does not require live exploitation

Examples:

aws-iam-policy-evaluation
aws-permission-boundary-basics
aws-s3-public-access-risk
aws-kms-key-policy-risk
aws-security-group-exposure
L3 — Principal LABs

Purpose:

Model advanced deterministic identity and attack-path scenarios with evidence linkage.

Audience:

senior engineers
principal engineers
security architects
platform security teams
CSO/CISO technical review

Characteristics:

advanced attack-path modeling
Shield deterministic finding linkage
Aegis Runtime mapping
OPA authority boundary
evidence record required
executive-readable explanation
no customer mutation
no live exploitation

Current Principal AWS Identity LABs:

aws-cross-account-role-escalation
aws-privilege-escalation-passrole
aws-role-chaining-escalation
L4 — Executive LABs

Purpose:

Translate technical cloud security paths into executive risk, blast-radius, governance, and decision intelligence.

Audience:

CSO
CISO
security leadership
audit stakeholders
board-level risk review
enterprise platform buyers

Characteristics:

risk narrative
governance posture
audit evidence
blast-radius explanation
decision summary
no tactical exploitation
grounded in L2/L3 evidence

Future examples:

executive-aws-identity-risk-brief
executive-cloud-identity-blast-radius-review
executive-zero-trust-runtime-decision-review
executive-audit-evidence-package-walkthrough
Curriculum Progression

Recommended AWS Identity progression:

L1: AWS IAM Basics
    ↓
L2: AWS IAM Policy Evaluation
    ↓
L3: AWS Principal Identity Track
    ↓
L4: Executive AWS Identity Risk Brief
Governance Boundary

All LAB levels remain read-only unless explicitly approved in a future controlled runtime phase.

The LAB platform does not:

exploit cloud environments
mutate customer infrastructure
deploy live infrastructure by default
execute remediation
issue runtime tokens through LAB content
override OPA
treat Aegis as enforcement authority
infer compromise from static learning artifacts

Authority model:

Runtime = source of truth
OPA = decision authority
Aegis = bounded intelligence
Frontend = rendering only
Current Strategy

Next build priority:

L2 Intermediate LABs

Reason:

The platform already has L1 foundation coverage and L3 Principal AWS identity coverage.
L2 now bridges beginner learning into deterministic security engineering reasoning.

First L2 LAB:

aws-iam-policy-evaluation


---

## AWS Principal Track Curriculum Linkage

The AWS Principal Identity Track is linked to the learning ladder:

```text
L1: AWS IAM Basics
    ↓
L2: AWS IAM Policy Evaluation
    ↓
L3: AWS Principal Identity Track

This linkage ensures that learners can progress from foundational IAM concepts into effective-permission reasoning before attempting Principal LABs such as:

cross-account role escalation
iam:PassRole privilege escalation
role chaining escalation

This curriculum linkage is educational and read-only.

No runtime, Shield, Aegis, or OPA logic changes are introduced by this linkage.

---

## AWS Intermediate Identity Track

The AWS Intermediate Identity Track is the L2 learning lane between AWS IAM Basics and the AWS Principal Identity Track.

Track path:

```text
/tracks/aws-intermediate-identity/

Current active L2 LAB:

aws-iam-policy-evaluation

Planned next L2 LABs:

aws-permission-boundary-basics
aws-scp-guardrail-reasoning
aws-resource-policy-evaluation
aws-s3-public-access-risk

Curriculum purpose:

Teach effective-permission reasoning before learners enter Principal LABs.

This track is read-only and educational.

No runtime, Shield, Aegis, or OPA logic changes are introduced by this track page.
