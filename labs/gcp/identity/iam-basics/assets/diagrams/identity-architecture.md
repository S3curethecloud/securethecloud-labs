# GCP IAM Identity Evaluation Flow

This diagram shows how Google Cloud evaluates identity and access
using IAM policy bindings on every request.

## Flow Breakdown

1. **Human or Workload**
   - User or workload initiates a request.

2. **Principal**
   - User identity or service account is identified.

3. **IAM Policy Bindings**
   - Roles are evaluated against the requested resource.

4. **Google Cloud Service**
   - If allowed, the request reaches the service.

## Interview Framing

Key sentence:
> “GCP IAM relies on role bindings evaluated at request time,
with service accounts as the primary workload identity.”
