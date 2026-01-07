#!/usr/bin/env python3
"""
Phase 1: Basic In-Memory Todo Console Application

A simple console-based Todo application that allows users to manage tasks
without any data persistence. Tasks are stored in memory using a list of
dictionaries and provides a command-line interface for interaction.

Features:
- Add tasks with descriptions
- Delete tasks by index
- Update task descriptions
- List all tasks with completion status
- Toggle task completion
- Search tasks by keyword
- Help and quit commands
"""

# =============================================================================
# Phase 1: Setup (T001-T002) - Global State
# =============================================================================

tasks = []  # List of task dictionaries: [{"id": int, "description": str, "completed": bool}]
next_id = 1  # Auto-incrementing ID counter starting from 1


# =============================================================================
# Phase 2: Foundational (T003-T004) - Helper Functions and Validators
# =============================================================================

def format_task(task):
    """
    Format a single task for display.

    Args:
        task: Dictionary with 'id', 'description', 'completed' keys

    Returns:
        str: Formatted task string like "1. [ ] Buy groceries"
    """
    status = "[x]" if task["completed"] else "[ ]"
    return f"{task['id']}. {status} {task['description']}"


def validate_index(index_str, tasks_list):
    """
    Validate that an index is numeric and within valid range.

    Args:
        index_str: String input from user
        tasks_list: Current list of tasks

    Returns:
        tuple: (is_valid: bool, result: int or error_message: str)
    """
    if not index_str.strip():
        return (False, "Error: Index must be a number.")

    try:
        index = int(index_str)
    except ValueError:
        return (False, "Error: Index must be a number.")

    if index < 1 or index > len(tasks_list):
        if len(tasks_list) == 0:
            return (False, "Error: Invalid index 1. Valid range: 1 to 0 (no tasks exist).")
        return (False, f"Error: Invalid index {index}. Valid range: 1 to {len(tasks_list)}.")

    return (True, index)


def validate_description(description):
    """
    Validate that a description is not empty or whitespace-only.

    Args:
        description: String input from user

    Returns:
        tuple: (is_valid: bool, result: str or error_message: str)
    """
    if not description or not description.strip():
        return (False, "Error: Task description cannot be empty.")
    return (True, description.strip())


def validate_keyword(keyword):
    """
    Validate that a search keyword is not empty or whitespace-only.

    Args:
        keyword: String input from user

    Returns:
        tuple: (is_valid: bool, result: str or error_message: str)
    """
    if not keyword or not keyword.strip():
        return (False, "Error: Search keyword cannot be empty.")
    return (True, keyword.strip())


# =============================================================================
# Phase 3: User Story 1 - Add Tasks (T005)
# =============================================================================

def add_task(description):
    """
    Add a new task to the task list.

    Args:
        description: The task description string
    """
    is_valid, result = validate_description(description)
    if not is_valid:
        print(result)
        return

    global next_id
    task = {
        "id": next_id,
        "description": result,
        "completed": False
    }
    tasks.append(task)
    next_id += 1
    print(f"Task added: {task['description']} (ID: {task['id']})")


# =============================================================================
# Phase 4: User Story 2 - Delete Tasks (T006)
# =============================================================================

def delete_task(index_str):
    """
    Delete a task by its 1-based index.

    Args:
        index_str: String representation of the task index
    """
    is_valid, result = validate_index(index_str, tasks)
    if not is_valid:
        print(result)
        return

    index = result - 1  # Convert 1-based to 0-based
    deleted_task = tasks.pop(index)
    print(f"Task {deleted_task['id']} deleted.")


# =============================================================================
# Phase 5: User Story 3 - Update Tasks (T007)
# =============================================================================

def update_task(index_str, new_description):
    """
    Update a task's description by its 1-based index.

    Args:
        index_str: String representation of the task index
        new_description: The new description for the task
    """
    is_valid, result = validate_index(index_str, tasks)
    if not is_valid:
        print(result)
        return

    index = result - 1  # Convert 1-based to 0-based

    is_valid_desc, desc_result = validate_description(new_description)
    if not is_valid_desc:
        print(desc_result)
        return

    task = tasks[index]
    task["description"] = desc_result
    print(f"Task {task['id']} updated.")


# =============================================================================
# Phase 6: User Story 4 - List Tasks (T008)
# =============================================================================

def list_tasks():
    """
    Display all tasks with their completion status.
    """
    if len(tasks) == 0:
        print("No tasks yet. Add one with 'add <description>'.")
        return

    for task in tasks:
        print(format_task(task))


# =============================================================================
# Phase 7: User Story 5 - Toggle Complete (T009)
# =============================================================================

def toggle_complete(index_str):
    """
    Toggle a task's completion status by its 1-based index.

    Args:
        index_str: String representation of the task index
    """
    is_valid, result = validate_index(index_str, tasks)
    if not is_valid:
        print(result)
        return

    index = result - 1  # Convert 1-based to 0-based
    task = tasks[index]
    task["completed"] = not task["completed"]
    status = "completed" if task["completed"] else "uncompleted"
    print(f"Task {task['id']} marked as {status}.")


# =============================================================================
# Phase 8: User Story 6 - Search Tasks (T010)
# =============================================================================

def search_tasks(keyword):
    """
    Search for tasks by keyword (case-insensitive partial match).

    Args:
        keyword: The search keyword
    """
    is_valid, result = validate_keyword(keyword)
    if not is_valid:
        print(result)
        return

    keyword_lower = result.lower()
    matching_tasks = [
        task for task in tasks
        if keyword_lower in task["description"].lower()
    ]

    if len(matching_tasks) == 0:
        print(f"No tasks found matching '{result}'.")
        return

    for task in matching_tasks:
        print(format_task(task))


# =============================================================================
# Phase 9: User Story 7 - Help + User Story 8 - Quit (T011-T012)
# =============================================================================

def show_help():
    """
    Display available commands and their usage.
    """
    help_text = """Available commands:
  add <description>      - Add a new task
  delete <index>         - Delete a task by index
  update <index> <desc>  - Update a task's description
  complete <index>       - Toggle task completion
  list                   - Show all tasks
  search <keyword>       - Search tasks by keyword
  help                   - Show this message
  quit                   - Exit the application"""
    print(help_text)


def quit_app():
    """
    Exit the application.
    """
    print("Goodbye!")
    return True  # Signal to exit the main loop


# =============================================================================
# Phase 10: Polish - Command Dispatcher and Main Loop (T013-T014)
# =============================================================================

def dispatch_command(input_line):
    """
    Parse and execute a user command.

    Args:
        input_line: Raw input string from user

    Returns:
        bool: True if quit command was given, False otherwise
    """
    parts = input_line.strip().split(maxsplit=2)
    command = parts[0].lower() if parts else ""

    # Handle commands with different argument counts
    if command == "add":
        if len(parts) < 2:
            print("Error: Task description cannot be empty.")
        else:
            add_task(parts[1])
    elif command == "delete":
        if len(parts) < 2:
            print("Error: Index must be a number.")
        else:
            delete_task(parts[1])
    elif command == "update":
        if len(parts) < 3:
            print("Error: Missing arguments. Usage: update <index> <description>")
        else:
            update_task(parts[1], parts[2])
    elif command == "complete":
        if len(parts) < 2:
            print("Error: Index must be a number.")
        else:
            toggle_complete(parts[1])
    elif command == "list":
        list_tasks()
    elif command == "search":
        if len(parts) < 2:
            print("Error: Search keyword cannot be empty.")
        else:
            search_tasks(parts[1])
    elif command == "help":
        show_help()
    elif command == "quit":
        return quit_app()
    elif command == "":
        pass  # Empty input, just prompt again
    else:
        print(f"Error: Unknown command '{command}'. Type 'help' for available commands.")

    return False


def main():
    """
    Main application loop.
    """
    print("Welcome to Todo Console App!")
    show_help()

    while True:
        try:
            user_input = input("> ")
            should_exit = dispatch_command(user_input)
            if should_exit:
                break
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break


# =============================================================================
# Entry Point
# =============================================================================

if __name__ == "__main__":
    main()
