import sqlite3
from Settings.Config import DB_PATH

def create_database():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    );
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        name TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id)
            ON DELETE CASCADE
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        status TEXT DEFAULT 'pending',
        due_date TEXT,
        FOREIGN KEY (project_id) REFERENCES projects(id)
            ON DELETE CASCADE,
        FOREIGN KEY (user_id) REFERENCES users(id)
            ON DELETE CASCADE
    );
    """)
    
    # TO DO: Maak van status een Enum met als opties "pending" of "completed"

    cursor.execute("INSERT OR IGNORE INTO users (id, name, email) VALUES (1, 'Magda', 'magda@gmail.com')")
    cursor.execute("INSERT OR IGNORE INTO users (id, name, email) VALUES (2, 'Germain', 'Germain@gmail.com')")
    cursor.execute("INSERT OR IGNORE INTO users (id, name, email) VALUES (3, 'Pieter', 'pieter@gmail.com')")
    cursor.execute("INSERT OR IGNORE INTO users (id, name, email) VALUES (4, 'Frank', 'frank@gmail.com')")
    cursor.execute("INSERT OR IGNORE INTO users (id, name, email) VALUES (5, 'Maria', 'maria@gmail.com')")
    cursor.execute("INSERT OR IGNORE INTO users (id, name, email) VALUES (6, 'Pol', 'pol@gmail.com')")

    cursor.execute("INSERT OR IGNORE INTO projects (id, user_id, name) VALUES (1, 1, 'Personal')")
    cursor.execute("INSERT OR IGNORE INTO projects (id, user_id, name) VALUES (2, 1, 'Work')")
    cursor.execute("INSERT OR IGNORE INTO projects (id, user_id, name) VALUES (3, 2, 'Home')")
    cursor.execute("INSERT OR IGNORE INTO projects (id, user_id, name) VALUES (4, 3, 'Study')")

    cursor.execute("INSERT OR IGNORE INTO tasks (id, project_id, user_id, title, status, due_date) VALUES (1, 1, 1, 'Buy groceries', 'pending', '2025-01-10')")
    cursor.execute("INSERT OR IGNORE INTO tasks (id, project_id, user_id, title, status, due_date) VALUES (2, 1, 1, 'Go running', 'completed', '2025-01-09')")
    cursor.execute("INSERT OR IGNORE INTO tasks (id, project_id, user_id, title, status, due_date) VALUES (3, 2, 1, 'Finish report', 'pending', '2025-01-15')")
    cursor.execute("INSERT OR IGNORE INTO tasks (id, project_id, user_id, title, status, due_date) VALUES (4, 3, 2, 'Fix kitchen sink', 'pending', '2025-01-12')")
    cursor.execute("INSERT OR IGNORE INTO tasks (id, project_id, user_id, title, status, due_date) VALUES (5, 2, 1, 'Prepare presentation', 'pending', '2025-01-14')")
    cursor.execute("INSERT OR IGNORE INTO tasks (id, project_id, user_id, title, status, due_date) VALUES (6, 3, 2, 'Paint bedroom', 'pending', '2025-01-20')")
    cursor.execute("INSERT OR IGNORE INTO tasks (id, project_id, user_id, title, status, due_date) VALUES (7, 4, 3, 'Read chapter 5', 'pending', '2025-01-11')")
    cursor.execute("INSERT OR IGNORE INTO tasks (id, project_id, user_id, title, status, due_date) VALUES (8, 4, 3, 'Submit assignment', 'pending', '2025-01-13')")

    connection.commit()
    connection.close()

if __name__ == "__main__":
    create_database()