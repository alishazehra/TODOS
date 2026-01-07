# Verification Checklist: Phase 1 Todo Console Application

**Purpose**: Manual test cases for all 8 user stories
**Created**: 2025-12-28
**Feature**: [spec.md](../spec.md)

## Quick Start

Run the application:
```bash
cd phase1
python todo.py
```

Exit with `quit` or Ctrl+C.

---

## User Story 1: Add Tasks (Priority: P1)

### Test 1.1: Add valid task
```
> add Buy milk and eggs
```
**Expected Output**: `Task added: Buy milk and eggs (ID: 1)`

### Test 1.2: Verify task ID auto-increment
```
> add Finish report
```
**Expected Output**: `Task added: Finish report (ID: 2)`

### Test 1.3: Reject empty description
```
> add
```
**Expected Output**: `Error: Task description cannot be empty.`

### Test 1.4: Reject whitespace-only
```
> add
```
**Expected Output**: `Error: Task description cannot be empty.`

---

## User Story 2: Delete Tasks (Priority: P1)

### Test 2.1: Delete existing task
```
> list
> delete 1
```
**Expected Output**: `Task 1 deleted.`

### Test 2.2: Verify IDs unchanged after delete
```
> add Task A
> add Task B
> delete 1
> list
```
**Expected Output**: Task B should have ID 2 (not renumbered to ID 1)

### Test 2.3: Reject invalid index (non-numeric)
```
> delete abc
```
**Expected Output**: `Error: Index must be a number.`

### Test 2.4: Reject out-of-range index
```
> delete 999
```
**Expected Output**: `Error: Invalid index 999. Valid range: 1 to [current_count].`

---

## User Story 3: Update Tasks (Priority: P1)

### Test 3.1: Update task description
```
> add Original description
> update 1 New description
```
**Expected Output**: `Task 1 updated.`

### Test 3.2: Verify completion status preserved
```
> add Buy milk
> complete 1
> update 1 Buy eggs
> list
```
**Expected Output**: Task should show `[x] Buy eggs` (status preserved)

### Test 3.3: Reject empty update
```
> update 1
```
**Expected Output**: `Error: Task description cannot be empty.`

### Test 3.4: Reject out-of-range index
```
> update 999 New desc
```
**Expected Output**: `Error: Invalid index 999. Valid range: 1 to [current_count].`

---

## User Story 4: View Task List (Priority: P1)

### Test 4.1: Empty list message
```
> list
```
**Expected Output**: `No tasks yet. Add one with 'add <description>'.`

### Test 4.2: List with multiple tasks
```
> add Task 1
> add Task 2
> add Task 3
> list
```
**Expected Output**:
```
1. [ ] Task 1
2. [ ] Task 2
3. [ ] Task 3
```

### Test 4.3: List with mixed completion status
```
> add Buy milk
> add Call mom
> complete 2
> list
```
**Expected Output**:
```
1. [ ] Buy milk
2. [x] Call mom
```

---

## User Story 5: Toggle Task Completion (Priority: P1)

### Test 5.1: Mark task as complete
```
> add New task
> complete 1
> list
```
**Expected Output**: Task shows `[x]` after toggle

### Test 5.2: Toggle complete back to incomplete
```
> complete 1
> list
```
**Expected Output**: Task shows `[ ]` after second toggle

### Test 5.3: Reject invalid index
```
> complete abc
```
**Expected Output**: `Error: Index must be a number.`

### Test 5.4: Reject out-of-range index
```
> complete 999
```
**Expected Output**: `Error: Invalid index 999. Valid range: 1 to [current_count].`

---

## User Story 6: Search Tasks (Priority: P2)

### Test 6.1: Find matching tasks (case-insensitive)
```
> add Buy milk
> add Buy eggs
> add Clean house
> search buy
```
**Expected Output**:
```
1. [ ] Buy milk
2. [ ] Buy eggs
```

### Test 6.2: Handle no matches
```
> search xyz
```
**Expected Output**: `No tasks found matching 'xyz'.`

### Test 6.3: Reject empty search
```
> search
```
**Expected Output**: `Error: Search keyword cannot be empty.`

### Test 6.4: Search preserves completion status
```
> add Buy milk
> complete 1
> search milk
```
**Expected Output**: `1. [x] Buy milk` (shows completion status)

---

## User Story 7: Help Command (Priority: P3)

### Test 7.1: Display help
```
> help
```
**Expected Output**: Shows all 8 commands with descriptions

---

## User Story 8: Quit Application (Priority: P3)

### Test 8.1: Quit with message
```
> quit
```
**Expected Output**: `Goodbye!` and application exits

---

## Edge Cases

### Empty List Operations
| Command | Expected |
|---------|----------|
| `delete 1` (empty list) | Error: Invalid index 1. Valid range: 1 to 0 |
| `complete 1` (empty list) | Error: Invalid index 1. Valid range: 1 to 0 |
| `update 1 new` (empty list) | Error: Invalid index 1. Valid range: 1 to 0 |
| `search milk` (empty list) | No tasks found matching 'milk' |

### Unknown Command
```
> unknowncmd
```
**Expected Output**: `Error: Unknown command 'unknowncmd'. Type 'help' for available commands.`

### Extra Whitespace in Commands
| Command | Expected |
|---------|----------|
| `  add   task  ` | Works (stripped) |
| `delete   1  ` | Works (stripped) |

### Unicode/Special Characters
```
> add Привет мир
> add 你好世界
> add Task with "quotes" and 'apostrophes'
> list
```
**Expected Output**: All special characters handled correctly

---

## Performance Tests

### SC-002: Operations complete within 1 second
- Each command should complete instantly (< 1s)
- No noticeable delay between command and output

### SC-003: Error messages within 1 second
- Invalid input should show error immediately

---

## Verification Summary

| User Story | Tests | Status |
|------------|-------|--------|
| US1: Add Tasks | 4 | [ ] |
| US2: Delete Tasks | 4 | [ ] |
| US3: Update Tasks | 4 | [ ] |
| US4: List Tasks | 3 | [ ] |
| US5: Toggle Complete | 4 | [ ] |
| US6: Search Tasks | 4 | [ ] |
| US7: Help | 1 | [ ] |
| US8: Quit | 1 | [ ] |
| Edge Cases | 5 | [ ] |
| Performance | 2 | [ ] |

**Total: 32 tests**

---

## Notes

- All tests are manual console verification (per spec requirements)
- No automated unit tests required for Phase 1
- Focus on user-facing behavior and error messages
