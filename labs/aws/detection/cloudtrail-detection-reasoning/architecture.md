# AWS CloudTrail Detection Reasoning

## 1. LAB Purpose

This L2 Intermediate LAB teaches how CloudTrail evidence supports detection reasoning.

The earlier L2 labs explain how AWS authorization and workload identity work.

This lab explains how analysts observe security-relevant activity after it happens.

CloudTrail is the evidence layer for:

- iam:PassRole
- sts:AssumeRole
- Lambda function updates
- Secrets Manager retrieval
- KMS decrypt
- cross-account access
- workload identity activity

---

## 2. Why This Matters

Security teams need to answer evidence questions:

```text
Who made the request?
What API was called?
Which resource was targeted?
Which role or session was used?
Was the event successful or denied?
Was this direct human access or workload-driven access?
What happened before and after?

CloudTrail helps convert cloud activity into investigation evidence.

3. Core Concept
Authorization reasoning = could this happen?

Detection reasoning = what evidence shows that it happened or was attempted?

CloudTrail event = API activity record

Detection signal = meaningful event pattern

Investigation context = identity, resource, time, source, session, and outcome

CloudTrail does not automatically prove business impact.

It provides event evidence that must be interpreted.

4. High-Value CloudTrail Events

Important L2 detection events include:

iam:PassRole
sts:AssumeRole
lambda:CreateFunction
lambda:UpdateFunctionCode
lambda:UpdateFunctionConfiguration
secretsmanager:GetSecretValue
kms:Decrypt
s3:GetObject
s3:PutBucketPolicy

These events help connect authorization paths to observable behavior.

5. Visual Detection Model
Principal / Workload
    ↓
AWS API Call
    ↓
CloudTrail Event
    ↓
Detection Rule / Analyst Query
    ↓
Investigation Context
    ↓
Evidence-Based Decision

Decision logic:

High-risk API call + sensitive resource = detection candidate

PassRole + Lambda create/update = workload identity risk signal

GetSecretValue + KMS Decrypt = secret retrieval evidence path

AssumeRole + cross-account target = trust-path investigation

AccessDenied event = attempted path, not confirmed success

Successful event = action happened, impact still requires context
6. Example Scenario

A developer updates Lambda function code:

eventSource: lambda.amazonaws.com
eventName: UpdateFunctionCode
userIdentity.type: AssumedRole
requestParameters.functionName: prod-secret-reader

Shortly after, the execution role retrieves a secret and decrypts it:

eventSource: secretsmanager.amazonaws.com
eventName: GetSecretValue

eventSource: kms.amazonaws.com
eventName: Decrypt

Detection reasoning:

Lambda code changed
Function may run under execution role
Execution role can retrieve secret
KMS decrypt occurred
Workload identity risk requires investigation
7. Relationship to L2 Authorization Model

CloudTrail Detection Reasoning connects to all current L2 labs:

IAM Policy Evaluation:
Who could call the API?

Permission Boundary Basics:
Was authority constrained?

SCP Guardrail Reasoning:
Was the action blocked or allowed at the org layer?

Resource Policy Evaluation:
Was resource-side trust involved?

S3 Public Access Risk:
Was storage exposure changed or accessed?

KMS Key Policy Evaluation:
Was decrypt authority exercised?

Secrets Manager Access Evaluation:
Was a secret value retrieved?

Lambda Execution Role Risk:
Did a workload identity execute sensitive access?
8. Relationship to Principal LABs

Principal LABs become stronger when learners can trace evidence.

Relevant Principal LAB connections:

iam:PassRole privilege escalation
Cross-account role escalation
Role chaining escalation

CloudTrail helps learners ask:

Was a role passed?
Was a role assumed?
Was the target role cross-account?
Was the chained role used?
Was the session used to access secrets, KMS, S3, or Lambda?
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

query customer CloudTrail
invoke AWS APIs against customer accounts
enumerate real events
deploy detection rules
create alerts
execute remediation
create Shield findings
create Aegis fixtures
issue runtime tokens
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
Visual CloudTrail Detection Model exists
manifest.json exposes the lab
AWS Intermediate Identity Track links the lab
homepage renders the lab with INTERMEDIATE maturity
