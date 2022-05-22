#!/usr/bin/python3
"""
Module that, using this REST API, for a given employee ID, returns information
about his/her TODO list progress.
    - Use urllib or requests module
    - The script accepts an integer as a parameter, which is the employee ID
    - The script displays the employee TODO list in this exact format:
        - First line: Employee EMPLOYEE_NAME is done with
          tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
            - EMPLOYEE_NAME: name of the employee
            - NUMBER_OF_DONE_TASKS: number of completed tasks
            - TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of
              completed and non-completed tasks
        - Second and N next lines display the title of completed tasks:
        TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
REST API: https://jsonplaceholder.typicode.com/
"""

import requests
from sys import argv


def main():
    url = 'https://jsonplaceholder.typicode.com/users/'
    users = requests.get('{}{}'.format(url, argv[1])).json()
    todos = requests.get('{}{}/todos'.format(url, argv[1])).json()

    done_task = [task.get('title') for task in todos
                 if task.get('completed') is True]

    print('Employee {} is done with tasks({}/{}):'
          .format(users['name'], len(done_task), len(todos)))
    for title in done_task:
        print('\t {}'.format(title))


if __name__ == "__main__":
    main()
