# Architecture & Trust Modeling — AWS Role Chaining Escalation

## 1. Environment Topology

We model an AWS identity path where a principal can assume one role, and that role can assume another role with broader privileges.

The modeled chain:

```text
Initial Principal
    ->
Role A
    ->
Role B
    ->
Privileged Permissions

The objective is to analyze how transitive sts:AssumeRole reachability can create deterministic privilege escalation risk.

2. Identity Flow Diagram
Low-Privilege Principal
    ->
sts:AssumeRole into IntermediateRole
    ->
sts:AssumeRole into PrivilegedRole
    ->
Expanded Permissions / Administrative Blast Radius

This is an identity-controlled role chaining path.

3. Vulnerable Trust Pattern

Role A trusts the initial principal:

{
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::111111111111:user/DeveloperUser"
  },
  "Action": "sts:AssumeRole"
}

Role B trusts Role A:

{
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::111111111111:role/IntermediateRole"
  },
  "Action": "sts:AssumeRole"
}

If Role B has elevated permissions, the initial principal may reach those permissions through the chain.

4. Why This Is Risky

Role chaining can hide escalation paths because no single policy may appear fully administrative from the initial principal's point of view.

The risk emerges from the graph relationship:

Principal can assume Role A
Role A can assume Role B
Role B has privileged permissions

If those edges exist, the privilege path exists.

5. What Shield Detects

Shield detects the deterministic relationship between:

the initial principal
an assumable intermediate role
a downstream privileged role
the transitive path that expands blast radius

Finding:

Role Chaining Escalation Path Detected

Linked finding:

shield-rolechain-001

Linked lab:

aws-role-chaining-escalation
6. Why This Is Deterministic

This finding is deterministic because it is derived from IAM trust and permission configuration:

the principal can assume Role A
Role A can assume Role B
Role B has broader privileges than the initial principal
no exploit chain is required
no runtime compromise is assumed
no external telemetry is required

If those trust and permission relationships exist, the escalation path exists.

7. Fix Guidance

Recommended controls:

minimize role-to-role trust relationships
restrict who can assume intermediate roles
prevent intermediate roles from assuming privileged roles unless explicitly required
monitor chained sts:AssumeRole paths
review transitive role reachability, not only direct access
apply permission boundaries to intermediate roles
avoid using administrative roles as downstream trust targets
8. Aegis Runtime Mapping

This lab is mapped to Aegis Runtime / Decision Intelligence.

Expected Aegis scenario:

role_chaining_escalation_path

Expected Aegis signal:

IDENTITY_DRIFT_DETECTED

Expected minimum risk modifier:

>= 20

Decision boundary:

Runtime = source of truth
OPA = decision authority
Aegis = bounded intelligence
Frontend = rendering only
9. Governance Boundary

This lab is read-only and deterministic.

It does not:

exploit AWS
mutate a customer environment
deploy live infrastructure
assume a real AWS role
execute remediation
issue tokens through Aegis
create sessions through Aegis
override OPA
treat Aegis as enforcement authority
10. Completion Criteria

This lab is complete when:

metadata.json exists and validates
architecture.md exists
runtime-mapping.json exists and validates
index.html renders an openable lab page
manifest.json exposes the lab
Intelligence Core includes shield-rolechain-001
Aegis Runtime fixture validates IDENTITY_DRIFT_DETECTED
Aegis unit test passes
Evidence record is created
