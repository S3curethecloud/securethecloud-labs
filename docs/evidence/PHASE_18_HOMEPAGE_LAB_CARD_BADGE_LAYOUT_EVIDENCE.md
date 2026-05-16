# Phase 18 — Homepage LAB Card Badge Layout Evidence Record

Status: Evidence Recorded / UI Polish Verified

## 1. Purpose

This phase records the homepage LAB card UI polish that resolved maturity badge ambiguity.

The issue was visual, not data-related.

The manifest, lab metadata, and dynamic renderer were already using the correct maturity values, but the old layout allowed badges to visually appear associated with the neighboring lab card.

---

## 2. UI Problem

Observed ambiguity:

```text
Open Lab →
PRINCIPAL

or:

Open Lab →
STARTER

The badge could visually look attached to the wrong lab because cards were not strongly separated and the badge appeared below the Open Lab link.

3. UI Resolution

The homepage card layout was improved so every lab renders as a distinct card and each maturity badge is placed inside the lab card header.

Expected final visual mapping:

AWS IAM Basics                              GOLD
AWS Cross-Account Role Escalation           PRINCIPAL
AWS Privilege Escalation via iam:PassRole   PRINCIPAL
AWS Role Chaining Escalation                PRINCIPAL
Azure Entra ID Basics                       STARTER
GCP IAM Basics                              STARTER
4. Repository Evidence

Repository:

securethecloud-labs

UI clarity CSS commit:

4192f8c

Badge header JS commit:

1734d05

Homepage renderer cache-bust commit:

e31e445

Files changed:

assets/css/labs.css
assets/js/labs.js
index.html
5. Production Verification

Production site:

https://labs.securethecloud.dev/

Production verification status:

true

Verified production behavior:

Homepage LAB cards are visually separated: true
Maturity badge appears inside each card header: true
AWS IAM Basics renders GOLD: true
Cross-account lab renders PRINCIPAL: true
PassRole lab renders PRINCIPAL: true
Role Chaining lab renders PRINCIPAL: true
Azure starter track renders STARTER: true
GCP starter track renders STARTER: true
6. Source-of-Truth Verification

Manifest remained valid:

true

Manifest maturity values:

aws-iam-basics: gold
aws-cross-account-role-escalation: principal
aws-privilege-escalation-passrole: principal
aws-role-chaining-escalation: principal
azure-entra-id-basics: starter
gcp-iam-basics: starter

Homepage renderer source:

assets/js/labs.js

Renderer field:

lab.maturity

Cache-busted script reference:

/assets/js/labs.js?v=homepage-badge-header-1734d05
7. Boundary

This phase changed UI rendering only.

It did not change:

manifest data
lab metadata
runtime mapping
Shield findings
Aegis Runtime logic
OPA authority
Intelligence Core datasets
Cloudflare routing
production runtime behavior
8. Governance Boundary

The homepage remains read-only and deterministic.

It does not:

exploit AWS
mutate infrastructure
deploy live cloud resources
issue tokens
create sessions
override OPA
treat Aegis as enforcement authority

Authority boundary remains:

Runtime = source of truth
OPA = decision authority
Aegis = bounded intelligence
Frontend = rendering only
9. Completion Verdict
PHASE 18 STATUS: COMPLETE
HOMEPAGE LAB CARD BADGE LAYOUT: VERIFIED
BADGE OWNERSHIP AMBIGUITY: RESOLVED
PRINCIPAL LAB BADGES: VERIFIED
STARTER TRACK BADGES: VERIFIED
AWS IAM GOLD BADGE: VERIFIED
MANIFEST DRIFT: FALSE
RUNTIME CHANGE REQUIRED: NO
OPA AUTHORITY: PRESERVED

