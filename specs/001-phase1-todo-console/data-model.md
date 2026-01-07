# Data Model: Phase 1 Todo Console Application

## Overview

This document describes the data structures used in the Phase 1 Todo application. All data is stored in-memory and is not persisted between sessions.

## Entities

### Task

The core entity representing a single todo item.

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `id` | Integer | 1 ≤ id ≤ ∞, unique, auto-incrementing | Unique identifier for the task |
| `description` | String | 1 ≤ length ≤ ∞, non-empty, non-whitespace-only | User-provided task text |
| `completed` | Boolean | true or false | Completion status |

### Example Task

```python
{
    "id": 1,
    "description": "Buy milk and eggs",
    "completed": False
}
```

### Completed Task Example

```python
{
    "id": 2,
    "description": "Call mom",
    "completed": True
}
```

## Global State

### Tasks List

```python
tasks: List[Dict[str, Any]] = []
```

The `tasks` list stores all Task dictionaries in insertion order. Tasks are never reordered or re-indexed after deletion.

### ID Counter

```python
next_id: int = 1
```

The `next_id` counter tracks the next available ID for new tasks. It starts at 1 and increments after each successful task creation.

## Validation Rules

| Operation | Validation | Error Message |
|-----------|------------|---------------|
| Add task | `description.strip() != ""` | "Error: Task description cannot be empty." |
| Update task | `new_description.strip() != ""` | "Error: Task description cannot be empty." |
| Search | `keyword.strip() != ""` | "Error: Search keyword cannot be empty." |
| Delete index | `isnumeric()` + `1 ≤ index ≤ len(tasks)` | "Error: Index must be a number." / "Error: Invalid index X. Valid range: 1 to Y." |

## State Transitions

### Task Lifecycle

```
┌──────────────┐
│   Created    │
│   (new task) │
└──────┬───────┘
       │ add_task()
       ▼
┌──────────────┐
│   Active     │
│  (completed=False)
└──────┬───────┘
       │ toggle_complete()
       ▼
┌──────────────┐
│   Completed  │
│  (completed=True)
└──────┬───────┘
       │ toggle_complete()
       ▼
┌──────────────┐
│   Active     │
│  (completed=False)
└──────┬───────┘
       │ delete_task()
       ▼
    (Removed)
```

### Description Updates

The `description` field can be updated at any time while the task exists. The `completed` status is preserved during description updates.

## Data Relationships

- Tasks exist independently (no parent/child relationships)
- Tasks maintain insertion order only
- No sorting, grouping, or hierarchy support in Phase 1

## Constraints

| Constraint | Enforcement |
|------------|-------------|
| ID uniqueness | Handled by `next_id` counter; IDs never reused |
| No ID renumbering | Deletions do not affect other task IDs |
| Non-empty descriptions | Validation before task creation/update |
| Boolean completion | Strict True/False (no partial states) |

## Performance Characteristics

| Operation | Time Complexity | Space Complexity |
|-----------|-----------------|------------------|
| Add task | O(1) | O(1) |
| Delete task | O(n) worst case (list shift) | O(1) |
| Update task | O(1) (direct index access) | O(1) |
| Toggle complete | O(1) (direct index access) | O(1) |
| List tasks | O(n) | O(1) |
| Search tasks | O(n) | O(1) |

*Note: For Phase 1 with expected small task lists, these complexities are acceptable.*
