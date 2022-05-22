#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data
in the JSON format.
    - Records all tasks from all employees
    - Format must be:
      { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
        "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME",
        "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ],
        "USER_ID": [ ... ]}
    - File name must be: todo_all_employees.json

"""

import json
import requests


def main():
    url = 'https://jsonplaceholder.typicode.com/users/'
    users = requests.get(url).json()

    info = {}
    for usr in users:
        todos = requests.get('{}{}/todos'.format(url, usr.get('id'))).json()
        tasks, k = [], ['username', 'task', 'completed']

        for task in todos:
            v = [usr.get('username'), task.get('title'), task.get('completed')]
            tasks.append(dict(zip(k, v)))

        info[usr.get('id')] = tasks

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(info, json_file)


if __name__ == "__main__":
    main()
