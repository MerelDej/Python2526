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
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def get_all_user_ids():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM users")
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_all_project_ids():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM projects")
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_all_task_ids():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM tasks")
    rows = cursor.fetchall()
    conn.close()
    return rows

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

def get_next_id(table_name):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(f"SELECT MAX(id) FROM {table_name}")
    max_id = cursor.fetchone()[0]
    conn.close()
    return 1 if max_id is None else max_id + 1

def add_user(name, email):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        next_id = get_next_id("users")
        cursor.execute("INSERT INTO users (id, name, email) VALUES (?, ?, ?)", (next_id, name, email))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        print("Error: Email is already in use, use another")
        return False
    finally:
        conn.close()

def add_task(project_id, user_id, title, status, due_date):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        next_id = get_next_id("tasks")
        cursor.execute("INSERT INTO tasks (id, project_id, user_id, title, status, due_date) VALUES (?, ?, ?, ?, ?, ?)", (next_id, project_id, user_id, title, status, due_date))
        conn.commit()
        return True
    except sqlite3.IntegrityError as e:
        print("Error: add_task failed")
        print(f"Error: {e}")
        return False
    finally:
        conn.close()

def add_project(user_id, name):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        next_id = get_next_id("projects")
        cursor.execute("INSERT INTO projects (id, user_id, name) VALUES (?, ?, ?)", (next_id, user_id, name))
        conn.commit()
        return True
    except sqlite3.IntegrityError as e:
        print("Error: add_project failed")
        print(f"Error: {e}")
        return False
    finally:
        conn.close()

def update_user(user_id, new_name=None, new_email=None):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        if new_name:
            cursor.execute("UPDATE users SET name = ? WHERE id = ?", (new_name, user_id))
        if new_email:
            cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        print("Error: Email is already in use, use another")
        return False
    finally:
        conn.close()

def update_task(task_id, new_project_id=None, new_user_id=None, new_title=None, new_status=None, new_due_date=None):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        if new_project_id:
            cursor.execute("UPDATE tasks SET project_id = ? WHERE id = ?", (new_project_id, task_id))
        if new_user_id:
            cursor.execute("UPDATE tasks SET user_id = ? WHERE id = ?", (new_user_id, task_id))
        if new_title:
            cursor.execute("UPDATE tasks SET title = ? WHERE id = ?", (new_title, task_id))
        if new_status:
            cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (new_status, task_id))
        if new_due_date:
            cursor.execute("UPDATE tasks SET due_date = ? WHERE id = ?", (new_due_date, task_id))
        conn.commit()
        return True
    except sqlite3.IntegrityError as e:
        print("Error: update_task failed")
        print(f"Error: {e}")
        return False
    finally:
        conn.close()

def update_project(project_id, new_name=None):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        if new_name:
            cursor.execute("UPDATE projects SET name = ? WHERE id = ?", (new_name, project_id))
        conn.commit()
        return True
    except sqlite3.IntegrityError as e:
        print("Error: update_project failed")
        print(f"Error: {e}")
        return False
    finally:
        conn.close()

def delete_user(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

def delete_project(project_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM projects WHERE id = ?", (project_id,))
    conn.commit()
    conn.close()