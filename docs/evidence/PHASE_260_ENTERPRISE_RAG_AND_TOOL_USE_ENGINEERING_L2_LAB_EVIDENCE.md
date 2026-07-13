# Phase 260 — Enterprise RAG and Tool-Use Engineering L2 LAB Evidence

Status: Evidence Recorded

## Phase Scope

This phase records production evidence for Phase 259 — Add Enterprise RAG and Tool-Use Engineering L2 LAB.

This phase is evidence-only.

No homepage content was changed in this phase.
No manifest content was changed in this phase.
No track content was changed in this phase.
No LAB content was changed in this phase.
No module metadata was changed in this phase.
No architecture content was changed in this phase.
No new learning module was added in this phase.
No backend was exposed.
No foundation model was called.
No agent runtime was started.
No document was ingested.
No embedding was generated.
No vector database was queried or mutated.
No RAG retrieval was executed.
No enterprise source was accessed.
No cross-tenant retrieval was performed.
No live tool or function call was enabled.
No API call execution was enabled.
No ticket was created.
No approval was executed.
No memory was persisted.
No MCP server or client was started.
No enterprise gateway integration was enabled.
No persistent registry mutation was performed.
No OPA policy was executed.
No Responsible AI evaluation was executed.
No OpenTelemetry data was exported.
No cloud resource was deployed.
No credential or secret handling was introduced.
No customer data access was introduced.
No runtime mutation was performed.
No production enforcement was claimed.

## Source Commits and Pull Request

```text
Phase 258 evidence commit: e6ec397
Phase 259 feature branch integration head: e3062b8
Phase 259 pull request: #3
Phase 259 main merge commit: 6d8465082d8a96823fa849050dc841f517b066b8
QA source head: 6d8465082d8a96823fa849050dc841f517b066b8
```

## Evidence Date

```text
Production verification date: 2026-07-12
Production host: https://labs.securethecloud.dev
```

## Production Homepage State

The Phase 259 homepage state was verified with the Enterprise Agent Developer track remaining active.

```text
LAB modules = 66
Learning paths = 6
Total AI modules = 42
Complete learning paths = 5
Backend exposure = 0
```

The homepage includes the Module 3 searchable catalog record:

```text
Enterprise RAG and Tool-Use Engineering
Track: enterprise-agent-developer
Path: /labs/enterprise-agent-developer/enterprise-rag-tool-use-engineering/
Level: L2
```

The Enterprise Agent Developer active-track preview records:

```text
Status = active track
Implemented modules = 3 of 9
Full track complete = false
No live agent execution = true
No live model execution = true
No live retrieval execution = true
No live tool execution = true
No live gateway execution = true
No live MCP execution = true
No live policy execution = true
No live telemetry export = true
No cloud execution = true
```

## Production Manifest Verification

The production manifest was valid JSON.

The Module 3 LAB record was verified:

```text
id: enterprise-rag-tool-use-engineering
title: Enterprise RAG and Tool-Use Engineering
cloud: enterprise-agent-developer
domain: Enterprise Agentic AI
track: enterprise-agent-developer
level: L2
status: implemented
path: /labs/enterprise-agent-developer/enterprise-rag-tool-use-engineering/
backend_exposure: false
```

The Enterprise Agent Developer track record was verified:

```text
id: enterprise-agent-developer
title: Enterprise Agent Developer L2 Track
cloud: enterprise-agent-developer
domain: Enterprise Agentic AI
level: L2
path: /tracks/enterprise-agent-developer/
status: active
implemented_modules: 3
planned_modules: 9
backend_exposure: false
production_enforcement_claim: false
```

The existing completed-track records with `implemented_modules: 9` and `planned_modules: 9` remain separate from this active track record.

## Production Track Route

Production route verified:

```text
Route: /tracks/enterprise-agent-developer/
HTTP status: 200
Title: Enterprise Agent Developer L2 Track
Status: Active Track
Modules: 3 of 9
Runtime: Read-only course
```

The production track shell contains all three implemented module links:

```text
1. Enterprise Agent Developer Role Architecture
/labs/enterprise-agent-developer/enterprise-agent-developer-role-architecture/

2. Task-Oriented and Conversational Agent Design
/labs/enterprise-agent-developer/task-oriented-conversational-agent-design/

3. Enterprise RAG and Tool-Use Engineering
/labs/enterprise-agent-developer/enterprise-rag-tool-use-engineering/
```

The track shell preserves the remaining six modules as planned rather than implemented.

## Production Track Governance Boundary

The production track shell governance boundary was verified:

```text
Track implemented = true
LAB modules implemented = 3 of 9
Runtime = read-only learning
Backend exposure = false
Public backend exposed = false
Live LLM inference = false
Agent runtime execution = false
RAG retrieval execution = false
Live tool invocation = false
MCP server execution = false
MCP client execution = false
Gateway integration = false
Persistent registry mutation = false
OPA policy execution = false
OpenTelemetry export = false
Cloud deployment = false
Credential handling = false
Customer data access = false
Runtime mutation = false
Production enforcement claim = false
```

## Production Module 3 Route

Production route verified:

```text
Route: /labs/enterprise-agent-developer/enterprise-rag-tool-use-engineering/
HTTP status: 200
Title: Enterprise RAG and Tool-Use Engineering
Domain: Enterprise Agentic AI
Track: Enterprise Agent Developer
Runtime: Read-only course
```

## Production Module 3 Layout

The production Module 3 LAB uses the shared Cloud Ops LAB presentation system.

Required layout and content markers verified:

```text
/assets/css/labs.css
lab-detail-shell
lab-status-grid
mobile-study-menu
lab-detail-layout
lab-side-nav
lab-main-panels
lab-panel
Concept Deep Dives
Visual Enterprise RAG and Tool-Use Model
Example Scenario
LAB Exercise
High-Risk Anti-Pattern
Governance Boundary
```

The LAB does not introduce a separate presentation framework.

## Module 3 Learning Architecture

The LAB defines enterprise RAG as a controlled evidence pipeline rather than vector search attached to a prompt.

The governing mental model is:

```text
Authoritative retrieval
Bounded context
Controlled action
```

The architecture note records the broader governed flow:

```text
Trusted source
Controlled retrieval
Validated context
Bounded tool authority
Observable outcome
```

The production LAB establishes the following operational separation:

```text
Authoritative sources
Controlled retrieval
Bounded context
Tool policy boundary
Grounded or safe outcome
```

The LAB teaches that retrieval supplies evidence rather than authority. A model may propose an action, while identity, authorization, policy, approval, schema validation, idempotency, and execution ownership remain deterministic controls outside model judgment.

## Source Authority Evidence

The production LAB requires every candidate source to define:

```text
Accountable owner
Business purpose
System-of-record or authority status
Data classification
Tenant and jurisdiction
Publication process
Freshness expectation
Effective date and version
Access policy
Retention rule
Lifecycle and deprecation status
```

The LAB rejects the assumption that every available document is equally trusted or eligible for ingestion.

## Ingestion, Chunking, and Metadata Evidence

The production LAB teaches that ingestion design must preserve:

```text
Document identity
Document version
Source owner
Publication and update timestamps
Classification
Tenant
Permissions
Region or residency
Lineage
Parent-document reference
Retention and legal-hold state
```

Chunking must follow semantic and structural boundaries and must be evaluated against retrieval quality rather than selected by habit.

## Authorization and Retrieval Filtering Evidence

The production LAB requires identity-aware and tenant-aware filtering before evidence reaches a model.

Example controls include:

```text
Document classification
Tenant
Business unit
Role
Region
Effective date
Product
Language
Legal hold
Source status
```

Similarity score is explicitly not treated as an authorization decision.

## Retrieval and Context Assembly Evidence

The LAB covers:

```text
Lexical retrieval
Vector retrieval
Hybrid retrieval
Query rewriting
Reranking
Context deduplication
Authority and freshness prioritization
Token-budget enforcement
Source labeling
Instruction-data separation
Minimum-necessary context
Abstention when authoritative evidence is absent
```

Retrieved content is treated as untrusted data and cannot override system instructions or grant execution authority.

## Citation and Provenance Evidence

The production LAB requires material claims to remain traceable to:

```text
Source identifier
Document version
Chunk identifier
Retrieval timestamp
Retrieval query or intent
Authority and freshness status
Final citation used in the response
```

Provenance must survive reranking and context compression so evidence selection can be reproduced and investigated.

## Tool-Use Engineering Evidence

Each proposed tool requires:

```text
Narrow business purpose
Accountable owner
Explicit JSON Schema
Dedicated caller identity
Least-privilege permissions
Data classification
Deterministic input validation
Policy decision
Approval requirement
Timeout
Retry rule
Rate limit
Idempotency behavior
Error contract
Dry-run or no-write mode
Human handoff path
Audit evidence
Final disposition
```

Tool descriptions and model confidence do not grant authority.

## Prompt-Injection and Abuse-Control Evidence

The production LAB identifies the following controls:

```text
Approved-source allowlist
Pre-retrieval authorization
Tenant and region filters
Prompt-injection isolation
Untrusted-content treatment
Content scanning
Context-instruction separation
Tool allowlist
Schema validation
Deterministic policy checks
Human approval for sensitive actions
No-write defaults
Duplicate-action detection
Circuit breakers
Trace correlation
```

## Evaluation Evidence

The LAB requires evaluation across retrieval, answer, tool, operational, and safety dimensions.

Example measures include:

```text
Recall at k
Precision at k
Mean reciprocal rank
Normalized discounted cumulative gain
Answer faithfulness
Citation correctness
Unauthorized-evidence exclusion
Stale-evidence exclusion
Refusal accuracy
Tool-schema validity
Approval-path correctness
Duplicate-action prevention
Latency
Token use
Cost
Trace completeness
```

Evaluation must include normal, edge, and adversarial cases with reproducible expected outcomes.

## LAB Exercise Evidence

The production LAB exercise requires a design package containing:

```text
1. Authoritative source inventory and ownership matrix
2. Data classification, tenant, region, and access model
3. Ingestion, parsing, chunking, and versioning specification
4. Metadata schema and pre-retrieval authorization filters
5. Vector, keyword, or hybrid retrieval decision
6. Reranking and context-selection policy
7. Retrieval evaluation dataset and quality metrics
8. Prompt-injection and untrusted-content control design
9. Context token budget and deduplication rules
10. Citation, provenance, and source-version contract
11. Tool inventory and least-privilege permission matrix
12. JSON Schema for each proposed tool request
13. Approval, idempotency, timeout, retry, and rate-limit rules
14. No-evidence, no-authorization, and no-write fallback paths
15. Trace, audit, residual-risk, and governance-boundary statement
```

Acceptance evidence includes:

```text
Every indexed source has an owner, authority status, classification, and freshness rule
Retrieval filters enforce identity, tenant, region, and data-policy boundaries
Retrieved text is treated as untrusted data rather than instruction
Retrieval quality is evaluated with reproducible test cases
Material claims preserve citation and provenance
Tools use narrow schemas and dedicated least-privilege identities
Model output cannot authorize or directly execute a write
Insufficient evidence or authority results in clarification, refusal, or handoff
The learner can explain RAG and tool-use tradeoffs in client-ready language
```

## High-Risk Anti-Pattern Evidence

The LAB identifies the following unsafe design pattern:

```text
No source owner or system-of-record designation
No classification, tenant, or region filters
Stale and superseded documents remain searchable
Chunking selected without evaluation
Retrieved content can override system instructions
Similarity score treated as access control
No citation or source-version evidence
Broad tool identity and permissive parameters
Free-form model text becomes an API request
Retries can duplicate irreversible actions
No approval, idempotency, or no-write fallback
No trace joining retrieval evidence to tool decisions
```

The safe alternative requires registered authoritative sources, access control before retrieval, preserved lineage and versions, evaluated retrieval quality, instruction-data separation, narrow tool schemas, least privilege, deterministic policy and approval, idempotency, rate limits, no-write defaults, and complete trace evidence.

## Production Module 3 Governance Boundaries

The production Module 3 governance boundary was verified:

```text
Runtime = read-only learning
Backend exposure = false
Public backend exposed = false
Live LLM inference = false
Agent runtime execution = false
Document ingestion execution = false
Embedding generation = false
Vector database execution = false
Vector index mutation = false
RAG retrieval execution = false
Enterprise source access = false
Cross-tenant retrieval = false
Live tool invocation = false
Live function calling = false
Live API call execution = false
System-of-record mutation = false
Ticket creation execution = false
Approval execution = false
Memory persistence = false
MCP server execution = false
MCP client execution = false
Gateway integration = false
Persistent registry mutation = false
OPA policy execution = false
Responsible AI evaluation execution = false
OpenTelemetry export = false
Cloud deployment = false
Customer data access = false
Credential handling = false
Secret handling = false
Runtime mutation = false
Production enforcement claim = false
```

## Metadata Boundary Verification

The Module 3 metadata record was verified as read-only and implemented.

```text
id = enterprise-rag-tool-use-engineering
status = implemented
runtime = read-only
backend_exposure = false
live_llm_inference = false
agent_runtime_execution = false
rag_retrieval_execution = false
live_tool_invocation = false
live_api_call_execution = false
mcp_server_execution = false
mcp_client_execution = false
gateway_integration = false
persistent_registry_mutation = false
opa_policy_execution = false
responsible_ai_evaluation_execution = false
opentelemetry_export = false
cloud_deployment = false
credential_handling = false
customer_data_access = false
runtime_mutation = false
production_enforcement_claim = false
```

## Old Class and Inline-Style Regression Check

The Module 3 LAB was checked for old or prohibited presentation patterns:

```text
lab-shell = absent
lab-toc = absent
comparison-grid = absent
boundary-table = absent
badge-false = absent
inline style block = absent
```

The page uses `/assets/css/labs.css` and the canonical Cloud Ops LAB classes.

## Active Track State

```text
Track status = active
Implemented modules = 3
Planned modules = 9
Locked LAB modules = 3
Remaining planned modules = 6
Full track complete = false
Backend exposure = false
Live model execution = false
Live agent execution = false
Document ingestion execution = false
RAG retrieval execution = false
Vector index mutation = false
Live tool execution = false
System-of-record mutation = false
Live gateway integration = false
Runtime mutation = false
Production enforcement claim = false
```

The Enterprise RAG and Tool-Use Engineering L2 LAB is complete and production-verified.

The Enterprise Agent Developer L2 Track is not complete. It remains active at 3 of 9 modules.

## Phase 260 Change Boundary

```text
Homepage changed in this phase = false
Manifest changed in this phase = false
Track changed in this phase = false
LAB changed in this phase = false
Metadata changed in this phase = false
Architecture note changed in this phase = false
New learning module added in this phase = false
Backend exposure changed in this phase = false
Production enforcement changed in this phase = false
```

## Lock Statement

Phase 260 records evidence only. Enterprise RAG and Tool-Use Engineering L2 LAB is production-verified and locked. The Enterprise Agent Developer L2 Track remains active at 3 of 9 modules and is not a complete learning path.
