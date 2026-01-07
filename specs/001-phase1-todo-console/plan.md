# Phase 1 Implementation Plan: Basic In-Memory Todo Console App with Search

**Branch**: `001-phase1-todo-console`
**Date**: 2025-12-28
**Spec**: [spec.md](./spec.md)

## 1. Overview

A simple console-based Todo application built in Python 3 that allows users to manage tasks without any data persistence. The application stores tasks in memory using a list of dictionaries and provides a command-line interface for interaction.

**6 Core Features:**
1. **Add Task** - Create new tasks with descriptions
2. **Delete Task** - Remove tasks by their 1-based index
3. **Update Task** - Modify task descriptions by index
4. **List Tasks** - View all tasks with completion status indicators
5. **Toggle Completion** - Mark tasks as done or undone by index
6. **Search Tasks** - Find tasks by keyword (case-insensitive partial match)

## 2. Technical Choices

| Component | Choice | Rationale |
|-----------|--------|-----------|
| **Language** | Python 3.x | Specified in Constitution; simple, readable, no compilation needed |
| **Storage** | In-memory list of dictionaries | Per Constitution: `tasks = [{"id": int, "description": str, "completed": bool}]` |
| **User Interface** | Command-line loop with `input()` | Spec requirement; no external libraries needed |
| **File Structure** | Single-file application (`todo.py`) | Simplest approach for Phase 1; easy to run |
| **External Dependencies** | None (standard library only) | Per Constitution tech stack constraints |
| **Encoding** | UTF-8 | Standard for Python; handles international characters |
| **Error Handling** | User-friendly messages | No stack traces exposed; clear error context |

## 3. High-Level Architecture

### Global State
```python
tasks: List[Dict[str, Any]]  # [{"id": int, "description": str, "completed": bool}]
next_id: int  # Auto-incrementing counter starting from 1
```

### Main Components

| Component | Responsibility |
|-----------|----------------|
| **Command Parser** | Parse user input into command + arguments |
| **Dispatcher** | Route commands to appropriate handler functions |
| **Handler Functions** | Implement business logic for each command |
| **Display Helpers** | Format and render task output |
| **Error Handlers** | Validate inputs and produce error messages |

### Program Flow
```
┌─────────────────────────────────────┐
│           Start Application         │
└──────────────┬──────────────────────┘
               ▼
┌─────────────────────────────────────┐
│     Print Welcome + Help Message    │
└──────────────┬──────────────────────┘
               ▼
┌─────────────────────────────────────┐
│    While True: Read user input      │
└──────────────┬──────────────────────┘
               ▼
┌─────────────────────────────────────┐
│           Parse Command             │
└──────────────┬──────────────────────┘
               ▼
┌─────────────────────────────────────┐
│         Dispatch to Handler         │
└──────────────┬──────────────────────┘
               ▼
┌─────────────────────────────────────┐
│        Execute + Display Result     │
└──────────────┬──────────────────────┘
               ▼
     (loop back to read input)
```

## 4. File Structure

```
phase1/
├── todo.py              # Main application (all code here, ~200-250 lines)
├── README.md            # Quick guide (auto-generated)
└── tests/               # Manual verification tests
    └── verification.md  # Console test cases
```

**Note:** For Phase 1, a single-file application is sufficient. No separate test file needed - verification will be done via inline comments and a verification.md checklist.

## 5. Detailed Task Breakdown

### Phase 1: Foundation (Tasks 1-3)

**T1. Set up global state**
- Initialize empty `tasks` list
- Initialize `next_id = 1`
- Add module docstring with description

**T2. Implement display helper function**
- Create `format_task(task)` function
- Returns string: `"1. [ ] Buy groceries"`
- Handle `[x]` for completed, `[ ]` for incomplete

**T3. Implement list_tasks()**
- Handle empty list case with helpful message
- Loop through tasks and call `format_task()`
- Print each formatted task

### Phase 2: Core CRUD (Tasks 4-7)

**T4. Implement add_task(description)**
- Validate description is not empty/whitespace only
- Create task dict with id, description, completed=false
- Append to tasks list
- Increment next_id
- Print confirmation message

**T5. Implement delete_task(index)**
- Validate index is numeric
- Validate index is in valid range (1 to len(tasks))
- Remove task at index-1 (1-based to 0-based conversion)
- Print confirmation message
- Note: IDs remain unchanged (no renumbering)

**T6. Implement update_task(index, new_description)**
- Validate index is numeric and in range
- Validate new_description is not empty/whitespace
- Update task's description field
- Preserve completed status
- Print confirmation message

**T7. Implement toggle_complete(index)**
- Validate index is numeric and in range
- Flip completed boolean (True <-> False)
- Print confirmation showing new status

### Phase 3: Search + Help (Tasks 8-9)

**T8. Implement search_tasks(keyword)**
- Validate keyword is not empty
- Perform case-insensitive partial match
- Use: `keyword.lower() in task["description"].lower()`
- Collect all matching tasks
- Display in same format as list (numbered)
- Handle no matches case with helpful message

**T9. Implement show_help()**
- Return formatted help text with all commands
- Include command syntax and descriptions

### Phase 4: Integration (Tasks 10-12)

**T10. Implement command dispatcher**
- Parse input line into command and args
- Support commands: add, delete, update, complete, list, search, help, quit
- Handle unknown commands with error message
- Route to appropriate handler function

**T11. Implement error handling**
- Non-numeric index input → "Error: Index must be a number."
- Out of range index → "Error: Invalid index X. Valid range: 1 to Y."
- Empty description → "Error: Task description cannot be empty."
- Empty search keyword → "Error: Search keyword cannot be empty."
- Unknown command → "Error: Unknown command 'xyz'. Type 'help' for available commands."

**T12. Implement main loop**
- Print welcome message on startup
- Print help message on startup
- Enter `while True` loop with `input("> ")`
- Exit cleanly on "quit" command with "Goodbye!"
- Handle KeyboardInterrupt (Ctrl+C) gracefully

### Phase 5: Verification (Task 13)

**T13. Manual verification checklist**
- Add inline comments for each acceptance scenario
- Create tests/verification.md with step-by-step test cases
- Document expected outputs for each command
- Verify all 8 user stories work correctly

## 6. Constitution Compliance

| Principle | Compliance | Evidence |
|-----------|------------|----------|
| Spec-First | ✓ | Implementation follows approved spec.md |
| Clean Code | ✓ | PEP 8, meaningful names, error handling |
| Testing Discipline | ✓ | Verification checklist per user story |
| Phase Isolation | ✓ | Single file, no external dependencies |
| Output Format | ✓ | Markdown docs, fenced code blocks |

## 7. Success Criteria Validation

| Criterion | Validation Method |
|-----------|-------------------|
| SC-001: Add task appears within 5s | Manual timing check |
| SC-002: Operations complete in 1s | Performance benchmark |
| SC-003: Error messages within 1s | Manual verification |
| SC-004: 100% commands work | Full test suite execution |
| SC-005: Search finds all matches | Keyword variety tests |

## 8. Risk Analysis

| Risk | Impact | Mitigation |
|------|--------|------------|
| Input validation gaps | Medium | Comprehensive error handling in T11 |
| Large task list performance | Low | O(n) search acceptable per spec |
| Unicode/special characters | Low | UTF-8 encoding default in Python |
| User confusion on errors | Medium | Clear, actionable error messages |

## 9. Next Steps

After this plan is approved:
1. Run `/sp.tasks` to break tasks into implementation units
2. Implement tasks sequentially (T1 → T13)
3. Run `/sp.implement` for each task
4. Verify with `/sp.analyze` after completion

---

**Plan Version**: 1.0 | **Created**: 2025-12-28 | **Status**: Ready for `/sp.tasks`
