import json
import time_handling
import os

file_path = "userdata/taskdata.json"

if not os.path.exists(os.path.dirname(file_path)):
    os.makedirs(os.path.dirname(file_path))

def read_tasks_from_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except:
        return []

def write_tasks_to_file(file_path, tasks):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4,  ensure_ascii=False)

def add_task(task_name, file_path):
    tasks = read_tasks_from_file(file_path)
    if tasks:
        max_id = max(task["id"] for task in tasks)
        new_id = max_id + 1
    else:
        new_id = 1
    now = time_handling.get_datetime()
    new_task = {
        "id": new_id,
        "description": task_name,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    }
    tasks.append(new_task)
    write_tasks_to_file(file_path, tasks)
    print(f"Task added successfully (ID: {new_id})")

def update_task(task_id, new_name, file_path):
    tasks = read_tasks_from_file(file_path)
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_name
            task["updatedAt"] = time_handling.get_datetime()
            write_tasks_to_file(file_path, tasks)
            print(f"Task updated successfully (ID: {task_id})")
            break
    else:
        print("Task not found")

def delete_task(task_id, file_path):
    tasks = read_tasks_from_file(file_path)
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            write_tasks_to_file(file_path, tasks)
            print(f"Task deleted successfully (ID: {task_id})")
            break
    else:
        print("Task not found")

def delete_all_tasks(file_path):
    write_tasks_to_file(file_path, [])
    print("All tasks deleted!")

def mark_task_in_progress(task_id, file_path):
    tasks = read_tasks_from_file(file_path)
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "in-progress"
            task["updatedAt"] = time_handling.get_datetime()
            write_tasks_to_file(file_path, tasks)
            print(f"Task marked in progress successfully (ID: {task_id})")
            break
    else:
        print("Task not found")

def mark_task_done(task_id, file_path):
    tasks = read_tasks_from_file(file_path)
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            task["updatedAt"] = time_handling.get_datetime()
            write_tasks_to_file(file_path, tasks)
            print(f"Task marked done successfully (ID: {task_id})")
            break
    else:
        print("Task not found")

def list_tasks(option, file_path):
    tasks = read_tasks_from_file(file_path)
    if len(tasks) == 0:
        print("No task!")
        return
    id_width = max(len(str(task["id"])) for task in tasks)
    name_width = max(len(task["description"]) for task in tasks)
    status_width = max(len(task["status"]) for task in tasks)
    
    if option == "all":
        for task in tasks:
            print(f"ID: {task['id']:<{id_width}} NAME: {task['description']:<{name_width}} STATUS: {task['status']:<{status_width}}")
    else:
        for task in tasks:
            if option == task["status"]:
                print(f"ID: {task['id']:<{id_width}} NAME: {task['description']:<{name_width}} STATUS: {task['status']:<{status_width}}")