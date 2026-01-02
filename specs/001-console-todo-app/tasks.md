---
description: "Task list template for feature implementation"
---

# Tasks: Console Todo Application

**Input**: Design documents from `/specs/001-console-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

<!--
  ============================================================================
  IMPORTANT: The tasks below are SAMPLE TASKS for illustration purposes only.

  The /sp.tasks command MUST replace these with actual tasks based on:
  - User stories from spec.md (with their priorities P1, P2, P3...)
  - Feature requirements from plan.md
  - Entities from data-model.md
  - Endpoints from contracts/

  Tasks MUST be organized by user story so each story can be:
  - Implemented independently
  - Tested independently
  - Delivered as an MVP increment

  DO NOT keep these sample tasks in the generated tasks.md file.
  ============================================================================
-->

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create `/src` directory structure
- [x] T002 [P] Create empty Python files: main.py, models.py, service.py, ui.py, exceptions.py in src/
- [x] T003 [P] Create `/tests/unit` and `/tests/integration` directory structure

---
## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T004 Create Todo class in src/models.py with id, title, description, completed attributes
- [x] T005 [P] Create custom exceptions in src/exceptions.py: TodoNotFoundError, InvalidInputError
- [x] T006 Create TodoService class in src/service.py with in-memory storage (todos list, next_id counter)

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---
## Phase 3: User Story 1 - Add Todo Item (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new todo items with required title and optional description

**Independent Test**: Can be fully tested by running the application, selecting "Add Todo", entering a title and description, and verifying that the item appears in the list with a unique ID and incomplete status.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T007 [P] [US1] Unit test for Todo model in tests/unit/test_models.py
- [ ] T008 [P] [US1] Unit test for add_todo function in tests/unit/test_service.py

### Implementation for User Story 1

- [x] T009 [P] [US1] Implement Todo class with attributes and validation in src/models.py
- [x] T010 [P] [US1] Implement add_todo method in TodoService in src/service.py
- [x] T011 [US1] Implement add_todo functionality in UI layer in src/ui.py
- [x] T012 [US1] Create basic menu loop in main.py to route to add_todo functionality
- [x] T013 [US1] Add validation for non-empty titles in add_todo method

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---
## Phase 4: User Story 2 - View All Todo Items (Priority: P2)

**Goal**: Enable users to see all their todo items with proper formatting and status indicators

**Independent Test**: Can be tested by adding a few todo items and then selecting "View Todos" to verify all items are displayed with proper formatting and status indicators.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T014 [P] [US2] Unit test for get_all_todos function in tests/unit/test_service.py
- [ ] T015 [P] [US2] UI test for displaying todos in tests/unit/test_ui.py

### Implementation for User Story 2

- [x] T016 [P] [US2] Implement get_all_todos method in TodoService in src/service.py
- [x] T017 [US2] Implement display todos functionality in UI layer in src/ui.py
- [x] T018 [US2] Integrate view todos functionality into main menu in main.py
- [x] T019 [US2] Handle case when no todos exist with appropriate message

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---
## Phase 5: User Story 3 - Update Todo Item (Priority: P3)

**Goal**: Enable users to modify existing todo items by changing title or description

**Independent Test**: Can be tested by creating a todo item, selecting "Update Todo", providing the ID and new values, and verifying the changes are reflected when viewing the todo list.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [ ] T020 [P] [US3] Unit test for update_todo function in tests/unit/test_service.py

### Implementation for User Story 3

- [x] T021 [P] [US3] Implement update_todo method in TodoService in src/service.py
- [x] T022 [US3] Implement update todo functionality in UI layer in src/ui.py
- [x] T023 [US3] Integrate update todos functionality into main menu in main.py
- [x] T024 [US3] Add validation for ID existence in update method

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---
## Phase 6: User Story 4 - Delete Todo Item (Priority: P3)

**Goal**: Enable users to remove todo items that are no longer needed

**Independent Test**: Can be tested by creating a todo item, selecting "Delete Todo", providing the ID, and verifying the item no longer appears in the list.

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [ ] T025 [P] [US4] Unit test for delete_todo function in tests/unit/test_service.py

### Implementation for User Story 4

- [x] T026 [P] [US4] Implement delete_todo method in TodoService in src/service.py
- [x] T027 [US4] Implement delete todo functionality in UI layer in src/ui.py
- [x] T028 [US4] Integrate delete todos functionality into main menu in main.py
- [x] T029 [US4] Add validation for ID existence in delete method

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---
## Phase 7: User Story 5 - Mark Todo Complete/Incomplete (Priority: P3)

**Goal**: Enable users to track completion status by toggling todo item status

**Independent Test**: Can be tested by creating a todo item, selecting "Mark Complete/Incomplete", providing the ID, and verifying the status changes appropriately.

### Tests for User Story 5 (OPTIONAL - only if tests requested) ⚠️

- [ ] T030 [P] [US5] Unit test for toggle_todo_status function in tests/unit/test_service.py

### Implementation for User Story 5

- [x] T031 [P] [US5] Implement toggle_todo_status method in TodoService in src/service.py
- [x] T032 [US5] Implement toggle status functionality in UI layer in src/ui.py
- [x] T033 [US5] Integrate toggle status functionality into main menu in main.py
- [x] T034 [US5] Add validation for ID existence in toggle method

**Checkpoint**: All user stories should now be independently functional

---
## Phase 8: Error Handling & Validation (Cross-User Story)

**Goal**: Ensure all user stories handle errors gracefully without crashing

- [x] T035 [P] Implement error handling for invalid menu selections across all user stories
- [x] T036 [P] Implement validation for non-numeric ID inputs across all user stories
- [x] T037 [P] Implement validation for non-existent IDs across all user stories
- [x] T038 [P] Implement validation for empty/whitespace titles across all user stories

---
## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T039 [P] Complete main menu with all options in main.py
- [x] T040 [P] Implement graceful exit functionality in main.py
- [x] T041 [P] Code cleanup and refactoring
- [x] T042 [P] Add type hints where helpful
- [x] T043 [P] Add docstrings to public methods
- [x] T044 [P] Run quickstart validation to ensure all functionality works

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Error Handling (Phase 8)**: Depends on all user story implementations
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3/US4 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before UI components
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Unit test for Todo model in tests/unit/test_models.py"
Task: "Unit test for add_todo function in tests/unit/test_service.py"

# Launch all models for User Story 1 together:
Task: "Implement Todo class with attributes and validation in src/models.py"
Task: "Implement add_todo method in TodoService in src/service.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence