#from Commands import parse_args, execute_command
from DbOperations import fetch_all_users, fetch_all_tasks, fetch_all_projects, add_user, add_task, add_project, update_user, update_task, update_project, delete_user, delete_task, delete_project
from Report import generate_full_report, generate_filtered_report
from Enums import TaskStatus, ReportFileType
from Quit import QuitToMenu, safe_input
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
    print("Adding a user...\nOr press q to quit\n")
    name = safe_input("Enter a name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    email = safe_input("Enter an email: ").strip()
    if not email:
        print("Email cannot be empty.")
        return
    add_user(name, email)
    os.system("echo User added")

def command_five():
    print("Adding a task...\nOr press q to quit\n")
    project_id = safe_input("Enter a project_id: ").strip()
    if not project_id:
        print("Project id cannot be empty.")
        return
    user_id = safe_input("Enter a user_id: ").strip()
    if not user_id:
        print("User id cannot be empty.")
        return
    title = safe_input("Enter a title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return
    status_input = safe_input("Enter status (pending/completed): ").strip().lower()
    try:
        status = TaskStatus(status_input).value
    except ValueError:
        print("Invalid status. Use 'pending' or 'completed'.")
        return
    due_date = safe_input("Enter a due_date: ").strip()
    if not due_date:
        print("Due date cannot be empty.")
        return
    add_task(project_id, user_id, title, status, due_date)
    os.system("echo Task added")

def command_six():
    print("Adding a project...\nOr press q to quit\n")
    user_id = safe_input("Enter a user_id: ").strip()
    if not user_id:
        print("User id cannot be empty.")
        return
    name = safe_input("Enter a name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    add_project(user_id, name)
    os.system("echo Project added")

def command_seven():
    print("Updating a user...\nOr press q to quit\n")
    id = safe_input("Enter the id of the user: ").strip()
    if not id:
        print("Id cannot be empty.")
        return
    new_name = safe_input("Enter a new name or press Enter to not change it: ").strip()
    if new_name == "":
        new_name=None
    new_email = safe_input("Enter a new email or press Enter to not change it: ").strip()
    if new_email == "":
        new_email=None
    update_user(id, new_name, new_email)
    os.system("echo User updated")

def command_eight():
    print("Updating a task...\nOr press q to quit\n")
    id = safe_input("Enter the id of the task: ").strip()
    if not id:
        print("Task id cannot be empty.")
        return
    new_project = safe_input("Enter a new project id or press Enter to not change it: ").strip()
    if new_project == "":
        new_project=None
    new_user = safe_input("Enter a new user id or press Enter to not change it: ").strip()
    if new_user == "":
        new_user=None
    new_title = safe_input("Enter a new title or press Enter to not change it: ").strip()
    if new_title == "":
        new_title=None
    new_status_input = safe_input("Enter a new status (pending/completed) or press Enter to skip: ").strip().lower()
    if new_status_input == "":
        new_status = None
    else:
        try:
            new_status = TaskStatus(new_status_input).value
        except ValueError:
            print("Invalid status.")
            return
    new_due_date = safe_input("Enter a new due date or press Enter to not change it: ").strip()
    if new_due_date == "":
        new_due_date=None
    update_task(id, new_project, new_user, new_title, new_status, new_due_date)
    os.system("echo Task updated")

def command_nine():
    print("Updating a project...\nOr press q to quit\n")
    id = safe_input("Enter the id of the project: ").strip()
    if not id:
        print("Project id cannot be empty.")
        return
    new_name = safe_input("Enter a name or press Enter to not change it: ").strip()
    if new_name == "":
        new_name=None
    update_project(id, new_name)
    os.system("echo Project updated")

def command_ten():
    print("Deleting a user...\nOr press q to quit\n")
    id = safe_input("Enter the id of the user you want to delete: ").strip()
    if not id:
        print("Id cannot be empty.")
        return
    delete_user(id)
    os.system("echo User deleted")

def command_eleven():
    print("Deleting a task...\nOr press q to quit\n")
    id = safe_input("Enter the id of the task you want to delete: ").strip()
    if not id:
        print("Id cannot be empty.")
        return
    delete_task(id)
    os.system("echo Task deleted")

def command_twelve():
    print("Deleting a project...\nOr press q to quit\n")
    id = safe_input("Enter the id of the project you want to delete: ").strip()
    if not id:
        print("Id cannot be empty.")
        return
    delete_project(id)
    os.system("echo Project deleted")

def command_thirteen():
    print("Generating full report...\nOr press q to quit\n")
    options = "/".join(t.value for t in ReportFileType)
    file_type_input = safe_input(f"Enter file type ({options}): ").strip().lower()
    try:
        file_type = ReportFileType(file_type_input).value
    except ValueError:
        print("Invalid file type. Choose 'csv' or 'excel'.")
        return
    generate_full_report(file_type)

def command_fourteen():
    print("Generating filtered report...\nOr press q to quit\n")
    options = "/".join(t.value for t in ReportFileType)
    file_type_input = safe_input(f"Enter file type ({options}): ").strip().lower()
    try:
        file_type = ReportFileType(file_type_input).value
    except ValueError:
        print("Invalid file type. Choose 'csv' or 'excel'.")
        return
    project_id = safe_input("Enter project ID or press Enter to skip: ").strip()
    if project_id == "":
        project_id = None
    user_id = safe_input("Enter user ID or press Enter to skip: ").strip()
    if user_id == "":
        user_id = None
    status = safe_input("Enter task status or press Enter to skip: ").strip()
    if status == "":
        status = None
    generate_filtered_report(file_type=file_type, project_id=project_id, user_id=user_id, status=status)

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
    "13": ("Generate full report", command_thirteen),
    "14": ("Generate filtered report", command_fourteen),
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
        if choice.lower() == "q":
            exit_program()

        if choice in MENU_OPTIONS:
            try:
                MENU_OPTIONS[choice][1]()
            except QuitToMenu:
                continue
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()