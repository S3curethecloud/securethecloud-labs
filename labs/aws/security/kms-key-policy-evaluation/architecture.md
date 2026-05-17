# AWS KMS Key Policy Evaluation

## 1. LAB Purpose

This L2 Intermediate LAB teaches how AWS KMS key policies participate in cryptographic access decisions.

KMS authorization is critical because encrypted data may remain inaccessible even when a principal can reach the surrounding AWS service.

A principal may have access to an S3 object, EBS volume, RDS snapshot, Lambda environment variable, or secret, but still fail if KMS denies decrypt authority.

---

## 2. Why This Matters

KMS is a high-value enterprise security control.

It protects:

- S3 objects encrypted with customer-managed keys
- EBS volumes
- RDS snapshots
- Secrets Manager secrets
- Lambda environment variables
- CloudTrail log encryption
- application data encryption workflows

KMS access often depends on multiple layers:

```text
IAM identity policy
KMS key policy
KMS grants
encryption context
SCP guardrails
explicit deny
service integration context
3. Core Concept
IAM policy = what the principal is allowed to request

KMS key policy = what the key permits

KMS grant = delegated permission to use the key under defined conditions

Encryption context = request metadata that can constrain cryptographic operations

Effective KMS access = identity-side allow + key-side allow/grant + context match + no explicit deny

KMS key policies are especially important because they define who can administer and use the key.

4. IAM Allow Alone May Not Be Enough

A principal may have an IAM policy allowing:

kms:Decrypt

But the request can still fail if the KMS key policy does not allow the principal, account, role, service, or grant path.

KMS access must be evaluated as a combined decision.

5. Visual Model
Principal
    ↓
IAM Identity Policy
    ↓
KMS Key Policy
    ↓
Grant / Encryption Context
    ↓
SCP / Explicit Deny Check
    ↓
Effective KMS Decision

Decision logic:

IAM allows + key policy allows = possible allow

IAM allows + key policy denies or omits trust = deny

Key policy allows + encryption context mismatch = deny

Grant permits + context matches = possible allow

Explicit deny anywhere = deny
6. Example Scenario

A workload role has an IAM policy allowing decrypt:

{
  "Effect": "Allow",
  "Action": "kms:Decrypt",
  "Resource": "arn:aws:kms:us-east-1:111111111111:key/example-key-id"
}

But the KMS key policy only allows a different role:

{
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::111111111111:role/ApprovedDataReader"
  },
  "Action": [
    "kms:Decrypt",
    "kms:DescribeKey"
  ],
  "Resource": "*"
}

If the workload role is not trusted by the key policy or covered by a valid grant, the final result is:

DENY

The IAM policy allowed the request, but the key policy did not trust the principal.

7. Relationship to S3 Public Access Risk

S3 public access and KMS access can produce different exposure outcomes.

A bucket may expose an object path publicly, but if the object is encrypted with a KMS key that does not allow public decrypt, the data may remain cryptographically protected.

However, if KMS permissions are overly broad, encryption may not reduce exposure.

This is why KMS key policy evaluation is a natural follow-up to S3 Public Access Risk.

8. Relationship to Principal LABs

KMS authorization prepares learners for Principal LABs because privilege escalation often targets access to encrypted data or the ability to change key administration paths.

Relevant Principal LAB connections:

iam:PassRole privilege escalation
Cross-account role escalation
Role chaining escalation

A principal that can pass or assume a role with KMS authority may gain access to encrypted data even without direct access under its original identity.

9. Shield / Aegis Boundary

This L2 LAB is Shield-aware but does not create a Shield finding by itself.

Current status:

Shield finding required: false
Aegis runtime fixture required: false
Runtime change required: false
OPA authority boundary: preserved
10. Governance Boundary

This LAB is read-only and deterministic.

It does not:

exploit AWS
mutate a customer environment
deploy live infrastructure
invoke AWS APIs against customer accounts
enumerate real keys
decrypt real data
execute remediation
issue tokens
create runtime sessions
override OPA

Authority boundary:

Runtime = source of truth
OPA = decision authority
Aegis = bounded intelligence
Frontend = rendering only
11. Completion Criteria

This LAB is complete when:

metadata.json exists and is valid
architecture.md exists
index.html renders the L2 page
Mobile Study Menu exists
Concept Deep Dives exist
Visual KMS Authorization Model exists
manifest.json exposes the lab
AWS Intermediate Identity Track links the lab
homepage renders the lab with INTERMEDIATE maturity
