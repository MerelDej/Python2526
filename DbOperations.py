import sqlite3
import os
from Database.Settings import DB_PATH


def print_table(headers, rows):
    # bereken max grootte voor elke kolom
    col_widths = []
    for i, header in enumerate(headers):
        max_data_width = max((len(str(row[i])) for row in rows), default=0)
        col_widths.append(max(len(header), max_data_width))
    # dynamische format string
    fmt = "  ".join(f"{{:<{w}}}" for w in col_widths)
    # print header
    print(fmt.format(*headers))
    print("-" * (sum(col_widths) + 2 * (len(col_widths)-1)))
    # print rows
    for row in rows:
        print(fmt.format(*row))

def connect_db():
    if not os.path.exists(DB_PATH):
        raise FileNotFoundError(f"Database not found at path: {DB_PATH}")
    return sqlite3.connect(DB_PATH)

def fetch_all_users():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    headers = ["id", "name", "email"]
    print_table(headers, rows)

def fetch_all_tasks():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    conn.close()
    headers = ["id", "project_id", "user_id", "title", "status", "due_date"]
    print_table(headers, rows)

def fetch_all_projects():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM projects")
    rows = cursor.fetchall()
    conn.close()
    headers = ["id", "user_id", "name"]
    print_table(headers, rows)

def add_user(name, email):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()

def add_task(project_id, user_id, title, status, due_date):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (project_id, user_id, title, status, due_date) VALUES (?, ?, ?, ?, ?)", (project_id, user_id, title, status, due_date))
    conn.commit()
    conn.close()

def add_project(user_id, name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO projects (user_id, name) VALUES (?, ?)", (user_id, name))
    conn.commit()
    conn.close()

def update_user(id, new_name=None, new_email=None):
    conn = connect_db()
    cursor = conn.cursor()
    if new_name:
        cursor.execute("UPDATE users SET name = ? WHERE id = ?", (new_name, id))
    if new_email:
        cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, id))
    conn.commit()
    conn.close()

def update_task(id, new_project_id=None, new_user_id=None, new_title=None, new_status=None, new_due_date=None):
    conn = connect_db()
    cursor = conn.cursor()
    if new_project_id:
        cursor.execute("UPDATE tasks SET project_id = ? WHERE id = ?", (new_project_id, id))
    if new_user_id:
        cursor.execute("UPDATE tasks SET user_id = ? WHERE id = ?", (new_user_id, id))
    if new_title:
        cursor.execute("UPDATE tasks SET title = ? WHERE id = ?", (new_title, id))
    if new_status:
        cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (new_status, id))
    if new_due_date:
        cursor.execute("UPDATE tasks SET due_date = ? WHERE id = ?", (new_due_date, id))
    conn.commit()
    conn.close()

def update_project(id, new_name=None):
    conn = connect_db()
    cursor = conn.cursor()
    if new_name:
        cursor.execute("UPDATE projects SET name = ? WHERE id = ?", (new_name, id))
    conn.commit()
    conn.close()

def delete_user(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (id))
    conn.commit()
    conn.close()

def delete_task(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (id))
    conn.commit()
    conn.close()

def delete_project(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM projects WHERE id = ?", (id))
    conn.commit()
    conn.close()