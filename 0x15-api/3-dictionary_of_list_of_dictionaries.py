#!/usr/bin/python3
"""Export all data in the JSON format"""
import json
import requests


def export_all_to_json():
    """Export TODO list progress for all employees to JSON."""
    base_url = "https://jsonplaceholder.typicode.com"
    users_url = f"{base_url}/users"
    todos_url = f"{base_url}/todos"

    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    if users_response.status_code != 200 or todos_response.status_code != 200:
        print("Error: Unable to retrieve data")
        return

    users_data = users_response.json()
    todos_data = todos_response.json()

    all_employees = {}

    for user in users_data:
        user_id = str(user['id'])
        username = user['username']
        user_todos = [todo for todo in todos_data if todo['userId'] == user['id']]
        
        tasks = []
        for todo in user_todos:
            tasks.append({
                "username": username,
                "task": todo['title'],
                "completed": todo['completed']
            })
        
        all_employees[user_id] = tasks

    filename = "todo_all_employees.json"
    with open(filename, 'w') as json_file:
        json.dump(all_employees, json_file)

    print(f"Data exported to {filename}")


if __name__ == "__main__":
    export_all_to_json()
