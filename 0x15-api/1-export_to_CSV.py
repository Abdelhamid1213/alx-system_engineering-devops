#!/usr/bin/python3
"""This script exports tasks of a given employee to a CSV file.

The script takes an employee ID as a command-line argument and retrieves
the tasks associated with that employee from a REST API.

It then writes the tasks to a CSV file in the format:
    "employee_id","username","completed","title\""""


if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) != 2:
        sys.exit(f"Usage: python3 {sys.argv[0]} <employee_id>")

    employee_id = sys.argv[1]
    route = 'https://jsonplaceholder.typicode.com'
    tasks = requests.get(f'{route}/todos?userId={employee_id}').json()
    username = requests.get(f'{route}/users/{employee_id}').json()['username']

    with open(f'{employee_id}.csv', "w") as f:
        for task in tasks:
            f.write('"{}","{}","{}","{}"\n'.format(
                employee_id,
                username,
                task['completed'],
                task['title'])
            )
