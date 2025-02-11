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
        task_handling.add_task(args.task_name, task_handling.file_path)
    elif args.command == "update":
        task_handling.update_task(args.task_id, args.new_name, task_handling.file_path)
    elif args.command == "delete":
        if args.task_id == "all":
            task_handling.delete_all_tasks(task_handling.file_path)
        else:
            task_handling.delete_task(args.task_id, task_handling.file_path)
    elif args.command == "mark-in-progress":
        task_handling.mark_task_in_progress(args.task_id, task_handling.file_path)
    elif args.command == "mark-done":
        task_handling.mark_task_done(args.task_id, task_handling.file_path)
    elif args.command == "list":
        task_handling.list_tasks(args.option, task_handling.file_path)

if __name__ == "__main__":
    main()