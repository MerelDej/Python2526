from DbOperations import get_all_user_ids, get_all_task_ids, get_all_project_ids, fetch_all_users, fetch_all_tasks, fetch_all_projects, add_user, add_task, add_project, update_user, update_task, update_project, delete_user, delete_task, delete_project
from Report import generate_full_report, generate_filtered_report
from Enums import TaskStatus, ReportFileType
from Quit import QuitToMenu, safe_input
from datetime import datetime
import sys
import re

def id_exists(get_function, id_value):
    return any(row[0] == id_value for row in get_function())

def get_numeric_id(prompt):
    while True:
        value = safe_input(prompt)
        if value == "":
            return None
        try:
            num = int(value)
            if num <= 0:
                print("ID must be a positive integer")
                continue
            return num
        except ValueError:
            print("Id must be a valid integer.")

def command_one():
    print("Fetching all users...\n")
    fetch_all_users()
    print("All users fetched")

def command_two():
    print("Fetching all tasks...\n")
    fetch_all_tasks()
    print("All tasks fetched")

def command_three():
    print("Fetching all projects...\n")
    fetch_all_projects()
    print("All projects fetched")

def command_four():
    print("Adding a user...\nOr press q to quit\n")
    while True:
        name = safe_input("Enter a name: ")
        if not name:
            print("Name cannot be empty.")
            continue
        if not name.replace(" ", "").isalpha():
            print("Name must contain only letters.")
            continue
        break
    while True:
        email = safe_input("Enter an email: ").lower()
        EMAIL_REGEX = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
        if not email:
            print("Email cannot be empty.")
            continue
        elif not re.match(EMAIL_REGEX, email):
            print("Invalid email format.")
            continue
        if not add_user(name, email):
            continue
        else:
            print("User added")
        break

def command_five():
    print("Adding a task...\nOr press q to quit\n")
    while True:
        project_id = get_numeric_id("Enter a project_id: ")
        if project_id is None:
            print("Project id cannot be empty.")
            continue
        if not id_exists(get_all_project_ids, project_id):
            print("Error: Project with that ID does not exist.")
            continue
        break
    while True:
        user_id = get_numeric_id("Enter a user_id: ")
        if user_id is None:
            print("User id cannot be empty.")
            continue
        if not id_exists(get_all_user_ids, user_id):
            print("Error: User with that ID does not exist.")
            continue
        break
    while True:
        title = safe_input("Enter a title: ")
        if not title:
            print("Title cannot be empty.")
            continue
        break
    while True:
        status_input = safe_input("Enter status (pending/completed): ").lower()
        try:
            status = TaskStatus(status_input).value
        except ValueError:
            print("Invalid status. Use 'pending' or 'completed'.")
            continue
        break
    while True:
        due_date = safe_input("Enter a due_date (YYYY-MM-DD):")
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date. Use YYYY-MM-DD and a real calendar date.")
            continue
        break
    while True:
        if not add_task(project_id, user_id, title, status, due_date):
            print("Error: Could not add task.")
            return
        else:
            print("Task added")
        break

def command_six():
    print("Adding a project...\nOr press q to quit\n")
    while True:
        user_id = get_numeric_id("Enter a user_id: ")
        if user_id is None:
            print("User id cannot be empty.")
            continue
        if not id_exists(get_all_user_ids, user_id):
            print("Error: User with that ID does not exist.")
            continue
        break
    while True:
        name = safe_input("Enter a name: ")
        if not name:
            print("Name cannot be empty.")
            continue
        break
    while True:
        if not add_project(user_id, name):
            print("Error: Could not add project.")
            return
        else:
            print("Project added")
        break

def command_seven():
    print("Updating a user...\nOr press q to quit\n")
    while True:
        user_id = get_numeric_id("Enter the id of the user: ")
        if user_id is None:
            print("Id cannot be empty.")
            continue
        if not id_exists(get_all_user_ids, user_id):
            print("Error: User with that ID does not exist.")
            continue
        break
    new_name = safe_input("Enter a new name or press Enter to not change it: ")
    if new_name == "":
        new_name=None
    while True:
        new_email = safe_input("Enter a new email or press Enter to not change it: ").lower()
        EMAIL_REGEX = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
        if new_email == "":
            new_email=None
        elif not re.match(EMAIL_REGEX, new_email):
            print("Invalid email format.")
            continue
        elif not update_user(user_id, new_name, new_email):
            continue
        else:
            print("User updated")
        break

def command_eight():
    print("Updating a task...\nOr press q to quit\n")
    while True:
        task_id = get_numeric_id("Enter the id of the task: ")
        if task_id is None:
            print("Task id cannot be empty.")
            continue
        if not id_exists(get_all_task_ids, task_id):
            print("Error: Task with that ID does not exist.")
            continue
        break
    while True:
        new_project = safe_input("Enter a new project id or press Enter to not change it: ")
        if new_project == "":
            new_project=None
        elif new_project:
            try:
                new_project = int(new_project)
            except ValueError:
                print("Project ID must be a number")
                continue
            if not id_exists(get_all_project_ids, new_project):
                print("Invalid project ID")
                continue
        break
    while True:
        new_user = safe_input("Enter a new user id or press Enter to not change it: ")
        if new_user == "":
            new_user=None
        elif new_user:
            try:
                new_user = int(new_user)
            except ValueError:
                print("User ID must be a number")
                continue
            if not id_exists(get_all_user_ids, new_user):
                print("Invalid project ID")
                continue
        break
    new_title = safe_input("Enter a new title or press Enter to not change it: ")
    if new_title == "":
        new_title=None
    while True:
        new_status_input = safe_input("Enter a new status (pending/completed) or press Enter to skip: ").lower()
        if new_status_input == "":
            new_status = None
        else:
            try:
                new_status = TaskStatus(new_status_input).value
            except ValueError:
                print("Invalid status.")
                continue
        break
    new_due_date = safe_input("Enter a new due date or press Enter to not change it: ")
    if new_due_date == "":
        new_due_date=None
    update_task(task_id, new_project, new_user, new_title, new_status, new_due_date)
    print("Task updated")

def command_nine():
    print("Updating a project...\nOr press q to quit\n")
    while True:
        project_id = get_numeric_id("Enter the id of the project: ")
        if project_id is None:
            print("Project id cannot be empty.")
            continue
        if not id_exists(get_all_project_ids, project_id):
            print("Error: Project with that ID does not exist.")
            continue
        break
    new_name = safe_input("Enter a name or press Enter to not change it: ")
    if new_name == "":
        new_name=None
    update_project(project_id, new_name)
    print("Project updated")

def command_ten():
    print("Deleting a user...\nOr press q to quit\n")
    while True:
        user_id = get_numeric_id("Enter the id of the user you want to delete: ")
        if user_id is None:
            print("Id cannot be empty.")
            continue
        if not id_exists(get_all_user_ids, user_id):
            print("Error: User with that ID does not exist.")
            continue
        break
    while True:
        confirm = safe_input("Are you sure? (y/n): ").lower()
        if confirm == "y":
            delete_user(user_id)
            print("User deleted")
        elif confirm == "n":
            print("Cancelled.")
        else:
            print("Please type 'y' for yes or 'n' for no.")
            continue
        break

def command_eleven():
    print("Deleting a task...\nOr press q to quit\n")
    while True:
        task_id = get_numeric_id("Enter the id of the task you want to delete: ")
        if task_id is None:
            print("Id cannot be empty.")
            continue
        if not id_exists(get_all_task_ids, task_id):
            print("Error: Task with that ID does not exist.")
            continue
        break
    while True:
        confirm = safe_input("Are you sure? (y/n): ").lower()
        if confirm == "y":
            delete_task(task_id)
            print("Task deleted")
        elif confirm == "n":
            print("Cancelled.")
        else:
            print("Please type 'y' for yes or 'n' for no.")
            continue
        break

def command_twelve():
    print("Deleting a project...\nOr press q to quit\n")
    while True:
        project_id = get_numeric_id("Enter the id of the project you want to delete: ")
        if project_id is None:
            print("Id cannot be empty.")
            continue
        if not id_exists(get_all_project_ids, project_id):
            print("Error: Project with that ID does not exist.")
            continue
        break
    while True:
        confirm = safe_input("Are you sure? (y/n): ").lower()
        if confirm == "y":
            delete_project(project_id)
            print("Project deleted")
        elif confirm == "n":
            print("Cancelled.")
        else:
            print("Please type 'y' for yes or 'n' for no.")
            continue
        break

def command_thirteen():
    print("Generating full report...\nOr press q to quit\n")
    while True:
        options = "/".join(t.value for t in ReportFileType)
        file_type_input = safe_input(f"Enter file type ({options}): ").lower()
        try:
            file_type = ReportFileType(file_type_input).value
        except ValueError:
            print("Invalid file type. Choose 'csv' or 'excel'.")
            continue
        break
    generate_full_report(file_type)

def command_fourteen():
    print("Generating filtered report...\nOr press q to quit\n")
    while True:
        options = "/".join(t.value for t in ReportFileType)
        file_type_input = safe_input(f"Enter file type ({options}): ").lower()
        try:
            file_type = ReportFileType(file_type_input).value
        except ValueError:
            print("Invalid file type. Choose 'csv' or 'excel'.")
            continue
        break
    project_id = get_numeric_id("Enter project ID or press Enter to skip: ")
    user_id = get_numeric_id("Enter user ID or press Enter to skip: ") 
    while True:
        status_input = safe_input("Enter task status or press Enter to skip: ")
        try:
            if status_input == "":
                status = None
                break
            else:
                status = TaskStatus(status_input).value
                break
        except ValueError:
                print("Invalid status. Use 'pending' or 'completed'.")
                continue
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
        choice = input("\nSelect an option: ")
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