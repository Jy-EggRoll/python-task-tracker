# Task Tracker

Build a CLI app to track your tasks and manage your to-do list.

This is a simple project for improving my Python skill.

The project URL is <https://roadmap.sh/projects/task-tracker>.

## Phase 1

### What to Learn

1. Python Basic Syntax
2. Command-Line Arguments Handling
3. JSON(JavaScript Objective Notation)
4. Date handling
5. Error handling

## Phase 2

Now that the project is basically accomplished, I will improve it.

In this phase, I will:

1. Fix bugs
2. Generate Release

## Usage Instruction for Task Tracker CLI

### Overview

This is a Command-Line Interface (CLI) for a task tracker. It allows you to manage tasks, including adding, updating, deleting, marking status, and listing tasks. The CLI is packaged as an executable file named `python-task-tracker-cli.exe`.

### Commands

1. **Version**:
    - **Command**: `python-task-tracker-cli version`
    - **Function**: Show the current version of the task tracker. The version is `2025-02-11`.

2. **Time**:
    - **Command**: `python-task-tracker-cli time`
    - **Function**: Display the current date and time.

3. **Add Task**:
    - **Command**: `python-task-tracker-cli add "Task description"`
    - **Function**: Add a new task with the given description. A unique ID will be assigned to the task.

4. **Update Task**:
    - **Command**: `python-task-tracker-cli update task_id "New task description"`
    - **Function**: Update the description of an existing task with the given ID.

5. **Delete Task**:
    - **Delete a single task**: `python-task-tracker-cli delete task_id`
    - **Delete all tasks**: `python-task-tracker-cli delete all`
    - **Function**: Delete a specific task by ID or all tasks.

6. **Mark Task Status**:
    - **Mark as in progress**: `python-task-tracker-cli mark-in-progress task_id`
    - **Mark as done**: `python-task-tracker-cli mark-done task_id`
    - **Function**: Change the status of a task to "in-progress" or "done".

7. **List Tasks**:
    - **List all tasks**: `python-task-tracker-cli list` or `python-task-tracker-cli list all`
    - **List specific tasks**: `python-task-tracker-cli list done`, `python-task-tracker-cli list todo`, `python-task-tracker-cli list in-progress`
    - **Function**: List tasks according to the given option.

### Note

- Task data is stored in `userdata/taskdata.json`. If the directory does not exist, it will be created automatically.
- If no command is provided, the version of the task tracker will be shown.
- This program has added support for CJK characters. However, there will be a width mismatch issue in the output, so the display is not ideal.
- This program is only for Windows. Adding or not adding `.exe` after the command has no effect; they are equivalent.
- This program is a personal learning project. There are bound to be many deficiencies, so please forgive me!
