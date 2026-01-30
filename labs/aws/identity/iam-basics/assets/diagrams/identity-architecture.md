# AWS IAM Identity Evaluation Flow

This diagram shows how AWS evaluates identity on **every request**, not at login.

## Flow Breakdown

1. **Human or Workload**
   - A user, EC2 instance, Lambda, or external identity initiates a request.

2. **IAM Principal**
   - The request is associated with a principal (user or assumed role).

3. **Policy Evaluation**
   - AWS evaluates all applicable identity, resource, SCP, and session policies.
   - Explicit DENY overrides everything.

4. **AWS Service**
   - If allowed, the request reaches the service (S3, EC2, RDS, etc).

## Interview Framing

Key sentence:
> “IAM is evaluated on every API call. Authentication gets you credentials; authorization happens continuously.”

This diagram is reusable across most AWS security discussions.
