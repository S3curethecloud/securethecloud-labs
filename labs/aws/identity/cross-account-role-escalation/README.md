# AWS Cross-Account Role Escalation Modeling (GOLD)

## Lab Overview

This lab demonstrates how misconfigured cross-account IAM trust policies
allow privilege escalation across AWS accounts.

The objective is to model identity reachability and understand how an
attacker can traverse trust boundaries without credential compromise.

---

## Scenario

Account A contains a privileged IAM role:

- Role: `AdminAccessRole`
- Permissions: `AdministratorAccess`

Account B has a role trusted by Account A via a permissive trust policy.

Due to insufficient conditions in the trust relationship,
an identity in Account B can assume the privileged role in Account A.

---

## Architecture Flow

Account B Principal
    ↓
AssumeRole (weak trust policy)
    ↓
Account A AdminAccessRole
    ↓
Full administrative control

---

## Why This Matters

Cross-account trust is frequently used for:

- CI/CD pipelines
- DevOps automation
- Third-party integrations

If trust policies lack:
- External ID conditions
- Source ARN restrictions
- Explicit principal limitations

Privilege escalation becomes reachable.

---

## Shield Alignment

This lab maps directly to:

- Identity graph reachability
- Cross-account attack path modeling
- Severity scoring based on blast radius

Shield would compute:

Account B Identity → Account A Admin Role → Full Access

---

## Security Takeaways

- Trust policies are part of your attack surface.
- Cross-account trust expands blast radius.
- Least privilege must apply to trust boundaries.
- Federation and AssumeRole paths must be modeled.

---

## Interview Signal

You should be able to explain:

- Difference between permission policy and trust policy.
- How AssumeRole works internally.
- How to restrict cross-account access safely.
- How Shield would detect this path deterministically.
