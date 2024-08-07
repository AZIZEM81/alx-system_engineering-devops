#!/usr/bin/python3
"""Export data in the CSV format"""
import csv
import requests
import sys


def export_to_csv(employee_id):
    """Export TODO list progress for a given employee ID to CSV."""
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
    filename = f"{employee_id}.csv"

    with open(filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for todo in todos_data:
            writer.writerow([
                employee_id,
                username,
                str(todo['completed']),
                todo['title']
            ])

    print(f"Data exported to {filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)

    export_to_csv(employee_id)
