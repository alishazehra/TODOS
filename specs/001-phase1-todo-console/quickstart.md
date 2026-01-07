# Quickstart: Phase 1 Todo Console Application

## Prerequisites

- Python 3.x installed
- No additional dependencies required

## Installation

1. Navigate to the phase1 directory:
   ```bash
   cd phase1/
   ```

2. No installation needed - the application is a single Python file.

## Running the Application

```bash
python todo.py
```

Or on Windows:
```bash
python todo.py
```

## Usage Guide

### Adding Tasks

```
> add Buy milk and eggs
Task added: Buy milk and eggs (ID: 1)
```

### Listing Tasks

```
> list
1. [ ] Buy milk and eggs
2. [ ] Call mom
3. [ ] Finish report
```

### Completing Tasks

```
> complete 1
Task 1 marked as completed.
```

### Searching Tasks

```
> search milk
1. [ ] Buy milk and eggs
```

### Getting Help

```
> help
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

### Exiting

```
> quit
Goodbye!
```

## Common Operations

| Task | Command |
|------|---------|
| Add a task | `add Buy groceries` |
| List all tasks | `list` |
| Mark task 3 done | `complete 3` |
| Remove task 2 | `delete 2` |
| Change task 1 | `update 1 Buy different item` |
| Find tasks with "milk" | `search milk` |
| Show help | `help` |
| Exit | `quit` |

## Error Messages

| Situation | Message |
|-----------|---------|
| Invalid index | `Error: Invalid index 5. Valid range: 1 to 3.` |
| Non-numeric index | `Error: Index must be a number.` |
| Empty description | `Error: Task description cannot be empty.` |
| Empty search | `Error: Search keyword cannot be empty.` |
| Unknown command | `Error: Unknown command 'xyz'. Type 'help' for available commands.` |
