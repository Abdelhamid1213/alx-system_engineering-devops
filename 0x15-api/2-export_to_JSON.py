#!/usr/bin/python3
"""This script exports tasks of a given employee from the JSONPlaceholder API
to a JSON file.

Usage: python3 2-export_to_JSON.py <employee_id>"""

if __name__ == "__main__":
    import json
    import requests
    import sys

    if len(sys.argv) != 2:
        sys.exit(f"Usage: python3 {sys.argv[0]} <employee_id>")

    employee_id = sys.argv[1]
    route = 'https://jsonplaceholder.typicode.com'
    tasks = requests.get(f'{route}/todos?userId={employee_id}').json()
    username = requests.get(f'{route}/users/{employee_id}').json()['username']

    data = {employee_id: []}
    for task in tasks:
        data[employee_id].append({"task": task['title'],
                                  "completed": task['completed'],
                                  "username": username})

    with open(f'{employee_id}.json', "w") as f:
        json.dump(data, f)
