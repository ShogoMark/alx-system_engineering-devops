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
    users = emp_data.json()

    emp_task = requests.get('{}todos'.format(url))
    todos = emp_task.json()

    res = {
          user.get("id"): [{"username": user.get("username"),
                            "task": todo.get("title"),
                            "completed": todo.get("completed")}
                           for todo in todos
                           if todo.get("userId") == user.get("id")]
          for user in users
     }
    with open("todo_all_employees.json", "w", newline="") as json_file:
        json.dump(res, json_file)
