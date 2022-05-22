#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data
in the CSV format.
    - Records all tasks that are owned by this employee
    - Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    - File name must be: USER_ID.csv
"""

import csv
import requests
from sys import argv


def main():
    url = 'https://jsonplaceholder.typicode.com/users/'
    users = requests.get('{}{}'.format(url, argv[1])).json()
    todos = requests.get('{}{}/todos'.format(url, argv[1])).json()

    filename = '{}.csv'.format(argv[1])
    with open(filename, 'w') as csv_file:
        info = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_ALL)

        for task in todos:
            info.writerow([users.get('id'), users.get('username'),
                           task.get('completed'), task.get('title')])


if __name__ == "__main__":
    main()
