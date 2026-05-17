# AWS Lambda Execution Role Risk

## 1. LAB Purpose

This L2 Intermediate LAB teaches how AWS Lambda execution roles create workload identity risk.

A Lambda function does not normally run with the permissions of the human or automation principal that created it.

It runs with its execution role.

That means risk can emerge when a principal can:

- create or update a Lambda function
- pass or attach an execution role
- update function code or environment variables
- invoke the function
- use the execution role to reach Secrets Manager, KMS, S3, or other resources

---

## 2. Why This Matters

Lambda execution role risk is an applied workload identity scenario.

It bridges:

```text
Secrets Manager Access Evaluation
KMS Key Policy Evaluation
iam:PassRole
Resource Policy Evaluation

A low-privilege identity may not directly access a secret, decrypt a key, or read a protected bucket.

But if it can update or create a Lambda function that runs under a stronger execution role, the workload may access those resources.

3. Core Concept
Caller identity = who creates, updates, or invokes the Lambda function

Execution role = the IAM role Lambda assumes when the function runs

Function code = what actions the workload performs

iam:PassRole = permission that allows a caller to attach a role to Lambda

Effective workload authority = execution role permissions + resource/KMS/secret access + runtime code path

The key question is:

Can this principal cause Lambda to run code under a role with stronger permissions?
4. Function Management vs Runtime Authority

A principal may have permissions like:

lambda:CreateFunction
lambda:UpdateFunctionCode
lambda:UpdateFunctionConfiguration
lambda:InvokeFunction
iam:PassRole

Those permissions control the function.

The execution role controls what the function can do at runtime.

This separation is why Lambda is important for workload identity risk.

5. Visual Model
Human / CI Principal
    ↓
Lambda Management Permission
    ↓
iam:PassRole Check
    ↓
Lambda Execution Role
    ↓
Runtime Access to Secrets / KMS / S3
    ↓
Effective Workload Risk

Decision logic:

Can update function + execution role has sensitive access = workload risk possible

Can pass strong role + create function = privilege expansion path possible

Can invoke function only + function performs sensitive action = controlled exposure depends on function behavior

No PassRole + no update authority = Lambda escalation path reduced

Explicit deny or boundary blocks role attachment = deny
6. Example Scenario

A developer role can update Lambda function code:

{
  "Effect": "Allow",
  "Action": [
    "lambda:UpdateFunctionCode",
    "lambda:InvokeFunction"
  ],
  "Resource": "arn:aws:lambda:us-east-1:111111111111:function:prod-secret-reader"
}

The Lambda execution role has permissions to retrieve a secret and decrypt it:

{
  "Effect": "Allow",
  "Action": [
    "secretsmanager:GetSecretValue",
    "kms:Decrypt"
  ],
  "Resource": "*"
}

If the developer can modify code that runs under the execution role, the function may retrieve sensitive data at runtime.

Final risk:

WORKLOAD IDENTITY RISK POSSIBLE

The developer may not have direct Secrets Manager or KMS authority, but the execution role does.

7. Relationship to Secrets Manager and KMS

Lambda commonly reads secrets and decrypts data.

A workload risk path may involve:

Lambda execution role allows secretsmanager:GetSecretValue

KMS key policy or grant allows kms:Decrypt

Function code retrieves and uses the secret

Caller controls or influences that function code

That makes Lambda execution role risk a natural continuation after KMS and Secrets Manager labs.

8. Relationship to Principal LABs

Lambda execution role risk prepares learners for Principal LABs because it is a practical bridge into identity escalation.

Relevant Principal LAB connections:

iam:PassRole privilege escalation
Cross-account role escalation
Role chaining escalation

If a principal can pass a role to Lambda, update function code, or chain into a role that can manage Lambda, the workload can become an escalation surface.

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
deploy Lambda functions
invoke Lambda functions
update real function code
pass IAM roles
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
Visual Lambda Workload Identity Model exists
manifest.json exposes the lab
AWS Intermediate Identity Track links the lab
homepage renders the lab with INTERMEDIATE maturity
