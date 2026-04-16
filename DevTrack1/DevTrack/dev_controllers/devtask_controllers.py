from datetime import datetime
# from database.devtrack_db import task_list
from dev_controllers.devtask_json_controllers import (
    load_tasks, save_tasks
)

task_list = load_tasks()

def create_task():
    task_name = input("Please enter task details: ")
    priority = input("Please enter priority: ")
    deadline = input("Please enter deadline (YYYY-MM-DD): ")


    task = {
        "task_id": len(task_list)+1,
        "task": task_name,
        "priority": priority,
        "deadline": deadline,
        "status": "Pending",
        "date_created":  datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    }

    task_list.append(task)
    save_tasks(task_list)
    print("Task added successfully!")



def view_task():
    if not task_list:
        print("No task found.")
        return

    for task in task_list:
        if not isinstance(task, dict):
            print("Invalid task data found, skipping:", task)
            continue

        print(
            f"\nTask_ID: {task['task_id']}"
            f"\n Task: {task['task']}"
            f"\n Priority: {task['priority']}"
            f"\n Deadline: {task['deadline']}"
            f"\n Status: {task['status']}"
            f"\n Date Created: {task['date_created']}"
        )
        print("-------------------------------------")


def update_task():
    if not task_list:
        print("No task found.")
        return

    task_id = int(input("Enter the task id to update: "))

    for task in task_list:
        if task["task_id"] == task_id:
            task["task"] = input("Enter new task name: ")
            task["priority"] = input("Enter new priority: ")
            task["deadline"] = input("Enter new deadline (YYYY-MM-DD): ")
            task["status"] = input("Enter new status: ")
            print("Task updated successfully!")
            return

    print("Task ID not found.")


def delete_task():
    if not task_list:
        print("No tasks found.")
        return

    task_id = int(input("Enter the task id to delete: "))

    for task in task_list:
        if task["task_id"] == task_id:
            task_list.remove(task)
            print("Task deleted successfully!")
            return

    print("Task ID not found.")

def status_task():
    if not task_list:
        print("No tasks available.")
        return

    print("\nFilter Tasks by Status")
    print("1. Completed")
    print("2. Pending")
    print("3. In Progress")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        status_name = "Completed"
    elif choice == "2":
        status_name = "Pending"
    elif choice == "3":
        status_name = "In Progress"
    else:
        print("Invalid choice.")
        return

    filtered_tasks = list(
        filter(lambda task: task["status"].lower() == status_name.lower(), task_list)
    )

    if not filtered_tasks:
        print(f"No tasks found with status: {status_name}")
    else:
        for task in filtered_tasks:
            print_task(task)

def print_task(task):
    print("-------------------------------")
    print(f"Task ID   : {task['Task_id']}")
    print(f"Deadline  : {task['Deadline']}")
    print(f"Status    : {task['status']}")
    
