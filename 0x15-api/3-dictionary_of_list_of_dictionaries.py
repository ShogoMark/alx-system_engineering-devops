#!/usr/bin/python3
"""A script that, uses this REST API, for a given employee ID"""

import csv
import json
import requests
import sys

if __name__ == "__main__":

    # API request to get employee information
    url = 'https://jsonplaceholder.typicode.com/'

    # API request to get employee information
    emp_data = requests.get('{}users'.format(url))
    username = emp_data.json()

    emp_task = requests.get('{}todos'.format(url))
    todos = emp_task.json()

    res = [{requests.get("userId"): [{"username": requests.get("username"), "task": [task["title"]], "completed": [task["completed"]]} for task in todos]} for users in username]
    print(res)
   #  with open(todo_all_employees.json, 'w') as json_file:
    #    json.dump({sys.argv[1]: all_task}, json_file)
