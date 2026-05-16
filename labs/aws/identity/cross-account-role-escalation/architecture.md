# Architecture & Trust Modeling — Cross-Account Role Escalation

## 1. Environment Topology

We model two AWS accounts:

- Account A (Target / Privileged)
- Account B (External / Potentially Compromised)

Account A contains a highly privileged IAM role:

- Role Name: AdminAccessRole
- Attached Policy: AdministratorAccess

The objective is to analyze how a principal in Account B
can escalate privileges into Account A.

---

## 2. Identity Flow Diagram (Logical)

Account B Principal
    ↓
sts:AssumeRole
    ↓
Account A AdminAccessRole
    ↓
Full Administrative Permissions

This is a trust-boundary traversal.

---

## 3. Vulnerable Trust Policy Example (BAD)

Below is a permissive trust policy on Account A’s AdminAccessRole:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::222222222222:root"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```


---

## 4. Why This Is Risky

This trust policy allows the root principal of Account B to assume a highly privileged role in Account A.

This does not require software exploitation.

The risk exists because the identity configuration creates a reachable privilege path.

Shield models this as identity reachability:

```text
External Principal → sts:AssumeRole → AdminAccessRole → AdministratorAccess
```

## 5. What Shield Detects

Shield detects the deterministic relationship between:

an external trusted principal
an assumable privileged role
an attached high-privilege policy
the resulting administrative blast radius

Finding:

Cross-Account Role Escalation Path Detected

Category:

Identity → Cross-Account Trust

Severity:

HIGH

Linked lab:

aws-cross-account-role-escalation

## 6. Why This Is Deterministic

This finding is deterministic because it is derived from static IAM configuration:

trust policy allows sts:AssumeRole
trusted principal belongs to another account
target role has administrative permissions
no exploit chain is required
no runtime behavior is assumed

If those conditions exist, the path exists.

## 7. Fix Guidance

Constrain the trust relationship.

Recommended controls:

avoid trusting external account root principals
trust only specific role ARNs
require sts:ExternalId where appropriate
scope permissions attached to assumable roles
review cross-account trust paths regularly

Example safer trust pattern:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::222222222222:role/ApprovedExternalRole"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "sts:ExternalId": "approved-external-id"
        }
      }
    }
  ]
}
```

## 8. Governance Boundary

This lab is read-only and deterministic.

It does not:

exploit a vulnerability
mutate a customer environment
execute remediation
assume runtime compromise
infer access paths not present in IAM configuration

The lab exists to teach and validate identity reachability modeling.

## 9. Lab ↔ Shield Linkage

Stable lab identifier:

aws-cross-account-role-escalation

Expected Shield finding identifier:

shield-xacct-001

This lab is intended to anchor the Shield finding:

Cross-Account Role Escalation Path Detected

The Shield finding must link back to this lab using the stable lab identifier, not an ad-hoc URL.

## 10. Completion Criteria

This lab is complete enough to cite when:

metadata.json contains stable lab_id
architecture.md renders correctly
lab appears in manifest.json
Shield finding includes linked lab metadata
AI Explain can cite the lab dataset
Shield UI renders “View linked lab”

---

## 11. Aegis Runtime Mapping

This lab is mapped to Aegis Runtime / Decision Intelligence.

Aegis Runtime evaluates the runtime security meaning of the cross-account identity path using bounded signals such as:

- principal identity
- requested intent
- action scope
- runtime risk
- identity integrity
- recent denial pressure
- policy drift
- session context where applicable

For this lab, the relevant Aegis runtime path is:

```text
External Account Principal
    ->
sts:AssumeRole intent
    ->
Privileged account role trust relationship
    ->
Administrative blast radius
    ->
Cross-account privilege escalation risk signal

Expected Aegis scenario:

cross_account_assume_role_escalation_path

Expected Aegis signal:

IDENTITY_DRIFT_DETECTED

Expected minimum risk modifier:

>= 20

Aegis does not enforce this finding.

Aegis may enrich the operator view with bounded signal interpretation, but the decision boundary remains:

Runtime = source of truth
OPA = decision authority
Aegis = bounded intelligence
Frontend = rendering only

This preserves the SecureTheCloud governance model while allowing the lab to teach how cross-account trust misconfiguration becomes runtime identity risk.
