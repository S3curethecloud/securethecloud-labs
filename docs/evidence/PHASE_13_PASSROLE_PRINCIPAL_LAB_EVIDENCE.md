# Phase 13 — PassRole Principal LAB Evidence Record

Status: Evidence Recorded / Principal LAB Locked

Recorded: 2026-05-16T01:52:34Z

## 1. LAB Identity

Lab ID:

```text
aws-privilege-escalation-passrole
```

Title:

```text
AWS Privilege Escalation via iam:PassRole
```

Maturity:

```text
principal
```

Category:

```text
Identity → Privilege Escalation
```

Linked Shield finding:

```text
shield-passrole-001
```

Runtime anchor:

```text
Aegis Runtime / Decision Intelligence
```

---

## 2. Repository Evidence

LAB repository:

```text
securethecloud-labs
```

LAB commit:

```text
039235f
```

Runtime repository:

```text
ztr-runtime-api-server.py-requirements.txt-fly.toml
```

Runtime commit:

```text
0c0d334
```

Intelligence Core repository:

```text
stc-intelligence-core
```

Intelligence Core commit:

```text
9ca3353
```

---

## 3. LAB Website Evidence

Production LAB website verified:

```text
true
```

PassRole LAB card visible:

```text
true
```

PassRole LAB page openable:

```text
true
```

Production path:

```text
https://labs.securethecloud.dev/labs/aws/identity/privilege-escalation-passrole/
```

Verified production LAB page content includes:

- LAB purpose
- Identity path
- Shield detection mapping
- Aegis Runtime Mapping
- Governance boundary
- Source artifacts

---

## 4. LAB Artifact Evidence

Required LAB files:

```text
labs/aws/identity/privilege-escalation-passrole/metadata.json
labs/aws/identity/privilege-escalation-passrole/architecture.md
labs/aws/identity/privilege-escalation-passrole/runtime-mapping.json
labs/aws/identity/privilege-escalation-passrole/index.html
```

Validation status:

```text
metadata.json valid: true
runtime-mapping.json valid: true
architecture.md includes Aegis Runtime Mapping: true
index.html renders Open Lab page: true
```

---

## 5. Intelligence Core Evidence

Finding ID:

```text
shield-passrole-001
```

Linked LAB:

```text
aws-privilege-escalation-passrole
```

Runtime anchor:

```text
aegis-runtime
```

Expected Aegis signal:

```text
IDENTITY_DRIFT_DETECTED
```

Expected minimum risk modifier:

```text
>= 20
```

Decision authority:

```text
OPA
```

Loader verification:

```text
shield-passrole-001 loaded: true
linked_lab loaded: true
runtime_anchor loaded: true
expected_aegis_signal loaded: true
decision_authority loaded: true
```

---

## 6. Aegis Runtime Evidence

Runtime fixture:

```text
fixtures/aegis/aws_privilege_escalation_passrole_identity_integrity.json
```

Runtime mapping document:

```text
docs/lab-mappings/aws-privilege-escalation-passrole-aegis-runtime.md
```

Runtime unit test:

```text
tests/test_aegis_identity.py::test_passrole_lab_maps_to_aegis_identity_drift_signal
```

Runtime test result:

```text
10 passed
```

Expected signal:

```text
IDENTITY_DRIFT_DETECTED
```

Expected risk modifier:

```text
>= 20
```

Decision authority preserved:

```text
OPA
```

---

## 7. Copilot Bridge Evidence

Copilot bridge preserved:

```text
true
```

Endpoint:

```text
/copilot/bridge/platform
```

CORS origin preserved:

```text
https://app.securethecloud.dev
```

Purpose:

```text
DDR Copilot / Deterministic Copilot platform bridge for Aegis Runtime platform summaries.
```

---

## 8. Governance Boundary

This Principal LAB remains read-only and deterministic.

It does not:

- exploit AWS
- mutate customer infrastructure
- deploy live infrastructure
- pass a real AWS role
- execute remediation
- issue tokens through Aegis
- create sessions through Aegis
- override OPA
- treat Aegis as enforcement authority
- rely on the old Shield UI as a blocker

Authority boundary:

```text
Runtime = source of truth
OPA = decision authority
Aegis = bounded intelligence
Frontend = rendering only
```

---

## 9. Completion Verdict

```text
PHASE 13 STATUS: COMPLETE
PASSROLE PRINCIPAL LAB: LOCKED
LAB WEBSITE: VERIFIED
AEGIS RUNTIME MAPPING: VERIFIED
INTELLIGENCE CORE FINDING: VERIFIED
COPILOT BRIDGE: PRESERVED
OPA AUTHORITY: PRESERVED
ARCHITECTURE CHANGE REQUIRED: NO
```
