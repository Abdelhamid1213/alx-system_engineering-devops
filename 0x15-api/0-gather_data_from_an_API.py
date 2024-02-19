#!/usr/bin/python3
"""This script retrieves data from an API based on the employee ID provided
as a command-line argument.

It fetches the tasks associated with the employee and displays the number of
completed tasks out of the total tasks."""


if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) != 2:
        sys.exit(f"Usage: python3 {sys.argv[0]} <employee_id>")

    employee_id = sys.argv[1]
    route = 'https://jsonplaceholder.typicode.com'
    tasks = requests.get(f'{route}/todos?userId={employee_id}').json()
    employee_name = requests.get(f'{route}/users/{employee_id}').json()['name']
    number_of_done_tasks = 0
    total_number_of_tasks = len(tasks)

    for task in tasks:
        if task['completed']:
            number_of_done_tasks += 1

    print(f'Employee {employee_name} \
is done with tasks({number_of_done_tasks}/{total_number_of_tasks}):')

    for task in tasks:
        if task['completed']:
            print(f'\t {task["title"]}')
