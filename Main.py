from DbOperations import fetch_all_users, fetch_all_tasks, fetch_all_projects, add_user, add_task, add_project, update_user, update_task, update_project, delete_user, delete_task, delete_project
from Report import generate_full_report, generate_filtered_report
from Enums import TaskStatus, ReportFileType
from Quit import QuitToMenu, safe_input
import sys

def id_exists(fetch_function, id_value):
    while True:
        records = fetch_function()
        return any(row[0] == id_value for row in records)

def get_numeric_id(prompt):
    while True:
        value = safe_input(prompt).strip()
        if not value:
            print("Id cannot be empty.")
            return None
        if not value.isdigit():
            print("Id must be a number.")
            return None
        return int(value)

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
        name = safe_input("Enter a name: ").strip()
        if not name:
            print("Name cannot be empty.")
            continue
        break
    while True:
        email = safe_input("Enter an email: ").strip()
        if not email:
            print("Email cannot be empty.")
            continue
        elif "@" not in email or "." not in email:
            print("Invalid email. Email must contain '@' and '.'.")
            continue
        break
    add_user(name, email)
    print("User added")

def command_five():
    print("Adding a task...\nOr press q to quit\n")
    while True:
        project_id = safe_input("Enter a project_id: ").strip()
        if not project_id:
            print("Project id cannot be empty.")
            continue
        break
    while True:
        user_id = safe_input("Enter a user_id: ").strip()
        if not user_id:
            print("User id cannot be empty.")
            continue
        break
    while True:
        title = safe_input("Enter a title: ").strip()
        if not title:
            print("Title cannot be empty.")
            continue
        break
    while True:
        status_input = safe_input("Enter status (pending/completed): ").strip().lower()
        try:
            status = TaskStatus(status_input).value
        except ValueError:
            print("Invalid status. Use 'pending' or 'completed'.")
            continue
        break
    while True:
        due_date = safe_input("Enter a due_date: ").strip()
        if not due_date:
            print("Due date cannot be empty.")
            continue
        break
    add_task(project_id, user_id, title, status, due_date)
    print("Task added")

def command_six():
    print("Adding a project...\nOr press q to quit\n")
    while True:
        user_id = get_numeric_id("Enter a user_id: ").strip()
        if not user_id:
            print("User id cannot be empty.")
            continue
        break
    while True:
        name = safe_input("Enter a name: ").strip()
        if not name:
            print("Name cannot be empty.")
            continue
        break
    add_project(user_id, name)
    print("Project added")

def command_seven():
    print("Updating a user...\nOr press q to quit\n")
    while True:
        id = get_numeric_id("Enter the id of the user: ").strip()
        if id is None:
            print("Id cannot be empty.")
            continue
        if not id_exists(fetch_all_users, id):
            print("Error: User with that ID does not exist.")
            continue
        break
    new_name = safe_input("Enter a new name or press Enter to not change it: ").strip()
    if new_name == "":
        new_name=None
    while True:
        new_email = safe_input("Enter a new email or press Enter to not change it: ").strip()
        if new_email == "":
            new_email=None
        elif "@" not in new_email or "." not in new_email:
            print("Invalid email. Email must contain '@' and '.'.")
            continue
        break
    update_user(id, new_name, new_email)
    print("User updated")

def command_eight():
    print("Updating a task...\nOr press q to quit\n")
    while True:
        id = get_numeric_id("Enter the id of the task: ").strip()
        if id is None:
            print("Task id cannot be empty.")
            continue
        if not id_exists(fetch_all_tasks, id):
            print("Error: Task with that ID does not exist.")
            continue
        break
    new_project = safe_input("Enter a new project id or press Enter to not change it: ").strip()
    if new_project == "":
        new_project=None
    new_user = safe_input("Enter a new user id or press Enter to not change it: ").strip()
    if new_user == "":
        new_user=None
    new_title = safe_input("Enter a new title or press Enter to not change it: ").strip()
    if new_title == "":
        new_title=None
    while True:
        new_status_input = safe_input("Enter a new status (pending/completed) or press Enter to skip: ").strip().lower()
        if new_status_input == "":
            new_status = None
        else:
            try:
                new_status = TaskStatus(new_status_input).value
            except ValueError:
                print("Invalid status.")
                continue
        break
    new_due_date = safe_input("Enter a new due date or press Enter to not change it: ").strip()
    if new_due_date == "":
        new_due_date=None
    update_task(id, new_project, new_user, new_title, new_status, new_due_date)
    print("Task updated")

def command_nine():
    print("Updating a project...\nOr press q to quit\n")
    while True:
        id = get_numeric_id("Enter the id of the project: ").strip()
        if id is None:
            print("Project id cannot be empty.")
            continue
        if not id_exists(fetch_all_projects, id):
            print("Error: Project with that ID does not exist.")
            continue
        break
    new_name = safe_input("Enter a name or press Enter to not change it: ").strip()
    if new_name == "":
        new_name=None
    update_project(id, new_name)
    print("Project updated")

def command_ten():
    print("Deleting a user...\nOr press q to quit\n")
    while True:
        id = get_numeric_id("Enter the id of the user you want to delete: ").strip()
        if id is None:
            print("Id cannot be empty.")
            continue
        if not id_exists(fetch_all_users, id):
            print("Error: User with that ID does not exist.")
            continue
        break
    delete_user(id)
    print("User deleted")

def command_eleven():
    print("Deleting a task...\nOr press q to quit\n")
    while True:
        id = get_numeric_id("Enter the id of the task you want to delete: ").strip()
        if id is None:
            print("Id cannot be empty.")
            continue
        if not id_exists(fetch_all_tasks, id):
            print("Error: Task with that ID does not exist.")
            continue
        break
    delete_task(id)
    print("Task deleted")

def command_twelve():
    print("Deleting a project...\nOr press q to quit\n")
    while True:
        id = get_numeric_id("Enter the id of the project you want to delete: ").strip()
        if id is None:
            print("Id cannot be empty.")
            continue
        if not id_exists(fetch_all_projects, id):
            print("Error: Project with that ID does not exist.")
            continue
        break
    delete_project(id)
    print("Project deleted")

def command_thirteen():
    print("Generating full report...\nOr press q to quit\n")
    while True:
        options = "/".join(t.value for t in ReportFileType)
        file_type_input = safe_input(f"Enter file type ({options}): ").strip().lower()
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
        file_type_input = safe_input(f"Enter file type ({options}): ").strip().lower()
        try:
            file_type = ReportFileType(file_type_input).value
        except ValueError:
            print("Invalid file type. Choose 'csv' or 'excel'.")
            continue
        break
    project_id = get_numeric_id("Enter project ID or press Enter to skip: ").strip()
    if project_id == "":
        project_id = None
    user_id = get_numeric_id("Enter user ID or press Enter to skip: ").strip()
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