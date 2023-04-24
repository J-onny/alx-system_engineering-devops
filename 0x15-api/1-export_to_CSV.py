#!/usr/bin/python3
import csv
import requests
import sys

if __name__ == '__main__':
    
    user_id = sys.argv[1]

    user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    user_response = requests.get(user_url)
    user_data = user_response.json()

    tasks_url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
    tasks_response = requests.get(tasks_url)
    tasks_data = tasks_response.json()

    employee_name = user_data['name']
    filename = f'{user_id}.csv'

    with open(filename, mode='w', newline='') as csv_file:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        for task in tasks_data:
            writer.writerow({
                'USER_ID': user_id,
                'USERNAME': employee_name,
                'TASK_COMPLETED_STATUS': str(task['completed']),
                'TASK_TITLE': task['title']
            })

    print(f'TODO list progress for employee {employee_name} has been exported to {filename}')

