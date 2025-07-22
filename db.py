# db.py

import sqlite3

def connect_db():
    return sqlite3.connect("students.db")

def create_table():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                roll TEXT UNIQUE NOT NULL,
                department TEXT,
                marks INTEGER
            )
        ''')
        conn.commit()

def insert_student(name, roll, department, marks):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (name, roll, department, marks) VALUES (?, ?, ?, ?)",
                       (name, roll, department, marks))
        conn.commit()

def get_all_students():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        return cursor.fetchall()

def search_by_roll(roll):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE roll=?", (roll,))
        return cursor.fetchone()

def update_student(roll, name, department, marks):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE students SET name=?, department=?, marks=? WHERE roll=?",
                       (name, department, marks, roll))
        conn.commit()

def delete_student(roll):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE roll=?", (roll,))
        conn.commit()
