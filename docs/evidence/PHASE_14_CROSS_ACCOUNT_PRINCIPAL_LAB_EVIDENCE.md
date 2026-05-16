# Phase 14 — Cross-Account Principal LAB Evidence Record

Status: Evidence Recorded / Principal LAB Parity Complete

## 1. LAB Identity

Lab ID:

```text
aws-cross-account-role-escalation

Title:

AWS Cross-Account Role Escalation

Maturity:

principal

Category:

Identity → Cross-Account Trust

Linked Shield finding:

shield-xacct-001

Runtime anchor:

Aegis Runtime / Decision Intelligence
2. Repository Evidence

LAB repository:

securethecloud-labs

LAB commit:

43b1cd2

Runtime repository:

ztr-runtime-api-server.py-requirements.txt-fly.toml

Runtime commit:

c22ad0e

Intelligence Core repository:

stc-intelligence-core

Intelligence Core commit:

826f853
3. LAB Website Evidence

Production LAB website verified:

true

Cross-account LAB card visible:

true

Cross-account LAB page openable:

true

Production path:

https://labs.securethecloud.dev/labs/aws/identity/cross-account-role-escalation/

UI polish complete:

true

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

labs/aws/identity/cross-account-role-escalation/metadata.json
labs/aws/identity/cross-account-role-escalation/architecture.md
labs/aws/identity/cross-account-role-escalation/runtime-mapping.json
labs/aws/identity/cross-account-role-escalation/index.html
labs/aws/identity/cross-account-role-escalation/README.md
labs/aws/identity/cross-account-role-escalation/mgf-sync.lab.json

Validation status:

metadata.json valid: true
runtime-mapping.json valid: true
architecture.md includes Aegis Runtime Mapping: true
index.html renders Principal LAB page: true
manifest entry promoted to principal: true
5. Intelligence Core Evidence

Finding ID:

shield-xacct-001

Linked LAB:

aws-cross-account-role-escalation

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

shield-xacct-001 loaded: true
linked_lab loaded: true
runtime_anchor loaded: true
runtime_surface loaded: true
expected_aegis_signal loaded: true
expected_minimum_risk_modifier loaded: true
decision_authority loaded: true
linked_runtime_mapping loaded: true
6. Aegis Runtime Evidence

Runtime fixture:

fixtures/aegis/aws_cross_account_role_escalation_identity_integrity.json

Runtime mapping document:

docs/lab-mappings/aws-cross-account-role-escalation-aegis-runtime.md

Runtime unit test:

tests/test_aegis_identity.py::test_cross_account_lab_maps_to_aegis_identity_drift_signal

Runtime test result:

11 passed

Expected signal:

IDENTITY_DRIFT_DETECTED

Expected risk modifier:

>= 20

Decision authority preserved:

OPA
7. Starter Track Evidence

Starter tracks retained:

true

Retained starter/foundation labs:

aws-iam-basics
azure-entra-id-basics
gcp-iam-basics

Starter UI normalization complete:

true

Azure retained for future Principal LAB track:

true

GCP retained for future Principal LAB track:

true

Starter pages do not claim Shield or Aegis linkage until explicitly mapped:

true
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
PHASE 14 STATUS: COMPLETE
CROSS-ACCOUNT PRINCIPAL LAB: LOCKED
LAB WEBSITE: VERIFIED
RUNTIME MAPPING: VERIFIED
AEGIS FIXTURE: VERIFIED
AEGIS TEST RESULT: 11 passed
INTELLIGENCE CORE FINDING: VERIFIED
UI POLISH COMPLETE: true
STARTER TRACKS RETAINED: true
OPA AUTHORITY: PRESERVED
ARCHITECTURE CHANGE REQUIRED: NO

