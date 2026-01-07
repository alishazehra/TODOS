# Tasks: Phase 1 - Basic In-Memory Todo Console Application with Search

**Input**: Design documents from `/specs/001-phase1-todo-console/`
**Prerequisites**: plan.md, spec.md, data-model.md
**Tests**: Not requested in spec - verification via console output

**Organization**: Tasks are grouped by user story to enable independent implementation and testing.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: All code in `phase1/todo.py`

---

## Phase 1: Setup (Shared Infrastructure) ✅ COMPLETED

**Purpose**: Project initialization and basic structure

- [x] T001 Create phase1 directory and todo.py file with module docstring
- [x] T002 Initialize global state: empty `tasks` list and `next_id = 1` counter

---

## Phase 2: Foundational (Blocking Prerequisites) ✅ COMPLETED

**Purpose**: Shared components used by ALL user stories

**CRITICAL**: No user story work can begin until this phase is complete

- [x] T003 [P] Implement `format_task(task)` helper function in todo.py
  - Returns string: `"1. [ ] Buy groceries"` format
  - Handle `[x]` for completed, `[ ]` for incomplete
- [x] T004 [P] Implement error handling utilities in todo.py
  - `validate_index(index, tasks)`: Returns (is_valid, error_message)
  - `validate_description(description)`: Returns (is_valid, error_message)
  - `validate_keyword(keyword)`: Returns (is_valid, error_message)

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - Add Tasks (Priority: P1) ✅ COMPLETED

**Goal**: Users can add new tasks with descriptions

**Independent Test**: Run app, enter `add Buy milk`, verify task appears in list

- [x] T005 [US1] Implement `add_task(description)` function in todo.py
  - Validate description is not empty/whitespace
  - Create task dict with id, description, completed=false
  - Append to tasks list, increment next_id
  - Print confirmation: "Task added: {description} (ID: {id})"

**Checkpoint**: User Story 1 complete - basic add functionality works

---

## Phase 4: User Story 2 - Delete Tasks (Priority: P1) ✅ COMPLETED

**Goal**: Users can remove tasks by their 1-based index

**Independent Test**: Add tasks, delete one, verify it's removed and IDs unchanged

- [x] T006 [US2] Implement `delete_task(index)` function in todo.py
  - Use validate_index from T004
  - Remove task at index-1 (1-based to 0-based)
  - Print confirmation: "Task {id} deleted."
  - Note: IDs of remaining tasks stay unchanged

**Checkpoint**: User Story 2 complete - delete functionality works

---

## Phase 5: User Story 3 - Update Task Descriptions (Priority: P1) ✅ COMPLETED

**Goal**: Users can modify task descriptions by index

**Independent Test**: Add task, update it, verify new description appears

- [x] T007 [US3] Implement `update_task(index, new_description)` function in todo.py
  - Validate index and new_description
  - Update task's description field
  - Preserve completed status
  - Print confirmation: "Task {id} updated."

**Checkpoint**: User Story 3 complete - update functionality works

---

## Phase 6: User Story 4 - View Task List (Priority: P1) ✅ COMPLETED

**Goal**: Users can see all tasks with completion status

**Independent Test**: Add multiple tasks, run list, verify correct format

- [x] T008 [US4] Implement `list_tasks()` function in todo.py
  - Handle empty list case with helpful message
  - Loop through tasks and call format_task()
  - Print each formatted task

**Checkpoint**: User Story 4 complete - list functionality works

---

## Phase 7: User Story 5 - Toggle Task Completion (Priority: P1) ✅ COMPLETED

**Goal**: Users can mark tasks as done or undone

**Independent Test**: Add task, toggle complete twice, verify status changes both ways

- [x] T009 [US5] Implement `toggle_complete(index)` function in todo.py
  - Validate index
  - Flip completed boolean (True <-> False)
  - Print confirmation showing new status

**Checkpoint**: User Story 5 complete - toggle functionality works

---

## Phase 8: User Story 6 - Search Tasks (Priority: P2) ✅ COMPLETED

**Goal**: Users can find tasks by keyword (case-insensitive partial match)

**Independent Test**: Add tasks with different descriptions, search, verify matches found

- [x] T010 [US6] Implement `search_tasks(keyword)` function in todo.py
  - Validate keyword is not empty
  - Case-insensitive partial match: `keyword.lower() in task["description"].lower()`
  - Collect matching tasks
  - Display using format_task() in numbered list
  - Handle no matches: "No tasks found matching '{keyword}'."

**Checkpoint**: User Story 6 complete - search functionality works

---

## Phase 9: User Story 7 - Help + User Story 8 - Quit (Priority: P3) ✅ COMPLETED

**Goal**: Users can see help and exit the application

**Independent Test**: Enter help, verify all commands shown. Enter quit, verify exit.

- [x] T011 [US7] Implement `show_help()` function in todo.py
  - Return formatted help text with all 8 commands
  - Include command syntax and descriptions
- [x] T012 [US8] Implement `quit()` function in todo.py
  - Print "Goodbye!" message
  - Return True to signal main loop to exit

**Checkpoint**: User Stories 7 and 8 complete - help and quit work

---

## Phase 10: Polish & Cross-Cutting Concerns ✅ COMPLETED

**Purpose**: Integration, main loop, and verification

- [x] T013 Implement command dispatcher in todo.py
  - Parse input line into command and arguments
  - Support: add, delete, update, complete, list, search, help, quit
  - Handle unknown commands with error message
- [x] T014 Implement main loop in todo.py
  - Print welcome message on startup
  - Print help message on startup
  - Enter `while True` loop with `input("> ")`
  - Exit on quit command or KeyboardInterrupt (Ctrl+C)
- [x] T015 Create verification checklist in phase1/tests/verification.md
  - Document step-by-step test cases for all 8 user stories
  - Include expected outputs for each command
  - List edge cases to verify

---

## Summary: All 15 Tasks Completed ✅

| Phase | Tasks | Status |
|-------|-------|--------|
| Phase 1: Setup | T001-T002 | ✅ |
| Phase 2: Foundational | T003-T004 | ✅ |
| Phase 3: US1 Add | T005 | ✅ |
| Phase 4: US2 Delete | T006 | ✅ |
| Phase 5: US3 Update | T007 | ✅ |
| Phase 6: US4 List | T008 | ✅ |
| Phase 7: US5 Toggle | T009 | ✅ |
| Phase 8: US6 Search | T010 | ✅ |
| Phase 9: US7-US8 Help/Quit | T011-T012 | ✅ |
| Phase 10: Polish | T013-T015 | ✅ |

**Total: 15/15 tasks completed**

---

## Dependencies & Execution Order (Complete)

### Phase Dependencies

| Phase | Depends On | Blocks |
|-------|-----------|--------|
| Setup (1) | None | Foundational |
| Foundational (2) | Setup | All User Stories |
| User Stories (3-9) | Foundational | Polish |
| Polish (10) | All User Stories | None |

### User Story Dependencies

| Story | Priority | Dependencies |
|-------|----------|--------------|
| US1: Add Tasks | P1 | Foundational (T003-T004) |
| US2: Delete Tasks | P1 | Foundational (T003-T004) |
| US3: Update Tasks | P1 | Foundational (T003-T004) |
| US4: List Tasks | P1 | Foundational (T003) |
| US5: Toggle Complete | P1 | Foundational (T003-T004) |
| US6: Search Tasks | P2 | Foundational (T003-T004) |
| US7: Help | P3 | Foundational |
| US8: Quit | P3 | Foundational |

**All user stories depend on Phase 2 completion but are independent of each other**

### Parallel Opportunities

- T003 and T004 (foundational helpers) can run in parallel
- All user story implementations (T005-T012) can run in parallel after T004
- T013 (dispatcher) and T014 (main loop) can run in parallel
- Verification (T015) must run last

---

## Implementation Strategy (Complete)

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001-T002)
2. Complete Phase 2: Foundational (T003-T004)
3. Complete Phase 3: User Story 1 (T005)
4. **STOP and VALIDATE**: Test add functionality independently
5. Deploy/demo if US1-only MVP is acceptable

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Complete US1 → Test → Deploy (MVP add functionality)
3. Complete US2 → Test → Deploy
4. Complete US3 → Test → Deploy
5. Complete US4 → Test → Deploy
6. Complete US5 → Test → Deploy
7. Complete US6 → Test → Deploy
8. Complete US7 + US8 → Test → Deploy
9. Complete Polish → Final verification

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: US1 + US4 + US6 (display/search)
   - Developer B: US2 + US3 + US5 (CRUD operations)
   - Developer C: US7 + US8 + Polish (help, quit, main loop)
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different components, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- No tests requested in spec - use verification.md for manual testing
- All tasks output to single file: `phase1/todo.py`
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
