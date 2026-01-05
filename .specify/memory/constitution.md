# CONSTITUTION.md
# 5-Phase Spec-Driven AI Hackathon Project Constitution

## 1. Purpose & Philosophy

**Spec-Driven Development Mandate**: All development must follow the Spec-Kit Plus lifecycle (Specify → Plan → Tasks → Implement). Code is not the primary artifact; specifications, plans, and tasks are the authoritative source of truth for all implementations.

**AI Agents as Digital FTEs**: AI agents are treated as full-time engineering resources with defined roles, responsibilities, and constraints. They must follow the same governance and compliance rules as human engineers.

**Predictability Over Innovation**: The primary goal is predictable, repeatable, and compliant development processes rather than creative or experimental approaches.

## 2. Non-Negotiable Principles

**No Code Without Approved Specs**: No implementation work is permitted without approved specifications in the `.specify/` directory. All code must directly reference approved spec, plan, and task documents.

**Architecture Changes Require Plan Updates**: Any architectural modifications must first be documented in updated plan files before implementation. No ad-hoc architectural changes are allowed.

**Event-First, Async-First Mindset**: All system interactions must be designed as asynchronous, event-driven communications. Direct service coupling is forbidden without Kafka or Dapr Pub/Sub abstraction.

**No Direct Service Coupling**: All microservices must communicate through Kafka (via Dapr Pub/Sub abstraction) rather than direct API calls. Hardcoded service discovery or direct HTTP calls between services are prohibited.

## 3. Agent Rules (MANDATORY)

**No Code Generation Without Task ID**: AI agents must never generate code without a specific Task ID referencing an approved task in the `.specify/tasks/` directory. All implementations must be traceable to specific, approved tasks.

**Request Clarification When Specs Are Missing**: When specifications, plans, or tasks are incomplete or missing, agents must stop immediately and request clarification from human operators. No assumptions are permitted.

**No Assumption of Requirements**: Agents must never "assume" requirements or infer missing specifications. All requirements must be explicitly defined in spec documents.

**Reference Spec + Plan in Every Implementation**: Every code implementation must include references to the relevant specification and plan documents in comments or documentation.

## 4. Phase Enforcement Rules

**Phase I - Core System Setup**: Foundation work only. No frontend, no agents, no Kafka/Dapr, no cloud deployment. Focus on basic architecture and tooling setup.

**Phase II - Frontend + Backend Integration**: Integration work only. No chatbot, no Kubernetes, no cloud deployment. Focus on connecting frontend and backend systems.

**Phase III - Chatbot + Agent Behavior**: AI behavior work only. No Kubernetes, no cloud deployment. Focus on implementing chatbot and agent-specific functionality.

**Phase IV - Local Kubernetes + Kafka/Dapr**: Containerization and event-driven architecture. No cloud deployment. Focus on local Kubernetes (Minikube) and Kafka/Dapr integration.

**Phase V - Cloud Deployment + Production Readiness**: Production deployment work only. Focus on cloud deployment (DigitalOcean) and production readiness.

**No Phase Skipping**: Each phase must be completed before advancing to the next. Partial completion is acceptable but skipping phases is forbidden.

## 5. Architecture Constraints

**Microservices Only**: All systems must be designed as independent microservices. Monolithic architectures are prohibited.

**Kafka via Dapr Pub/Sub Abstraction**: All event streaming must use Kafka through Dapr's Pub/Sub abstraction layer. Direct Kafka SDK usage is forbidden when Dapr is available.

**No Hardcoded Credentials**: No credentials, API keys, or secrets may be hardcoded in source code. All secrets must be managed through proper secret management systems.

**Stateless Services Where Possible**: Services must be designed as stateless where possible to ensure scalability and resilience.

## 6. Tooling Constraints

**Spec-Kit Plus Lifecycle Mandatory**: The complete Spec-Kit Plus lifecycle (specify → plan → tasks → implement) must be followed for all development work.

**MCP Servers for External Access Only**: MCP servers may only be used for external system access and must not be used for internal service communication.

**No Direct SDK Usage When Dapr Available**: When Dapr provides an abstraction for databases, Kafka, or other services, direct SDK usage is prohibited.

## 7. Security & Reliability Rules

**Secrets Management**: All secrets must be stored and accessed through proper secret management systems (Dapr Secrets, Kubernetes Secrets, or cloud provider secret stores). No secrets in code, configuration files, or repositories.

**No Credentials in Code or Repos**: No credentials of any kind may be stored in source code repositories. All credential storage must be external to the codebase.

**Retry, Idempotency, and Failure Handling**: All service interactions must implement proper retry logic, idempotency where appropriate, and graceful failure handling.

## 8. Documentation & Submission Rules

**Required Repository Structure**: Repository must include `.specify/specs/`, `.specify/plans/`, `.specify/tasks/`, and implementation directories with clear separation between specification and implementation.

**Mandatory Documentation**: README, specifications, plans, and tasks documents are mandatory for submission. Missing documentation results in automatic failure.

**Demo Video Constraints**: All demo videos must be 90 seconds or less, demonstrating the implemented functionality and the spec-driven development process.

## 9. Violation Handling

**Immediate Halt on Rule Violations**: When any constitutional rule is violated, all development must stop immediately until human approval is obtained.

**Escalation to Human Required**: All violations must be escalated to human operators for resolution. Agents cannot make exceptions to constitutional rules.

**Documentation of Violations**: All violations and their resolutions must be documented in the project history.

## 10. Final Authority Statement

**Constitution Overrides All**: This Constitution document is the highest authority in the project hierarchy and overrides all other documents, agent creativity, and implementation preferences.

**Predictability Over Cleverness**: All decisions must prioritize predictable, compliant behavior over clever or innovative solutions.

**Specifications Over Code**: The specification documents (spec, plan, tasks) are the authoritative source of truth, not the implementation code.

---

**Established**: 2026-01-05
**Version**: 1.0.0
**Authority**: This Constitution governs all aspects of the 5-Phase Spec-Driven AI Hackathon project and must be followed without exception.
