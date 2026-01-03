# speckit.constitution
# Hackathon II – Master Constitution (Phases I–V)
# Purpose: Single source of truth for rules, principles, tech stack, and agent behavior

---

## 1. Project Principles

1. **Spec-Driven Development (SDD)**: 
   - No code is allowed until specifications (speckit.specify, speckit.plan, speckit.tasks) are fully written and approved.
   - Workflow: **Specify → Plan → Tasks → Implement**

2. **Single Constitution File**:
   - Only one `speckit.constitution` exists for the entire Hackathon II.
   - Covers Phase I → V rules, architecture principles, stack constraints, agent conduct.
   - Cannot be duplicated or modified per phase.

3. **Phase-Specific Files Allowed**:
   - `speckit.specify`, `speckit.plan`, `speckit.tasks` can be created per phase.
   - Each phase’s implementation must reference the **master constitution**.

4. **Agent Compliance**:
   - All AI agents (Claude, Copilot, Gemini, local LLMs) must obey this constitution.
   - Agents **cannot override rules**, invent code, or bypass workflow.
   - Agents must reference Task IDs, Specification, and Plan for every implementation.

---

## 2. Technology Stack Constraints

| Component         | Allowed Technology / Tool                          |
|------------------|---------------------------------------------------|
| Frontend         | OpenAI ChatKit, Next.js (or React-based)          |
| Backend          | FastAPI (Python), OpenAI Agents SDK               |
| Database         | Neon Serverless PostgreSQL                        |
| ORM              | SQLModel                                          |
| Authentication   | Better Auth                                      |
| Containerization | Docker Desktop, Gordon (Docker AI)               |
| Kubernetes       | Minikube (local), AKS / GKE / OKE (cloud)       |
| Helm             | Helm Charts for all deployments                  |
| AI DevOps        | kubectl-ai, Kagent                               |
| Event Streaming  | Kafka (Redpanda Cloud / Strimzi operator)       |
| Distributed Runtime | Dapr (Pub/Sub, State, Bindings, Jobs, Secrets) |

**Notes:**  
- Stack must remain as above. Additional libraries allowed only if fully compatible.  
- Agents cannot change backend framework, database, or main orchestration method without explicit human approval.

---

## 3. Architecture Principles

1. **Stateless Server Design**:
   - Backend server should not hold conversation state; use database or Dapr state management.
   - Scalable, horizontally deployable, resilient.

2. **Microservices Separation**:
   - Frontend, Chat API, Notification Service, Recurring Task Service, Audit Service must be separate services/pods.
   - Event-driven interactions via Kafka or Dapr Pub/Sub.

3. **Decoupled Event Handling**:
   - Task operations, reminders, recurring tasks, real-time updates must be published as events, not direct API calls.
   - Kafka topics: `task-events`, `reminders`, `task-updates`.

4. **Dapr Abstraction**:
   - Backend apps must use Dapr sidecars for Pub/Sub, State, Jobs, Secrets, Service Invocation where possible.
   - Allows backend code to remain clean and backend dependencies swappable.

5. **CI/CD & Cloud-Readiness**:
   - Phase IV: Local Minikube deployment (containerized, Helm-based).  
   - Phase V: Cloud deployment (AKS/GKE/OKE), with Dapr, Kafka, monitoring/logging, CI/CD via GitHub Actions.

---

## 4. Agent Conduct Rules

1. **No freestyle coding**:
   - Agents must not generate code without a Task ID referencing `speckit.tasks`.

2. **Follow Spec Hierarchy**:
   - Constitution > Specify > Plan > Tasks
   - Any deviation must be explicitly requested and documented.

3. **Implementation Rules**:
   - Always reference Task ID, Spec section, and Plan section in code comments.
   - Agents cannot add endpoints, fields, workflows not present in the spec.

4. **Error Handling & Confirmation**:
   - Agents must provide graceful error messages.
   - Always confirm user actions (task created, completed, deleted, updated).

5. **Tool Usage**:
   - Use MCP tools only for defined operations.
   - No direct DB manipulations outside defined MCP/Dapr tools.

6. **Phase Compliance**:
   - Phase-specific features (Phase II: Basic Todos, Phase III: MCP, Phase IV: Kubernetes, Phase V: Advanced Cloud & Kafka) must respect the constitution.
   - New features require spec updates first.

---

## 5. Security & Operational Guidelines

1. **Secrets Management**:
   - Use Dapr Secrets API or Kubernetes Secrets.
   - No API keys or passwords in codebase.

2. **Database Access**:
   - All conversation and task data must be persisted in Neon PostgreSQL or via Dapr state.
   - No local in-memory storage for persistent state.

3. **Cloud Domain Security**:
   - Frontend must register domain in OpenAI allowlist before deploying ChatKit.
   - Use HTTPS in production environments.

4. **Scaling & Resilience**:
   - Backend and microservices must be horizontally scalable.
   - Stateless design ensures resilience to pod restarts.

---

## 6. Testing & Validation Principles

1. **Unit Testing**:
   - Minimum 90% coverage for backend MCP tool operations.

2. **Integration Testing**:
   - Verify MCP tool interactions, Dapr Pub/Sub, database state.

3. **Deployment Validation**:
   - Minikube: Verify pods, services, Helm chart functionality.  
   - Cloud (AKS/GKE/OKE): Verify Dapr sidecars, Kafka topics, CI/CD pipeline.

---

## 7. Documentation & Submission Rules

1. **Repository Structure**:
   - `/frontend` → ChatKit frontend
   - `/backend` → FastAPI backend + MCP tools
   - `/specs` → speckit files
   - `/k8s` → Helm charts, Dapr components, Kubernetes manifests

2. **CLAUDE.md & AGENTS.md**:
   - CLAUDE.md forwards to AGENTS.md for agent instructions.
   - Agents read these files to execute Spec-Kit commands.

3. **Demo Video**:
   - Max 90 seconds; demonstrate features and Spec-Driven workflow.

4. **Submission**:
   - GitHub repo + deployed URLs for each phase.
   - Partial phases accepted; scoring proportional.

---

## 8. Versioning & Change Control

1. Constitution is immutable for Hackathon II duration.
2. Only human organizers may update it.
3. Agents **cannot propose edits to this file**.
4. Phase-specific changes allowed only in `speckit.specify` and `speckit.plan`.

---

**End of Hackathon II Master Constitution**  
