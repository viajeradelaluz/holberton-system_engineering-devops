#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data
in the JSON format.
    - Records all tasks that are owned by this employee
    - Format must be:
      { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
        "username": "USERNAME"}, ... ] }
    - File name must be: USER_ID.json
"""

import json
import requests
from sys import argv


def main():
    url = 'https://jsonplaceholder.typicode.com/users/'
    users = requests.get('{}{}'.format(url, argv[1])).json()
    todos = requests.get('{}{}/todos'.format(url, argv[1])).json()

    info, tasks, k = {}, [], ['task', 'completed', 'username']

    for task in todos:
        v = [task.get('title'), task.get('completed'), users.get('username')]
        tasks.append(dict(zip(k, v)))
        info[users.get('id')] = tasks

    filename = '{}.json'.format(argv[1])
    with open(filename, 'w') as json_file:
        json.dump(info, json_file)


if __name__ == "__main__":
    main()
