# Architecture & Trust Modeling — AWS Privilege Escalation via iam:PassRole

## 1. Environment Topology

We model a single AWS account containing:

- a low-privilege IAM principal
- a high-privilege IAM role
- a compute service capable of assuming an execution role
- an IAM policy that allows the principal to pass the high-privilege role to the service

The objective is to analyze how `iam:PassRole` can create a deterministic privilege escalation path without requiring software exploitation.

---

## 2. Identity Flow Diagram (Logical)

```text
Low-Privilege Principal
    ↓
iam:PassRole
    ↓
Compute Service Creation or Update
    ↓
High-Privilege Execution Role
    ↓
Expanded Permissions / Administrative Blast Radius

This is an identity-controlled privilege escalation path.

3. Vulnerable Permission Pattern (BAD)

The low-privilege principal has permission to pass a high-privilege role:

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "iam:PassRole",
      "Resource": "arn:aws:iam::111111111111:role/AdminExecutionRole"
    }
  ]
}

This becomes dangerous when the same principal can create or update a service that accepts that role as an execution role.

Example service capability:

{
  "Effect": "Allow",
  "Action": [
    "lambda:CreateFunction",
    "lambda:UpdateFunctionConfiguration"
  ],
  "Resource": "*"
}
4. Why This Is Risky

iam:PassRole does not directly grant the caller the permissions of the role.

However, if the caller can pass a privileged role to a service they control or can update, they may cause that service to run with permissions that exceed the caller’s own authority.

This creates a deterministic privilege escalation path:

Principal → iam:PassRole → Lambda Execution Role → Elevated Permissions

The risk exists because the identity configuration allows the principal to bind a more privileged role to an executable service context.

5. What Shield Detects

Shield detects the deterministic relationship between:

a principal with iam:PassRole
a passable role with broader privileges
a service action that accepts an execution role
the resulting escalation path

Finding:

Privilege Escalation Path via iam:PassRole Detected

Category:

Identity → Privilege Escalation

Severity:

HIGH

Linked lab:

aws-privilege-escalation-passrole

Expected Shield finding identifier:

shield-passrole-001
6. Why This Is Deterministic

This finding is deterministic because it is derived from static IAM and service configuration:

the principal is allowed to call iam:PassRole
the role being passed has broader privileges than the principal
the principal is allowed to create or update a service that accepts that role
no exploit chain is required
no runtime compromise is assumed
no external telemetry is required

If those conditions exist, the escalation path exists.

7. Fix Guidance

Constrain iam:PassRole and the services that can receive roles.

Recommended controls:

restrict iam:PassRole to specific approved roles
use iam:PassedToService conditions
avoid allowing PassRole on administrative roles
restrict compute creation and update permissions
use permission boundaries for roles that can be passed
monitor for principals with both PassRole and service creation capability

Example safer PassRole pattern:

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "iam:PassRole",
      "Resource": "arn:aws:iam::111111111111:role/ApprovedLambdaExecutionRole",
      "Condition": {
        "StringEquals": {
          "iam:PassedToService": "lambda.amazonaws.com"
        }
      }
    }
  ]
}
8. Governance Boundary

This lab is read-only and deterministic.

It does not:

exploit a vulnerability
mutate a customer environment
execute remediation
deploy live infrastructure
invoke AWS APIs against customer accounts
assume runtime compromise
infer access paths not present in IAM configuration

The lab exists to teach and validate identity privilege escalation modeling.

9. Lab ↔ Shield Linkage

Stable lab identifier:

aws-privilege-escalation-passrole

Expected Shield finding identifier:

shield-passrole-001

This lab is intended to anchor the Shield finding:

Privilege Escalation Path via iam:PassRole Detected

The Shield finding must link back to this lab using the stable lab identifier, not an ad-hoc URL.

10. AI Explain Boundary

AI Explain may use this lab to explain:

why iam:PassRole can create escalation paths
why service creation or update permissions matter
why the finding is deterministic
what safer role-passing constraints look like

AI Explain must not:

invent cloud state not present in the dataset
suggest live exploitation
perform remediation
cite external web sources
treat the lab as evidence of customer compromise
11. Completion Criteria

This lab is complete enough to cite when:

metadata.json contains stable lab_id
architecture.md renders correctly
lab appears in manifest.json
Shield finding includes linked lab metadata
/shield/findings returns shield-passrole-001
AI Explain can cite the lab dataset
Shield UI renders “View linked lab”
