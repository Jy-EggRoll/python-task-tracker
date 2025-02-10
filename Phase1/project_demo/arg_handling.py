import argparse

def arg_handling():

    parser = argparse.ArgumentParser(description="Task tracker CLI")

    subparsers = parser.add_subparsers(dest="command", title="Available commands")

    version_parser = subparsers.add_parser("version", help="Get the version")

    time_parser = subparsers.add_parser("time", help="Get the date and time")

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("task_name", help="Task name or description")

    update_parser = subparsers.add_parser("update", help="Update specific task by ID")
    update_parser.add_argument("task_id", type=int, help="Task ID to update")
    update_parser.add_argument("new_name", help="New task name or description")

    delete_parser = subparsers.add_parser("delete", help="Delete an existing task by ID")
    delete_parser.add_argument("task_id", type=int, help="Task ID to delete")

    mark_in_progress_parser = subparsers.add_parser("mark-in-progress", help="Mark a task as in progress by ID")
    mark_in_progress_parser.add_argument("task_id", type=int, help="Task ID to mark as in progress")

    mark_done_parser = subparsers.add_parser("mark-done", help="Mark a task as done by ID")
    mark_done_parser.add_argument("task_id", type=int, help="Task ID to mark as done")

    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument("status", nargs="?", default=None, choices=["done", "todo", "in-progress"], help="List specific tasks by choice (This is an optional arg)")

    args = parser.parse_args()

    return args

if __name__ == "__main__":
    arg_handling()