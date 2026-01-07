# Feature Specification: Phase 1 - Basic In-Memory Todo Console Application

**Feature Branch**: `001-phase1-todo-console`
**Created**: 2025-12-28
**Status**: Draft
**Input**: User description for Phase 1 Todo console app with 6 features including search

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Add Tasks (Priority: P1)

As a user, I want to add new tasks with descriptions so that I can track things I need to do.

**Why this priority**: Adding tasks is the fundamental operation - without it, nothing else matters.

**Independent Test**: Can be fully tested by running the application, entering "add Buy milk", and verifying a task appears in the list.

**Acceptance Scenarios**:

1. **Given** the application is running, **When** I enter `add Buy milk and eggs`, **Then** a new task with description "Buy milk and eggs" is created with completed=false.

2. **Given** the application is running with 3 existing tasks, **When** I enter `add Finish report`, **Then** the new task has ID 4 (auto-incremented from 1).

3. **Given** the application is running, **When** I enter `add    ` (whitespace only), **Then** an error message is shown: "Error: Task description cannot be empty."

---

### User Story 2 - Delete Tasks (Priority: P1)

As a user, I want to delete tasks I no longer need so that my list stays relevant.

**Why this priority**: Managing task lifecycle includes removal - essential for a usable todo app.

**Independent Test**: Can be fully tested by adding tasks, listing them, deleting one, and verifying it's removed.

**Acceptance Scenarios**:

1. **Given** the task list contains 3 tasks, **When** I enter `delete 2`, **Then** task with ID 2 is removed and remaining tasks keep their IDs (no renumbering).

2. **Given** the task list contains 1 task, **When** I enter `delete 1`, **Then** the list becomes empty.

3. **Given** the application is running, **When** I enter `delete 5` (non-existent index), **Then** an error message is shown: "Error: Invalid index 5. Valid range: 1 to [current_count]."

4. **Given** the application is running, **When** I enter `delete abc` (non-numeric), **Then** an error message is shown: "Error: Index must be a number."

---

### User Story 3 - Update Task Descriptions (Priority: P1)

As a user, I want to modify task descriptions so that I can correct or improve my task details.

**Why this priority**: Tasks often need refinement - critical for real-world usage.

**Independent Test**: Can be fully tested by adding a task, updating it, and verifying the new description.

**Acceptance Scenarios**:

1. **Given** a task exists with description "Buy milk", **When** I enter `update 1 Buy eggs instead`, **Then** the task's description changes to "Buy eggs instead" and completed status remains unchanged.

2. **Given** a task exists, **When** I enter `update 1    ` (whitespace only), **Then** an error message is shown and description remains unchanged.

3. **Given** 5 tasks exist, **When** I enter `update 10 New description` (out of range), **Then** an error message is shown and no tasks are modified.

---

### User Story 4 - View Task List (Priority: P1)

As a user, I want to see all my tasks with their status so that I can review what I need to do.

**Why this priority**: Visibility is essential - users must see their tasks to manage them.

**Independent Test**: Can be fully tested by adding tasks, running list, and verifying output format.

**Acceptance Scenarios**:

1. **Given** the task list is empty, **When** I enter `list`, **Then** the message "No tasks yet. Add one with 'add <description>'." is displayed.

2. **Given** 3 tasks exist (IDs 1, 2, 3) with different completion statuses, **When** I enter `list`, **Then** tasks are displayed as:
   ```
   1. [ ] Buy groceries
   2. [x] Call mom
   3. [ ] Finish report
   ```

3. **Given** many tasks exist, **When** I enter `list`, **Then** all tasks are displayed with numbering, description, and status indicators.

---

### User Story 5 - Toggle Task Completion (Priority: P1)

As a user, I want to mark tasks as done so that I can track my progress.

**Why this priority**: Core todo app functionality - users need to know what's complete.

**Independent Test**: Can be fully tested by adding a task, toggling it, and verifying status changes.

**Acceptance Scenarios**:

1. **Given** task 1 is incomplete "[ ]", **When** I enter `complete 1`, **Then** task 1 becomes "[x]" (completed).

2. **Given** task 2 is already completed "[x]", **When** I enter `complete 2`, **Then** task 2 becomes "[ ]" (incomplete - toggle behavior).

3. **Given** tasks exist, **When** I enter `complete 999` (invalid index), **Then** an error message is shown.

---

### User Story 6 - Search Tasks (Priority: P2)

As a user, I want to search for tasks by keyword so that I can find specific tasks in a long list.

**Why this priority**: Useful for large task lists; enhances usability but not essential for MVP.

**Independent Test**: Can be fully tested by adding multiple tasks with different descriptions and verifying search finds correct ones.

**Acceptance Scenarios**:

1. **Given** tasks exist with descriptions "Buy milk", "Buy eggs", "Clean house", **When** I enter `search buy`, **Then** tasks 1 and 2 are displayed (case-insensitive match).

2. **Given** no tasks match the search term, **When** I enter `search xyz`, **Then** the message "No tasks found matching 'xyz'." is displayed.

3. **Given** tasks exist, **When** I enter `search ` (empty keyword), **Then** an error message is shown: "Error: Search keyword cannot be empty."

4. **Given** tasks have mixed completion statuses, **When** I enter a valid search, **Then** matching tasks display with their correct completion status.

---

### User Story 7 - Help Command (Priority: P3)

As a new user, I want to see available commands so that I can learn how to use the application.

**Why this priority**: Improves onboarding but not critical for experienced users.

**Acceptance Scenarios**:

1. **Given** the application is running, **When** I enter `help`, **Then** the following is displayed:
   ```
   Available commands:
     add <description>      - Add a new task
     delete <index>         - Delete a task by index
     update <index> <desc>  - Update a task's description
     complete <index>       - Toggle task completion
     list                   - Show all tasks
     search <keyword>       - Search tasks by keyword
     help                   - Show this message
     quit                   - Exit the application
   ```

---

### User Story 8 - Quit Application (Priority: P3)

As a user, I want to exit the application cleanly.

**Why this priority**: Basic usability requirement.

**Acceptance Scenarios**:

1. **Given** the application is running, **When** I enter `quit`, **Then** the application exits with message "Goodbye!".

---

## Edge Cases

- **Empty task list**: All operations (delete, update, complete, search, list) handle empty state gracefully.
- **Whitespace-only descriptions**: Both add and update reject descriptions that are only whitespace.
- **Invalid indices**: Non-numeric input, zero, negative numbers, and out-of-range indices all produce clear error messages.
- **Search with no matches**: Clear "no tasks found" message with the search term shown.
- **Search with multiple matches**: All matching tasks displayed with correct format.
- **Search case sensitivity**: "MILK", "milk", and "Milk" all match search for "milk".
- **Large task list**: All operations work correctly regardless of task count (limited only by memory).
- **Toggle after update**: Completion status persists across description updates.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST allow users to add tasks with a non-empty description.
- **FR-002**: System MUST assign unique auto-incrementing IDs starting from 1 to each task.
- **FR-003**: System MUST allow users to delete tasks by their 1-based index.
- **FR-004**: System MUST allow users to update task descriptions by index.
- **FR-005**: System MUST allow users to toggle task completion status by index.
- **FR-006**: System MUST display all tasks with ID, description, and completion status using "[x]" or "[ ]".
- **FR-007**: System MUST search tasks by keyword using case-insensitive partial matching.
- **FR-008**: System MUST provide a help command showing all available commands.
- **FR-009**: System MUST provide a quit command to exit the application.
- **FR-010**: System MUST validate all user inputs and display clear error messages for invalid input.
- **FR-011**: System MUST maintain task IDs unchanged when other tasks are deleted.

### Key Entities

- **Task**: Represents a single todo item with the following attributes:
  - `id`: Integer, unique, auto-incrementing starting from 1
  - `description`: String, non-empty, user-provided task text
  - `completed`: Boolean, indicates if task is done

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can successfully add a task and see it appear in the list within 5 seconds of starting the application.
- **SC-002**: All 6 core operations (add, delete, update, complete, list, search) complete within 1 second each on standard hardware.
- **SC-003**: Error messages are displayed within 1 second of invalid input.
- **SC-004**: 100% of valid commands produce the expected output or state change.
- **SC-005**: Search returns all tasks whose description contains the keyword (case-insensitive).

## Technical Assumptions

- **Platform**: Console/terminal application running on Python 3.x
- **Storage**: In-memory list of dictionaries; data is not persisted between runs
- **Input**: Single-line commands via `input()` function
- **Encoding**: UTF-8 for all task descriptions
- **Performance**: O(n) search is acceptable for in-memory data
- **Error handling**: User-friendly messages; no stack traces exposed to users

## Out of Scope

- Task persistence between sessions
- Task prioritization or ordering (beyond insertion order)
- Categories, tags, or folders
- Due dates or reminders
- Undo/redo functionality
- Import/export capabilities
- Multiple users or authentication
- Data backup or recovery
