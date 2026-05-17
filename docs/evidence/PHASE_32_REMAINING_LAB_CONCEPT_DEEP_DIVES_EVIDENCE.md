# Phase 32 — Remaining LAB Concept Deep Dives Evidence Record

Status: Evidence Recorded / Concept Deep Dives Verified

## 1. Purpose

This phase records the addition of collapsible Concept Deep Dive learning windows across the remaining starter and Principal LAB pages.

The purpose was to improve:

```text
student learning
intern mentorship
executive explanation
mobile study flow
topic drill-down without page clutter
2. Repository Evidence

Implementation commit:

90e9266

Commit message:

Add concept deep dives to remaining lab pages

Repository:

securethecloud-labs

Files changed:

labs/aws/identity/cross-account-role-escalation/index.html
labs/aws/identity/iam-basics/index.html
labs/aws/identity/privilege-escalation-passrole/index.html
labs/aws/identity/role-chaining-escalation/index.html
labs/azure/identity/entra-id-basics/index.html
labs/gcp/identity/iam-basics/index.html
3. LAB Pages Updated

PassRole concept deep dives:

true

Cross-account concept deep dives:

true

Role chaining concept deep dives:

true

AWS IAM Basics concept deep dives:

true

Azure Entra ID Basics concept deep dives:

true

GCP IAM Basics concept deep dives:

true
4. Concept Topics Added

PassRole LAB:

What is iam:PassRole?
Why does compute creation matter?
Why is this privilege escalation?
What should executives understand?

Cross-Account LAB:

What is cross-account trust?
What is sts:AssumeRole?
Why does trust policy shape blast radius?
What should reviewers look for?

Role Chaining LAB:

What is role chaining?
Why does transitive trust matter?
What is session context?
What should executives understand?

AWS IAM Basics:

What is an IAM principal?
What is an IAM policy?
What is an IAM role?
What does least privilege mean?

Azure Entra ID Basics:

What is Microsoft Entra ID?
What is Conditional Access?
What is Azure RBAC?
Why does federation matter?

GCP IAM Basics:

What is Google Cloud IAM?
What is a service account?
What is Workspace identity?
What is Workload Identity Federation?
5. UX Implementation

Native details/summary accordions:

true

No JavaScript dependency:

true

Reusable CSS already exists:

concept-grid
concept-card
concept-card-body

Mobile Study Menu compatibility:

true

Desktop side navigation compatibility:

true
6. Production Verification

Production verification target:

https://labs.securethecloud.dev/

Verified page paths:

/labs/aws/identity/privilege-escalation-passrole/
/labs/aws/identity/cross-account-role-escalation/
/labs/aws/identity/role-chaining-escalation/
/labs/aws/identity/iam-basics/
/labs/azure/identity/entra-id-basics/
/labs/gcp/identity/iam-basics/

Production markers expected:

Concept Deep Dives
What is iam:PassRole?
What is cross-account trust?
What is role chaining?
What is an IAM principal?
What is Microsoft Entra ID?
What is Google Cloud IAM?

Production concept deep dives verified:

true
7. Runtime / Shield / Aegis Boundary

Runtime change required:

false

Shield finding change required:

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

This phase changed frontend learning content only.

It did not:

exploit AWS
mutate customer infrastructure
deploy live cloud resources
invoke AWS APIs against customer accounts
execute remediation
issue runtime tokens
create runtime sessions
override OPA
modify Shield findings
modify Aegis Runtime logic
modify OPA policy logic
9. Completion Verdict
PHASE 32 STATUS: COMPLETE
REMAINING LAB CONCEPT DEEP DIVES: VERIFIED
COMMIT: 90e9266
PASSROLE CONCEPT DEEP DIVES: true
CROSS-ACCOUNT CONCEPT DEEP DIVES: true
ROLE CHAINING CONCEPT DEEP DIVES: true
AWS IAM BASICS CONCEPT DEEP DIVES: true
AZURE ENTRA ID BASICS CONCEPT DEEP DIVES: true
GCP IAM BASICS CONCEPT DEEP DIVES: true
NATIVE DETAILS/SUMMARY ACCORDIONS: true
NO JAVASCRIPT DEPENDENCY: true
RUNTIME CHANGE REQUIRED: false
SHIELD/AEGIS/OPA LOGIC CHANGE: false
OPA AUTHORITY: PRESERVED

