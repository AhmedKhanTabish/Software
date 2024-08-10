import sqlite3
from datetime import datetime, timedelta, time
import pickle
import os.path
from requests import Request
import sqlite3
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow


def init_database():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task TEXT, completed INTEGER)''')
    conn.commit()
    conn.close()

def add_task(task):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("INSERT INTO tasks (task, completed) VALUES (?, 0)", (task,))
    conn.commit()
    conn.close()

def mark_completed(task_id):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

def get_tasks():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tasks WHERE completed = 0")
    tasks = c.fetchall()
    conn.close()
    return tasks

def delete_task(task_id):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

def main():
    init_database()
    print("Welcome to the To-Do List App!")
    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. Mark task as completed")
        print("3. View tasks")
        print("4. Delete task")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            task = input("Enter your task: ")
            add_task(task)
            print("Task added!")
        elif choice == 2:
            task_id = int(input("Enter the task ID to mark as completed: "))
            mark_completed(task_id)
            print("Task marked as completed!")
        elif choice == 3:
            tasks = get_tasks()
            for task in tasks:
                print(f"{task[0]}. {task[1]}")
        elif choice == 4:
            task_id = int(input("Enter the task ID to delete: "))
            delete_task(task_id)
            print("Task deleted!")
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_calendar_service():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_    