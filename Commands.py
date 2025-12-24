import argparse
from DbOperations import fetch_all_users, fetch_all_tasks, fetch_all_projects, add_user, add_task, add_project, update_user, update_task, update_project, delete_user, delete_task, delete_project
from Report import generate_full_report, generate_filtered_report

def parse_args():
    parser = argparse.ArgumentParser(description="CLI Database Manager")
    subparsers = parser.add_subparsers(dest="command")

    # Add user
    add_user_parser = subparsers.add_parser("add-user")
    add_user_parser.add_argument("--name", required=True, help="Name of the user")
    add_user_parser.add_argument("--email", required=True, help="Email of the user")

    # Add task
    add_task_parser = subparsers.add_parser("add-task")
    add_task_parser.add_argument("--project-id", required=True, type=int, help="Project ID")
    add_task_parser.add_argument("--user-id", required=True, type=int, help="User ID")
    add_task_parser.add_argument("--title", required=True, help="Task title")
    add_task_parser.add_argument("--status", default="pending", help="Task status")
    add_task_parser.add_argument("--due-date", help="Due date (YYYY-MM-DD)")

    # Add project
    add_project_parser = subparsers.add_parser("add-project")
    add_project_parser.add_argument("--user-id", required=True, type=int, help="User ID")
    add_project_parser.add_argument("--name", required=True, help="Project name")

    # Update user
    update_user_parser = subparsers.add_parser("update-user")
    update_user_parser.add_argument("--id", required=True, type=int, help="ID of the user")
    update_user_parser.add_argument("--name", help="New name of the user")
    update_user_parser.add_argument("--email", help="New email of the user")

    # Update task
    update_task_parser = subparsers.add_parser("update-task")
    update_task_parser.add_argument("--id", required=True, type=int, help="Task ID")
    update_task_parser.add_argument("--project-id", type=int)
    update_task_parser.add_argument("--user-id", type=int)
    update_task_parser.add_argument("--title")
    update_task_parser.add_argument("--status")
    update_task_parser.add_argument("--due-date")

    # Update project
    update_project_parser = subparsers.add_parser("update-project")
    update_project_parser.add_argument("--id", required=True, type=int)
    update_project_parser.add_argument("--name")

    # Delete commands
    subparsers.add_parser("list-users")
    subparsers.add_parser("list-tasks")
    subparsers.add_parser("list-projects")
    delete_user_parser = subparsers.add_parser("delete-user")
    delete_user_parser.add_argument("--id", required=True, type=int)
    delete_task_parser = subparsers.add_parser("delete-task")
    delete_task_parser.add_argument("--id", required=True, type=int)
    delete_project_parser = subparsers.add_parser("delete-project")
    delete_project_parser.add_argument("--id", required=True, type=int)

    # Generate full report
    report_parser = subparsers.add_parser("generate-full-report")
    report_parser.add_argument("--file-type", required=True, choices=["csv", "excel"], help="Report type")

    # Generate filtered report
    report_parser = subparsers.add_parser("generate-filtered-report")
    report_parser.add_argument("--file-type", required=True, choices=["csv", "excel"], help="Report type")
    report_parser.add_argument("--project-id", type=int)
    report_parser.add_argument("--user-id", type=int)
    report_parser.add_argument("--status")

    args = parser.parse_args()

    # Execute corresponding function
    if args.command == "add-user":
        add_user(args.name, args.email)
    elif args.command == "add-task":
        add_task(args.project_id, args.user_id, args.title, args.status, args.due_date)
    elif args.command == "add-project":
        add_project(args.user_id, args.name)
    elif args.command == "update-user":
        update_user(args.id, args.name, args.email)
    elif args.command == "update-task":
        update_task(args.id, args.project_id, args.user_id, args.title, args.status, args.due_date)
    elif args.command == "update-project":
        update_project(args.id, args.name)
    elif args.command == "list-users":
        users = fetch_all_users()
        for u in users:
            print(u)
    elif args.command == "list-tasks":
        tasks = fetch_all_tasks()
        for t in tasks:
            print(t)
    elif args.command == "delete-user":
        delete_user(args.id)
    elif args.command == "delete-task":
        delete_task(args.id)
    elif args.command == "delete-project":
        delete_project(args.id)
    elif args.command == "generate-full-report":
        generate_full_report(args.file_type)
    elif args.command == "generate-filtered-report":
        generate_filtered_report(
            args.file_type,
            project_id=args.project_id,
            user_id=args.user_id,
            status=args.status
        )
    else:
        parser.print_help()

def execute_command(args):
    if args.command == "add-user":
        add_user(args.name, args.email)
        print(f"User {args.name} added successfully!")
    elif args.command == "add-task":
        add_task(args.project_id, args.user_id, args.title, args.status, args.due_date)
        print(f"Task for {args.title} added successfully!")
    elif args.command == "add-project":
        add_project(args.user_id, args.name)
        print(f"Project for {args.name} added successfully!")
    elif args.command == "list-users":
        users = fetch_all_users()
        print("Users:")
        for user in users:
            print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")
    elif args.command == "list-tasks":
        tasks = fetch_all_tasks()
        print("Tasks:")
        for task in tasks:
            print(f"ID: {task[0]}, Project ID: {task[1]}, User ID: {task[2]}, Title: {task[3]}, Status: {task[4]}, Due date: {task[5]}")
    elif args.command == "list-projects":
        projects = fetch_all_projects()
        print("Projects:")
        for project in projects:
            print(f"ID: {project[0]}, User ID: {project[1]}, Name: {project[2]}")
    elif args.command == "update-user":
        update_user(args.id, args.name, args.email)
        print(f"User ID {args.id} updated successfully!")
    elif args.command == "update-task":
        update_task(args.id, args.project_id, args.user_id, args.title, args.status, args.due_date)
        print(f"Task ID {args.id} updated successfully!")
    elif args.command == "update-project":
        update_project(args.id, args.name)
        print(f"Project ID {args.id} updated successfully!")
    elif args.command == "generate-full-report":
        generate_full_report(args.file_type)
    elif args.command == "generate-filtered-report":
        generate_filtered_report(args.file_type, args.project_id, args.user_id, args.status)