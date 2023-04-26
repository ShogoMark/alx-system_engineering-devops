#!/usr/bin/python3
"""A script that, uses this REST API, for a given employee ID"""

import requests
import sys

if __name__ == "__main__":

    # API request to get employee information
    url = 'https://jsonplaceholder.typicode.com/'
    emp_data = requests.get('{}users/{}'.format(url, sys.argv[1]))
    j_res = emp_data.json()

    print("Employee {} is done with tasks".format(j_res.get('name')), end="")

    # API request to get employee to-do list
    emp_todo = '{}todos?userId={}'.format(url, sys.argv[1])
    todo_data = requests.get(emp_todo)
    total_task = todo_data.json()
    completed_task = []
    for task in total_task:
        if task.get('completed') is True:
            completed_task.append(task)
    print("({}/{}):".format(len(completed_task), len(total_task)))
    for task in completed_task:
        print("\t {}".format(task.get('title')))
