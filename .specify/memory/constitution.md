<!--
Sync Impact Report:
Version change: N/A → 1.0.0
List of modified principles: N/A (new constitution)
Added sections: All sections (new constitution created)
Removed sections: N/A
Templates requiring updates: ⚠ pending - .specify/templates/plan-template.md, .specify/templates/spec-template.md, .specify/templates/tasks-template.md
Follow-up TODOs: None
-->

# In-Memory Python Console Todo App Constitution

## Core Principles

### Phase I Hackathon Development
All development must strictly follow the Spec-Kit Plus workflow: Constitution, Specify, Plan, Tasks, Implement. No manual coding is allowed at any stage. All source code must be generated and modified only through Claude Code.

### Functional Scope (Phase I)
The application must implement exactly the following features: 1) Add a todo item with a title and optional description, 2) List all todo items with unique IDs and completion status, 3) Update an existing todo item by ID, 4) Delete a todo item by ID, 5) Mark a todo item as complete or incomplete.

### Technical Constraints
Programming language: Python. Python version: 3.12.6. Interface: Console / Command Line only. Data storage: In-memory only (no files, no databases). Code must follow clean code principles and be well-structured.

### Tooling Constraints
Claude Code must act as the primary General Agent. Spec-Kit Plus must manage all specifications and implementation steps. uv must be used for Python environment management.

### Repository Requirements
The project repository must include: A `/src` directory containing the Python source code, A `/specs/history` directory containing all specification versions, A `CLAUDE.md` file explaining how Claude Code is used, A `README.md` file with setup and usage instructions, This constitution generated via Spec-Kit Plus.

### Development Rules

All development must strictly follow the Spec-Kit Plus workflow with no deviations.

## Additional Constraints
The application is a simple, in-memory, command-line Todo application using Python. The goal is to demonstrate spec-driven, agentic development using Claude Code and Spec-Kit Plus.

## Development Workflow
All development must strictly follow the Spec-Kit Plus workflow: Constitution, Specify, Plan, Tasks, Implement. No manual coding is allowed at any stage. All source code must be generated and modified only through Claude Code.

## Governance
This project is a Phase I hackathon task to build a simple, in-memory, command-line Todo application using Python. The goal is to demonstrate spec-driven, agentic development using Claude Code and Spec-Kit Plus. Any deviation from this constitution or workflow may result in disqualification.

**Version**: 1.0.0 | **Ratified**: 2026-01-02 | **Last Amended**: 2026-01-02
