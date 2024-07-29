#!/usr/bin/python3
"""Export data in the JSON format"""
import json
import requests
import sys


def export_to_json(employee_id):
    """Export TODO list progress for a given employee ID to JSON."""
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Error: Unable to retrieve data")
        sys.exit(1)

    user_data = user_response.json()
    todos_data = todos_response.json()

    username = user_data['username']
    filename = f"{employee_id}.json"

    tasks = []
    for todo in todos_data:
        tasks.append({
            "task": todo['title'],
            "completed": todo['completed'],
            "username": username
        })

    json_data = {str(employee_id): tasks}

    with open(filename, 'w') as json_file:
        json.dump(json_data, json_file)

    print(f"Data exported to {filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)

    export_to_json(employee_id)
