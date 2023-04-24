#!/usr/bin/env python3
from requests import get
from sys import argv




if __name__ == '__main__':
    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    response = requests.get(url)
    employee_name = response.json().get('name')
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    response = requests.get(url)
    tasks = response.json()
    completed_tasks = [task for task in tasks if task.get('completed')]
    num_completed_tasks = len(completed_tasks)
    total_num_tasks = len(tasks)

    print("Employee {} is done with tasks ({}/{}):"
          .format(employee_name, num_completed_tasks, total_num_tasks))
    for task in completed_tasks:
        print("\t{} {}".format('\u2022', task.get('title')))

