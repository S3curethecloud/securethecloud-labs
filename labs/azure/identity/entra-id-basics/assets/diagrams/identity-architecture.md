# Azure Entra ID Identity Evaluation Flow

This diagram illustrates how Azure evaluates identity through token issuance
and Conditional Access before a request reaches Azure Resource Manager (ARM).

## Flow Breakdown

1. **Human or Workload**
   - User, application, or automation initiates sign-in.

2. **Entra ID Principal**
   - User or Service Principal authenticates.

3. **Token Issuance & Conditional Access**
   - Authentication occurs.
   - Conditional Access policies are evaluated.
   - Tokens are issued with claims.

4. **Azure Resource (ARM)**
   - ARM authorizes the request using RBAC.

## Interview Framing

Key sentence:
> “In Azure, access decisions start at authentication with Conditional Access,
then continue at authorization with RBAC.”
