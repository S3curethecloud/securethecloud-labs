# SecureTheCloud LAB Platform Engineering Charter

Status: Principal LAB Build / Active

## Purpose

SecureTheCloud LABs are governed, deterministic, read-only platform engineering labs that connect:

- hands-on cloud security learning
- Shield deterministic findings
- AI Explain bounded reasoning
- governed datasets
- UI-rendered evidence paths

## Authority Model

Lab truth lives in:

`~/securethecloud-labs/labs/...`

Dataset truth lives in:

`~/stc-intelligence-core/datasets/...`

UI truth lives in:

`~/projects/stc-shield-landing/...`

## Non-Negotiables

- Labs must use stable `lab_id` values.
- Shield findings must link to labs using stable lab identifiers.
- AI Explain must cite governed datasets only.
- No web invention.
- No remediation execution.
- No mutation of customer cloud environments.
- No guessing.
- No ad-hoc URLs as identity.
- UI must render linked labs only from explicit metadata.

## LAB Maturity Levels

### Bronze

Introductory cloud security concept lab.

### Silver

Hands-on lab with deterministic expected output.

### Gold

Lab linked to a Shield finding and AI Explain dataset.

### Principal

Platform engineering lab proving the full loop:

Lab → Dataset → Shield Finding → AI Explain → UI Render → Back to Lab

## Principal LAB Requirements

Each Principal LAB must include:

- `metadata.json`
- `architecture.md`
- deterministic finding mapping
- Shield finding object
- AI Explain context
- stable lab URL
- expected outputs
- fix guidance
- governance boundary section
- no-remediation statement
- no-mutation statement

## First Principal LAB Track

Identity Attack Path Engineering:

1. `aws-cross-account-role-escalation`
2. `aws-privilege-escalation-passrole`
3. `aws-role-chaining-escalation`

## Current Build Target

Next LAB:

`aws-privilege-escalation-passrole`

Purpose:

Model deterministic AWS privilege escalation through `iam:PassRole` plus compute service creation/update capability.

## Completion Definition

The LAB platform is aligned when:

- labs are visible in the LAB website
- labs appear in `manifest.json`
- Shield findings include linked lab metadata
- `/shield/findings` returns lab-linked finding objects
- Shield UI renders “View linked lab”
- AI Explain can produce bounded hybrid explanation
