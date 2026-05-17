# AWS Secrets Manager Access Evaluation

## 1. LAB Purpose

This L2 Intermediate LAB teaches how AWS Secrets Manager access is evaluated.

Secrets Manager access is not only an IAM question.

A principal may need:

- IAM permission to request the secret
- Secrets Manager resource policy permission if cross-account or resource-side trust is involved
- KMS decrypt authority when the secret uses a customer-managed KMS key
- matching request context
- no explicit deny
- no organization guardrail blocking the action

---

## 2. Why This Matters

Secrets Manager protects high-value credentials and application secrets.

A secret can contain:

- database credentials
- API keys
- application tokens
- OAuth client secrets
- service credentials
- third-party integration keys

If secret access is misconfigured, a low-privilege or unintended principal may retrieve sensitive material.

If secret access is too restrictive, production workloads may break.

---

## 3. Core Concept

```text
IAM policy = can the principal request secret access?

Secret resource policy = does the secret trust this principal or account path?

KMS key policy = can the principal decrypt the encrypted secret value?

SCP / guardrail = does the organization permit this class of access?

Explicit deny = hard stop

Effective secret access = GetSecretValue allow + KMS decrypt allow + no deny
4. Secret Metadata vs Secret Value

A principal may be able to list or describe a secret without being able to retrieve the secret value.

Important distinction:

secretsmanager:ListSecrets = discover secret metadata

secretsmanager:DescribeSecret = inspect secret configuration

secretsmanager:GetSecretValue = retrieve sensitive secret material

kms:Decrypt = decrypt secret value when a customer-managed KMS key is used

The highest-risk operation is normally:

secretsmanager:GetSecretValue
5. Visual Model
Principal
    ↓
IAM Policy
    ↓
Secret Resource Policy
    ↓
KMS Key Policy / Grant
    ↓
SCP / Explicit Deny Check
    ↓
Effective Secret Access Decision

Decision logic:

IAM allows GetSecretValue + KMS allows Decrypt = possible secret retrieval

IAM allows GetSecretValue + KMS denies Decrypt = deny

Secret resource policy denies principal = deny

SCP denies secret retrieval or key usage = deny

Explicit deny anywhere = deny
6. Example Scenario

A workload role has IAM permission to retrieve a secret:

{
  "Effect": "Allow",
  "Action": "secretsmanager:GetSecretValue",
  "Resource": "arn:aws:secretsmanager:us-east-1:111111111111:secret:prod/db/password-*"
}

But the secret is encrypted with a customer-managed KMS key, and the role does not have decrypt authority on that key.

Final result:

DENY

The IAM policy allowed secret retrieval, but KMS blocked decrypt.

7. Relationship to KMS Key Policy Evaluation

Secrets Manager depends heavily on KMS.

A learner should understand:

Secrets Manager stores and retrieves the secret.

KMS protects the encrypted secret value.

IAM may allow the request.

KMS may still deny decrypt.

This is why Secrets Manager Access Evaluation naturally follows KMS Key Policy Evaluation.

8. Relationship to Principal LABs

Secrets are often the target after identity escalation.

Relevant Principal LAB connections:

iam:PassRole privilege escalation
Cross-account role escalation
Role chaining escalation

A principal that can assume, pass, or chain into a role with Secrets Manager and KMS authority may retrieve sensitive credentials.

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
enumerate real secrets
retrieve secret values
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
Visual Secrets Access Model exists
manifest.json exposes the lab
AWS Intermediate Identity Track links the lab
homepage renders the lab with INTERMEDIATE maturity
