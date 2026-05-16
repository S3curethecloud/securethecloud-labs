# Phase 15 — Role Chaining Principal LAB Evidence Record

Status: Evidence Recorded / Principal LAB Locked

## 1. LAB Identity

Lab ID:

```text
aws-role-chaining-escalation

Title:

AWS Role Chaining Escalation

Maturity:

principal

Category:

Identity → Role Chaining

Linked Shield finding:

shield-rolechain-001

Runtime anchor:

Aegis Runtime / Decision Intelligence
2. Repository Evidence

LAB repository:

securethecloud-labs

LAB commit:

331beb3

Runtime repository:

ztr-runtime-api-server.py-requirements.txt-fly.toml

Runtime commit:

56c70f4

Intelligence Core repository:

stc-intelligence-core

Intelligence Core commit:

b942e43
3. LAB Website Evidence

Production LAB website verified:

true

Role Chaining LAB card visible:

true

Role Chaining LAB page openable:

true

Production path:

https://labs.securethecloud.dev/labs/aws/identity/role-chaining-escalation/

Verified production LAB page content includes:

executive hero section
Principal LAB badge
status cards
sticky lab navigation
identity path
Shield detection panel
Aegis Runtime Mapping panel
governance boundary
source artifacts panel
4. LAB Artifact Evidence

Required LAB files:

labs/aws/identity/role-chaining-escalation/metadata.json
labs/aws/identity/role-chaining-escalation/architecture.md
labs/aws/identity/role-chaining-escalation/runtime-mapping.json
labs/aws/identity/role-chaining-escalation/index.html

Validation status:

metadata.json valid: true
runtime-mapping.json valid: true
architecture.md includes Aegis Runtime Mapping: true
index.html renders Principal LAB page: true
manifest entry exposes lab: true

Manifest evidence:

aws-role-chaining-escalation present: true
shield-rolechain-001 present: true
5. Intelligence Core Evidence

Finding ID:

shield-rolechain-001

Linked LAB:

aws-role-chaining-escalation

Runtime anchor:

aegis-runtime

Runtime surface:

Aegis Runtime / Decision Intelligence

Expected Aegis signal:

IDENTITY_DRIFT_DETECTED

Expected minimum risk modifier:

>= 20

Decision authority:

OPA

Loader verification:

shield-rolechain-001 loaded: true
linked_lab loaded: true
runtime_anchor loaded: true
runtime_surface loaded: true
expected_aegis_signal loaded: true
expected_minimum_risk_modifier loaded: true
decision_authority loaded: true
linked_runtime_mapping loaded: true

Deployed endpoint verification:

finding_count: 3
shield-rolechain-001 returned by deployed endpoint: true
aws-role-chaining-escalation returned by deployed endpoint: true
aegis-runtime returned by deployed endpoint: true
IDENTITY_DRIFT_DETECTED returned by deployed endpoint: true
6. Aegis Runtime Evidence

Runtime fixture:

fixtures/aegis/aws_role_chaining_escalation_identity_integrity.json

Runtime mapping document:

docs/lab-mappings/aws-role-chaining-escalation-aegis-runtime.md

Runtime unit test:

tests/test_aegis_identity.py::test_role_chaining_lab_maps_to_aegis_identity_drift_signal

Runtime test result:

12 passed

Expected signal:

IDENTITY_DRIFT_DETECTED

Expected risk modifier:

>= 20

Decision authority preserved:

OPA
7. AWS Principal Identity Track Evidence

Principal LAB track now includes:

aws-cross-account-role-escalation
aws-privilege-escalation-passrole
aws-role-chaining-escalation

All three Principal LABs have:

LAB page: true
manifest registration: true
runtime-mapping.json: true
Shield finding: true
Aegis Runtime fixture/test: true
Intelligence Core deployed finding: true
OPA authority preserved: true
8. Governance Boundary

This Principal LAB remains read-only and deterministic.

It does not:

exploit AWS
mutate customer infrastructure
deploy live infrastructure
assume a real AWS role
execute remediation
issue tokens through Aegis
create sessions through Aegis
override OPA
treat Aegis as enforcement authority
rely on the old Shield UI as a blocker

Authority boundary:

Runtime = source of truth
OPA = decision authority
Aegis = bounded intelligence
Frontend = rendering only
9. Completion Verdict
PHASE 15 STATUS: COMPLETE
ROLE CHAINING PRINCIPAL LAB: LOCKED
LAB WEBSITE: VERIFIED
RUNTIME MAPPING: VERIFIED
AEGIS FIXTURE: VERIFIED
AEGIS TEST RESULT: 12 passed
INTELLIGENCE CORE FINDING: VERIFIED
DEPLOYED SHIELD ENDPOINT: VERIFIED
OPA AUTHORITY: PRESERVED
ARCHITECTURE CHANGE REQUIRED: NO

