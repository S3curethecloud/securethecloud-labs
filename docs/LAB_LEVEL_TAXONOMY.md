# SecureTheCloud LAB Level Taxonomy

Status: Active / Curriculum Authority

## Purpose

SecureTheCloud Labs are organized into a level-based curriculum that supports students, interns, mentors, security engineers, and executive security leaders.

The level model prevents the platform from becoming a flat list of labs. It defines a progression from foundational understanding to intermediate reasoning, principal-level attack-path modeling, and future executive decision intelligence.

---

## LAB Levels

### L1 — Foundation LABs

Purpose:

```text
Teach core cloud security primitives, identity concepts, and policy reasoning.

Audience:

students
interns
new cloud security engineers
interview preparation

Characteristics:

concept-first
beginner-safe
read-only
no live mutation
no exploitation
no runtime dependency required
teaches vocabulary and mental models

Examples:

aws-iam-basics
azure-entra-id-basics
gcp-iam-basics
L2 — Intermediate LABs

Purpose:

Teach realistic cloud misconfiguration reasoning and deterministic evaluation paths.

Audience:

students moving beyond basics
interns entering real-world cloud security
security engineers building evidence reasoning
mentors teaching practical cloud security

Characteristics:

scenario-driven
deterministic reasoning
cloud control-plane focused
explains effective permissions
introduces evidence mapping
may be Shield-aligned
may be Aegis Runtime-eligible
does not require live exploitation

Examples:

aws-iam-policy-evaluation
aws-permission-boundary-basics
aws-s3-public-access-risk
aws-kms-key-policy-risk
aws-security-group-exposure
L3 — Principal LABs

Purpose:

Model advanced deterministic identity and attack-path scenarios with evidence linkage.

Audience:

senior engineers
principal engineers
security architects
platform security teams
CSO/CISO technical review

Characteristics:

advanced attack-path modeling
Shield deterministic finding linkage
Aegis Runtime mapping
OPA authority boundary
evidence record required
executive-readable explanation
no customer mutation
no live exploitation

Current Principal AWS Identity LABs:

aws-cross-account-role-escalation
aws-privilege-escalation-passrole
aws-role-chaining-escalation
L4 — Executive LABs

Purpose:

Translate technical cloud security paths into executive risk, blast-radius, governance, and decision intelligence.

Audience:

CSO
CISO
security leadership
audit stakeholders
board-level risk review
enterprise platform buyers

Characteristics:

risk narrative
governance posture
audit evidence
blast-radius explanation
decision summary
no tactical exploitation
grounded in L2/L3 evidence

Future examples:

executive-aws-identity-risk-brief
executive-cloud-identity-blast-radius-review
executive-zero-trust-runtime-decision-review
executive-audit-evidence-package-walkthrough
Curriculum Progression

Recommended AWS Identity progression:

L1: AWS IAM Basics
    ↓
L2: AWS IAM Policy Evaluation
    ↓
L3: AWS Principal Identity Track
    ↓
L4: Executive AWS Identity Risk Brief
Governance Boundary

All LAB levels remain read-only unless explicitly approved in a future controlled runtime phase.

The LAB platform does not:

exploit cloud environments
mutate customer infrastructure
deploy live infrastructure by default
execute remediation
issue runtime tokens through LAB content
override OPA
treat Aegis as enforcement authority
infer compromise from static learning artifacts

Authority model:

Runtime = source of truth
OPA = decision authority
Aegis = bounded intelligence
Frontend = rendering only
Current Strategy

Next build priority:

L2 Intermediate LABs

Reason:

The platform already has L1 foundation coverage and L3 Principal AWS identity coverage.
L2 now bridges beginner learning into deterministic security engineering reasoning.

First L2 LAB:

aws-iam-policy-evaluation


---

## AWS Principal Track Curriculum Linkage

The AWS Principal Identity Track is linked to the learning ladder:

```text
L1: AWS IAM Basics
    ↓
L2: AWS IAM Policy Evaluation
    ↓
L3: AWS Principal Identity Track

This linkage ensures that learners can progress from foundational IAM concepts into effective-permission reasoning before attempting Principal LABs such as:

cross-account role escalation
iam:PassRole privilege escalation
role chaining escalation

This curriculum linkage is educational and read-only.

No runtime, Shield, Aegis, or OPA logic changes are introduced by this linkage.

---

## AWS Intermediate Identity Track

The AWS Intermediate Identity Track is the L2 learning lane between AWS IAM Basics and the AWS Principal Identity Track.

Track path:

```text
/tracks/aws-intermediate-identity/

Current active L2 LAB:

aws-iam-policy-evaluation

Planned next L2 LABs:

aws-permission-boundary-basics
aws-scp-guardrail-reasoning
aws-resource-policy-evaluation
aws-s3-public-access-risk

Curriculum purpose:

Teach effective-permission reasoning before learners enter Principal LABs.

This track is read-only and educational.

No runtime, Shield, Aegis, or OPA logic changes are introduced by this track page.

---

## AWS Permission Boundary Basics L2 LAB

The AWS Permission Boundary Basics LAB has been added to the AWS Intermediate Identity Track.

LAB path:

```text
/labs/aws/identity/permission-boundary-basics/

LAB ID:

aws-permission-boundary-basics

Curriculum role:

L2 intermediate identity-policy reasoning

Purpose:

Teach how permission boundaries constrain maximum principal authority without granting access by themselves.

Runtime / Shield / Aegis boundary:

Runtime change required: false
Shield finding required: false
Aegis fixture required: false
OPA authority preserved: true


---

## AWS SCP Guardrail Reasoning L2 LAB

The AWS SCP Guardrail Reasoning LAB has been added to the AWS Intermediate Identity Track.

LAB path:

```text
/labs/aws/identity/scp-guardrail-reasoning/

LAB ID:

aws-scp-guardrail-reasoning

Curriculum role:

L2 intermediate organization-guardrail reasoning

Purpose:

Teach how AWS Service Control Policies define organization-level maximum permissions without granting access by themselves.

Runtime / Shield / Aegis boundary:

Runtime change required: false
Shield finding required: false
Aegis fixture required: false
OPA authority preserved: true


---

## AWS Resource Policy Evaluation L2 LAB

The AWS Resource Policy Evaluation LAB has been added to the AWS Intermediate Identity Track.

LAB path:

```text
/labs/aws/identity/resource-policy-evaluation/

LAB ID:

aws-resource-policy-evaluation

Curriculum role:

L2 intermediate resource-side authorization reasoning

Purpose:

Teach how AWS resource-based policies participate in authorization decisions alongside identity policies, boundaries, SCPs, and explicit deny.

Runtime / Shield / Aegis boundary:

Runtime change required: false
Shield finding required: false
Aegis fixture required: false
OPA authority preserved: true


---

## AWS S3 Public Access Risk L2 LAB

The AWS S3 Public Access Risk LAB has been added to the AWS Intermediate Identity Track as the first applied L2 risk lab after the four-part authorization model.

LAB path:

```text
/labs/aws/storage/s3-public-access-risk/

LAB ID:

aws-s3-public-access-risk

Curriculum role:

L2 applied storage exposure and authorization-risk reasoning

Purpose:

Teach how S3 public access risk emerges from bucket policy, Block Public Access settings, ACL history, identity permissions, resource policies, and organization guardrails.

Runtime / Shield / Aegis boundary:

Runtime change required: false
Shield finding required: false
Aegis fixture required: false
OPA authority preserved: true


---

## AWS KMS Key Policy Evaluation L2 LAB

The AWS KMS Key Policy Evaluation LAB has been added to the AWS Intermediate Identity Track as a high-value data-protection and cryptographic authorization LAB.

LAB path:

```text
/labs/aws/security/kms-key-policy-evaluation/

LAB ID:

aws-kms-key-policy-evaluation

Curriculum role:

L2 cryptographic authorization and key-policy reasoning

Purpose:

Teach how AWS KMS key policies, IAM permissions, grants, encryption context, and organization guardrails combine to control cryptographic access.

Runtime / Shield / Aegis boundary:

Runtime change required: false
Shield finding required: false
Aegis fixture required: false
OPA authority preserved: true


---

## AWS L2 Authorization Model Executive Study Guide

The AWS L2 Authorization Model guide packages the intermediate AWS authorization curriculum into a mentor, student, and executive-facing learning artifact.

Guide path:

```text
/guides/aws-l2-authorization-model/

Covered L2 LABs:

AWS IAM Policy Evaluation
AWS Permission Boundary Basics
AWS SCP Guardrail Reasoning
AWS Resource Policy Evaluation
AWS S3 Public Access Risk
AWS KMS Key Policy Evaluation

Curriculum role:

L2 executive study guide and authorization model summary

Purpose:

Summarize identity-side authorization, principal ceilings, organization guardrails, resource-side authorization, applied public exposure risk, and cryptographic access control.

Runtime / Shield / Aegis boundary:

Runtime change required: false
Shield finding required: false
Aegis fixture required: false
OPA authority preserved: true


---

## AWS Secrets Manager Access Evaluation L2 LAB

The AWS Secrets Manager Access Evaluation LAB has been added to the AWS Intermediate Identity Track as a data-protection and secret-access authorization LAB.

LAB path:

```text
/labs/aws/security/secrets-manager-access-evaluation/

LAB ID:

aws-secrets-manager-access-evaluation

Curriculum role:

L2 secret-access authorization and data-protection reasoning

Purpose:

Teach how AWS Secrets Manager access depends on IAM permissions, resource policies, KMS decrypt authority, explicit deny, and organization guardrails.

Runtime / Shield / Aegis boundary:

Runtime change required: false
Shield finding required: false
Aegis fixture required: false
OPA authority preserved: true


---

## AWS Lambda Execution Role Risk L2 LAB

The AWS Lambda Execution Role Risk LAB has been added to the AWS Intermediate Identity Track as a workload identity and serverless authorization-risk LAB.

LAB path:

```text
/labs/aws/compute/lambda-execution-role-risk/

LAB ID:

aws-lambda-execution-role-risk

Curriculum role:

L2 workload identity and serverless execution-role risk reasoning

Purpose:

Teach how Lambda execution roles create workload identity risk when function update authority, iam:PassRole, Secrets Manager access, KMS decrypt, and resource permissions combine.

Runtime / Shield / Aegis boundary:

Runtime change required: false
Shield finding required: false
Aegis fixture required: false
OPA authority preserved: true


---

## AWS CloudTrail Detection Reasoning L2 LAB

The AWS CloudTrail Detection Reasoning LAB has been added to the AWS Intermediate Identity Track as the first detection-reasoning LAB.

LAB path:

```text
/labs/aws/detection/cloudtrail-detection-reasoning/

LAB ID:

aws-cloudtrail-detection-reasoning

Curriculum role:

L2 detection reasoning and CloudTrail evidence analysis

Purpose:

Teach how CloudTrail evidence supports detection reasoning for iam:PassRole, sts:AssumeRole, Lambda updates, Secrets Manager access, KMS decrypt, and workload identity activity.

Runtime / Shield / Aegis boundary:

Runtime change required: false
Shield finding required: false
Aegis fixture required: false
OPA authority preserved: true

## AI Governance Command Center Track

```text
Track: AI Governance Command Center
Level: Intermediate / Executive Learning Path
Purpose: Teach enterprise AI governance command center design using intake, risk tiering, policy gates, human approval, agent workflow governance, observability, support handoff, and executive demo boundaries.
Runtime: Read-only learning course.
Backend exposure: false.
Production enforcement claim: false.

## AI Agent Tool-Use Risk L2 LAB

```text
Lab: AI Agent Tool-Use Risk
Track: AI Governance Command Center
Level: Intermediate / L2
Purpose: Teach how AI agent tool-use becomes enterprise risk when tool permissions, API action boundaries, human approval gates, and autonomous execution controls are not governed.
Runtime: Read-only learning course.
Backend exposure: false.
Live tool execution: false.
Production enforcement claim: false.

## Prompt Injection and Tool Hijacking L2 LAB

```text
Lab: Prompt Injection and Tool Hijacking
Track: AI Governance Command Center
Level: Intermediate / L2
Purpose: Teach how prompt injection can manipulate AI agent instructions, tool selection, policy bypass attempts, and approval-gated execution paths.
Runtime: Read-only learning course.
Backend exposure: false.
Live tool execution: false.
Production enforcement claim: false.

## RAG Data Boundary and Retrieval Risk L2 LAB

```text
Lab: RAG Data Boundary and Retrieval Risk
Track: AI Governance Command Center
Level: Intermediate / L2
Purpose: Teach how RAG and retrieval systems create AI governance risk when trusted, untrusted, sensitive, stale, or poisoned context is retrieved and treated as authority.
Runtime: Read-only learning course.
Backend exposure: false.
Live retrieval execution: false.
Enterprise data access: false.
Production enforcement claim: false.

## Human Approval Gate Design L2 LAB

```text
Lab: Human Approval Gate Design
Track: AI Governance Command Center
Level: Intermediate / L2
Purpose: Teach how human approval gates prevent AI agents, tool-use, prompt injection, and retrieval risk from becoming ungoverned enterprise execution.
Runtime: Read-only learning course.
Backend exposure: false.
Live approval execution: false.
Enterprise API mutation: false.
Production enforcement claim: false.

## AI Audit Evidence and Traceability L2 LAB

```text
Lab: AI Audit Evidence and Traceability
Track: AI Governance Command Center
Level: Intermediate / L2
Purpose: Teach how to build audit-ready evidence trails for AI decisions, prompts, retrieved context, tool attempts, policy decisions, human approvals, blocked actions, and executive summaries.
Runtime: Read-only learning course.
Backend exposure: false.
Live audit pipeline: false.
Enterprise evidence access: false.
Production enforcement claim: false.

## AI Cost, Token, and Rate Limit Governance L2 LAB

```text
Lab: AI Cost, Token, and Rate Limit Governance
Track: AI Governance Command Center
Level: Intermediate / L2
Purpose: Teach how to govern AI cost, token usage, runaway agent loops, repeated tool attempts, expensive retrieval calls, rate limits, budget thresholds, and operational evidence.
Runtime: Read-only learning course.
Backend exposure: false.
Live billing integration: false.
Live rate-limit enforcement: false.
Provider quota mutation: false.
Production enforcement claim: false.

## AI Security Engineering Overview L2 LAB

```text
Lab: AI Security Engineering Overview
Track: AI Security Engineering
Level: Intermediate / L2
Purpose: Introduce secure AI system engineering, AI threat surfaces, prompt/model/retrieval/tool/policy/evidence boundaries, and the relationship between AI governance and AI security engineering.
Runtime: Read-only learning course.
Backend exposure: false.
Live model integration: false.
Live tool execution: false.
Live retrieval execution: false.
Provider quota mutation: false.
Production enforcement claim: false.

## Secure AI Application Architecture L2 LAB

```text
Lab: Secure AI Application Architecture
Track: AI Security Engineering
Level: Intermediate / L2
Purpose: Teach secure AI application architecture patterns across frontend, backend/API, model, retrieval, tool, policy, approval, evidence, observability, and runtime boundaries.
Runtime: Read-only learning course.
Backend exposure: false.
Live model integration: false.
Live tool execution: false.
Live retrieval execution: false.
Provider quota mutation: false.
Production enforcement claim: false.

## Prompt Boundary Engineering L2 LAB

```text
Lab: Prompt Boundary Engineering
Track: AI Security Engineering
Level: Intermediate / L2
Purpose: Teach prompt boundary engineering by separating trusted instructions from untrusted user input, retrieved content, tool output, and model-generated recommendations.
Runtime: Read-only learning course.
Backend exposure: false.
Live model integration: false.
Live tool execution: false.
Live retrieval execution: false.
Provider quota mutation: false.
Production enforcement claim: false.

## Tool Permission Engineering L2 LAB

```text
Lab: Tool Permission Engineering
Track: AI Security Engineering
Level: Intermediate / L2
Purpose: Teach scoped AI tool permissions, action classification, read-only vs mutating tool boundaries, approval gates, self-approval prevention, and evidence capture.
Runtime: Read-only learning course.
Backend exposure: false.
Live model integration: false.
Live tool execution: false.
Live retrieval execution: false.
Provider quota mutation: false.
Production enforcement claim: false.

## Retrieval Security Engineering L2 LAB

```text
Lab: Retrieval Security Engineering
Track: AI Security Engineering
Level: Intermediate / L2
Purpose: Teach secure retrieval engineering for AI systems, including source authority, tenant scope, sensitivity, freshness, retrieval poisoning resistance, context packaging, and evidence capture.
Runtime: Read-only learning course.
Backend exposure: false.
Live model integration: false.
Live tool execution: false.
Live retrieval execution: false.
Vector database access: false.
Enterprise data access: false.
Provider quota mutation: false.
Production enforcement claim: false.

## Output Safety and Response Policy Engineering L2 LAB

```text
Lab: Output Safety and Response Policy Engineering
Track: AI Security Engineering
Level: Intermediate / L2
Purpose: Teach AI output safety and response policy engineering, including response classification, sensitive data handling, grounded answers, refusal behavior, escalation, unsafe-response prevention, and evidence capture.
Runtime: Read-only learning course.
Backend exposure: false.
Live model integration: false.
Live tool execution: false.
Live retrieval execution: false.
Vector database access: false.
Enterprise data access: false.
Provider quota mutation: false.
Production enforcement claim: false.

## AI Runtime Guardrails and Failure Mode Engineering L2 LAB

```text
Lab: AI Runtime Guardrails and Failure Mode Engineering
Track: AI Security Engineering
Level: Intermediate / L2
Purpose: Teach AI runtime guardrails and failure mode engineering, including loop control, retries, timeouts, deny paths, fail-closed behavior, circuit breakers, degradation, escalation, and evidence capture.
Runtime: Read-only learning course.
Backend exposure: false.
Live model integration: false.
Live tool execution: false.
Live retrieval execution: false.
Vector database access: false.
Enterprise data access: false.
Provider quota mutation: false.
Production enforcement claim: false.

## AI Abuse, Cost, and Rate Limit Engineering L2 LAB

```text
Lab: AI Abuse, Cost, and Rate Limit Engineering
Track: AI Security Engineering
Level: Intermediate / L2
Purpose: Teach AI abuse, cost, and rate limit engineering, including token budgets, quota controls, repeated attempts, expensive retrieval/tool paths, throttling, denial, and evidence capture.
Runtime: Read-only learning course.
Backend exposure: false.
Live billing integration: false.
Live rate-limit enforcement: false.
Live model integration: false.
Live tool execution: false.
Live retrieval execution: false.
Vector database access: false.
Enterprise data access: false.
Provider quota mutation: false.
Production enforcement claim: false.

## AI Security Testing and Evidence Harness L2 LAB

```text
Lab: AI Security Testing and Evidence Harness
Track: AI Security Engineering
Level: Intermediate / L2
Purpose: Teach AI security testing and evidence harness design, including prompt boundary tests, tool permission tests, retrieval tests, output safety checks, runtime guardrail tests, abuse/cost tests, expected outcomes, and audit-ready evidence packages.
Runtime: Read-only learning course.
Backend exposure: false.
Live model integration: false.
Live tool execution: false.
Live retrieval execution: false.
Vector database access: false.
Enterprise data access: false.
Provider quota mutation: false.
Production enforcement claim: false.

## Cloud Security Operations Overview L2 LAB

```text
Lab: Cloud Security Operations Overview
Track: Cloud Security Operations
Level: Intermediate / L2
Purpose: Introduce cloud security operations fundamentals including detection, triage, event context, evidence collection, escalation, incident narrative, and safe production boundary language.
Runtime: Read-only learning course.
Backend exposure: false.
Cloud provider integration: false.
SIEM integration: false.
Ticketing integration: false.
Alert pipeline: false.
Customer data access: false.
Live detector execution: false.
Runtime mutation: false.
Production enforcement claim: false.

## Cloud Event and Signal Classification L2 LAB

```text
Lab: Cloud Event and Signal Classification
Track: Cloud Security Operations
Level: Intermediate / L2
Purpose: Teach cloud event and signal classification by source, actor, asset, action, severity, confidence, tenant context, and evidence quality.
Runtime: Read-only learning course.
Backend exposure: false.
Cloud provider integration: false.
SIEM integration: false.
Ticketing integration: false.
Alert pipeline: false.
Customer data access: false.
Live detector execution: false.
Runtime mutation: false.
Production enforcement claim: false.

## IAM Activity Triage L2 LAB

```text
Lab: IAM Activity Triage
Track: Cloud Security Operations
Level: Intermediate / L2
Purpose: Teach IAM activity triage including role assumption, privilege changes, access key activity, policy edits, failed access, suspicious identity behavior, evidence quality, escalation, and safe response narratives.
Runtime: Read-only learning course.
Backend exposure: false.
Cloud provider integration: false.
SIEM integration: false.
Ticketing integration: false.
Alert pipeline: false.
Customer data access: false.
Live detector execution: false.
IAM mutation: false.
Cloud provider mutation: false.
Runtime mutation: false.
Production enforcement claim: false.

