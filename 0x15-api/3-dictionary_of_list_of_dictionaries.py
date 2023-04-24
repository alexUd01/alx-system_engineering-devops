#!/usr/bin/python3
""" Using what you did in the task #0, extend your Python script to export
data in the JSON format.

Requirements:
Records all tasks from all employees
Format must be:
{ "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME",
"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ],
"USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME",
"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}

File name must be: todo_all_employees.json
"""
from requests import get
import json

if __name__ == "__main__":
    # Fetch all employees' personal details
    r_users = get('https://jsonplaceholder.typicode.com/users/')

    # Fetch employee's todo list
    r_todos = get('https://jsonplaceholder.typicode.com/todos/')
    # Process Todo
    tmp_lst = r_users.json()
    all_todo_items = []

    for item in range(len(tmp_lst)):
        lst = []
        if 

    # Pretty print te result
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(done_items), len(all_todo_items)))
    for item in done_items:
        print('\t {}'.format(item.get('title')))
