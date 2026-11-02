
import sqlite3
import os

# Get the current project folder location
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Store database inside the project folder
DATABASE_NAME = os.path.join(BASE_DIR, "students.db")


def get_db_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def create_table():
    connection = get_db_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            date_of_birth TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phone TEXT,
            course TEXT,
            address TEXT,
            enrollment_date TEXT
        )
    """)

    connection.commit()
    connection.close()
