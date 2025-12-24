#from Commands import parse_args, execute_command
from DbOperations import fetch_all_users, fetch_all_tasks, fetch_all_projects, add_user, add_task, add_project, update_user, update_task, update_project, delete_user, delete_task, delete_project
from Report import generate_full_report, generate_filtered_report
import sys
import os

def command_one():
    print("Fetching all users...\n")
    fetch_all_users()
    os.system("echo All users fetched")

def command_two():
    print("Fetching all tasks...\n")
    fetch_all_tasks()
    os.system("echo All tasks fetched")

def command_three():
    print("Fetching all projects...\n")
    fetch_all_projects()
    os.system("echo All projects fetched")

def command_four():
    print("Adding a user...\n")
    name = input("Enter a name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    email = input("Enter an email: ").strip()
    if not email:
        print("Email cannot be empty.")
        return
    add_user(name, email)
    os.system("echo User added")

def command_five():
    print("Adding a task...\n")
    project_id = input("Enter a project_id: ").strip()
    if not project_id:
        print("Project id cannot be empty.")
        return
    user_id = input("Enter a user_id: ").strip()
    if not user_id:
        print("User id cannot be empty.")
        return
    title = input("Enter a title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return
    status = input("Enter an status: ").strip()
    if not status:
        print("Status cannot be empty.")
        return
    due_date = input("Enter a due_date: ").strip()
    if not due_date:
        print("Due date cannot be empty.")
        return
    add_task(project_id, user_id, title, status, due_date)
    os.system("echo Task added")

def command_six():
    print("Adding a project...\n")
    user_id = input("Enter a user_id: ").strip()
    if not user_id:
        print("User id cannot be empty.")
        return
    name = input("Enter a name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    add_project(user_id, name)
    os.system("echo Project added")

def command_seven():
    print("Updating a user...\n")
    id = input("Enter the id of the user: ").strip()
    if not id:
        print("Id cannot be empty.")
        return
    new_name = input("Enter a new name or press Enter to not change it: ").strip()
    if not new_name:
        new_name=None
    new_email = input("Enter a new email or press Enter to not change it: ").strip()
    if not new_email:
        new_email=None
    update_user(new_name, new_email)
    os.system("echo User updated")

def command_eight():
    print("Updating a task...\n")
    id = input("Enter the id of the task: ").strip()
    if not id:
        print("Task id cannot be empty.")
        return
    new_project = input("Enter a new project id or press Enter to not change it: ").strip()
    if not new_project:
        new_project=None
        return new_project
    new_user = input("Enter a new user id or press Enter to not change it: ").strip()
    if not new_user:
        new_user_id=None
        return new_user_id
    new_title = input("Enter a new title or press Enter to not change it: ").strip()
    if not new_title:
        new_title=None
        return new_title
    new_status = input("Enter a new status or press Enter to not change it: ").strip()
    if not new_status:
        new_status=None
        return new_status
    new_due_date = input("Enter a new due date or press Enter to not change it: ").strip()
    if not new_due_date:
        new_due_date=None
        return new_due_date
    update_task(id, new_project, new_user, new_title, new_status, new_due_date)
    os.system("echo Task updated")

def command_nine():
    print("Updating a project...\n")
    project_id = input("Enter the id of the project: ").strip()
    if not project_id:
        print("Project id cannot be empty.")
        return
    new_name = input("Enter a name or press Enter to not change it: ").strip()
    if not new_name:
        new_name=None
        return new_name
    update_project(project_id, new_name)
    os.system("echo Project updated")

def command_ten():
    print("Deleting a user...\n")
    id = input("Enter the id of the user you want to delete: ").strip()
    if not id:
        print("Id cannot be empty.")
        return
    delete_user(id)
    os.system("echo User deleted")

def command_eleven():
    print("Deleting a task...\n")
    id = input("Enter the id of the task you want to delete: ").strip()
    if not id:
        print("Id cannot be empty.")
        return
    delete_task(id)
    os.system("echo Task deleted")

def command_twelve():
    print("Deleting a project...\n")
    id = input("Enter the id of the project you want to delete: ").strip()
    if not id:
        print("Id cannot be empty.")
        return
    delete_project(id)
    os.system("echo Project deleted")

def exit_program():
    print("Exiting program.")
    sys.exit(0)

MENU_OPTIONS = {
    "1": ("List all users", command_one),
    "2": ("List all tasks", command_two),
    "3": ("List all projects", command_three),
    "4": ("Add user", command_four),
    "5": ("Add task", command_five),
    "6": ("Add project", command_six),
    "7": ("Update user", command_seven),
    "8": ("Update task", command_eight),
    "9": ("Update project", command_nine),
    "10": ("Delete user", command_ten),
    "11": ("Delete task", command_eleven),
    "12": ("Delete project", command_twelve),
    "0": ("Exit", exit_program),
}

def show_menu():
    print("\n=== To Do List Command Menu ===")
    for key, (description, _) in MENU_OPTIONS.items():
        print(f"{key}. {description}")

def main():
    while True:
        show_menu()
        choice = input("\nSelect an option: ").strip()
        if choice in MENU_OPTIONS:
            MENU_OPTIONS[choice][1]()
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()