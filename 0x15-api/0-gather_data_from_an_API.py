#!/usr/bin/python3
"""A script that, uses this REST API, for a given employee ID"""

import requests
import sys

if __name__ == "__main__":

# API request to get employee information
    emp_res = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1]))
    emp_data = emp_res.json()
	
    print("Employee {} is done with tasks".format(emp_data.get('name')), end="")

# API request to get employee to-do list
    emp_todo = requests.get("https://jsonplaceholder.typicode.com/todos/{}".format(sys.argv[1]))
    todo_data = emp_todo.json()
    completed_task = []
    	for task in todo_data:
            if task.get('completed') is True:
                completed_task.append(task)

	print("({}/{}):".format(len(completed_task), len(todo_data)))
	for task in completed_task:
		print("\t {}".format(task.get('title')))
