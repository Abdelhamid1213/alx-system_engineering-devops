#!/usr/bin/python3
"""This script retrieves data from an API and creates a JSON file containing
a dictionary of tasks for each employee.

The script makes use of the requests library to send HTTP requests to the API
and retrieve data in JSON format.
It retrieves a list of tasks for each employee and organizes them into
a dictionary, where the keys are employee IDs.
Each value in the dictionary is a list of dictionaries, representing individual
 tasks, with the task title, completion status, and the employee's username.

The resulting dictionary is then dumped into a JSON file named
'todo_all_employees.json'"""

if __name__ == "__main__":
    import json
    import requests

    route = 'https://jsonplaceholder.typicode.com'

    r = requests.get(f'{route}/todos/').json()
    unique_employee_ids = set(entry['userId'] for entry in r)
    data = {}

    for employee_id in unique_employee_ids:
        tasks = requests.get(f'{route}/todos?userId={employee_id}').json()
        username = requests.get(
            f'{route}/users/{employee_id}'
        ).json()['username']
        data[employee_id] = []
        for task in tasks:
            data[employee_id].append({"task": task['title'],
                                      "completed": task['completed'],
                                      "username": username})

    with open('todo_all_employees.json', "w") as f:
        json.dump(data, f)
