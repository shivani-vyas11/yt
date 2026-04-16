from dev_controllers.devtask_controllers import (
    create_task, view_task, update_task, delete_task
)
from constants.task_constants import (
    CREATE_TASK, VIEW_TASK, UPDATE_TASK, DELETE_TASK, EXIT
)

def dev_task_ui():

    while True:
        print("Welcome to Developer Tracking System")
        print("1- Add a task")
        print("2- View a task")
        print("3- Update a task")
        print("4- Delete a task")
        print("5- Exit")
        
        user_choice = input("Please enter your choice: ")

        if user_choice == CREATE_TASK:
            create_task()
        elif user_choice == VIEW_TASK:
            view_task()
        elif user_choice == UPDATE_TASK:
            update_task()
        elif user_choice == DELETE_TASK:
            delete_task()
        elif user_choice == EXIT:
            print("Exiting DevTrack.")
            break
        else:
            break