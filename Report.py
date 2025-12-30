import pandas as pd
import sqlite3
import os
from Database.Settings import DB_PATH
from datetime import datetime

def generate_full_report(file_type):
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    conn = sqlite3.connect(DB_PATH)
    query = """
    SELECT 
        users.name AS User,
        projects.name AS Project,
        tasks.title AS Task,
        tasks.status AS Status,
        tasks.due_date AS DueDate
    FROM tasks
    JOIN users ON tasks.user_id = users.id
    JOIN projects ON tasks.project_id = projects.id
    """
    df = pd.read_sql_query(query, conn)
    conn.close()

    try:
        os.mkdir("reports")
        print("Directory 'reports' created successfully.")
    except FileExistsError:
        print("Directory 'reports' already exists.")

    filename = f"reports/full_report_{now}"
    if file_type == "csv":
        df.to_csv(f"{filename}.csv", index=False)
        print(f"Full report generated: {filename}.csv")
    elif file_type == "excel":
        df.to_excel(f"{filename}.xlsx", index=False)
        print(f"Full report generated: {filename}.xlsx")

def generate_filtered_report(file_type, project_id=None, user_id=None, status=None):
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    conn = sqlite3.connect(DB_PATH)
    query = """
    SELECT 
        users.name AS User,
        projects.name AS Project,
        tasks.title AS Task,
        tasks.status AS Status,
        tasks.due_date AS DueDate
    FROM tasks
    JOIN users ON tasks.user_id = users.id
    JOIN projects ON tasks.project_id = projects.id
    WHERE 1=1
    """
    params = []

    if project_id is not None:
        query += " AND tasks.project_id = ?"
        params.append(project_id)
    if user_id is not None:
        query += " AND tasks.user_id = ?"
        params.append(user_id)
    if status is not None:
        query += " AND tasks.status = ?"
        params.append(status)

    df = pd.read_sql_query(query, conn, params=params)
    conn.close()

    if file_type and not df.empty:
        try:
            os.mkdir("reports")
            print("Directory 'reports' created successfully.")
        except FileExistsError:
            print("Directory 'reports' already exists.")

        filename = f"reports/filtered_report_{now}"
        if file_type.lower() == "csv":
            df.to_csv(f"{filename}.csv", index=False)
            print(f"Filtered report generated: {filename}.csv")
        elif file_type.lower() == "excel":
            df.to_excel(f"{filename}.xlsx", index=False)
            print(f"Filtered report generated: {filename}.xlsx")
    return df