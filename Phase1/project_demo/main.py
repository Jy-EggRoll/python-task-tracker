import arg_handling
import variables
import time_handling
import task_handling

def main():

    args = arg_handling.arg_handling()

    if args.command is None:
        print(f"Now the version is: {variables.version}")
    elif args.command == "version":
        print(f"Now the version is: {variables.version}")
    elif args.command == "time":
        print(f"Now the date and time is: {time_handling.get_datetime()}")
    elif args.command == "add":
        task_handling.add_task(args.task_name)
    elif args.command == "update":
        task_handling.update_task(args.task_id, args.new_name)
    elif args.command == "delete":
        task_handling.delete_task(args.task_id)
    elif args.command == "mark-in-progress":
        task_handling.mark_task_in_progress(args.task_id)
    elif args.command == "mark-done":
        task_handling.mark_task_done(args.task_id)
    elif args.command == "list":
        task_handling.list_tasks(args.status)

if __name__ == "__main__":
    main()