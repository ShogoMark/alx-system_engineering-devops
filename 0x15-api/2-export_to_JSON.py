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
    emp_data = requests.get('{}users/{}'.format(url, sys.argv[1]))
    j_res = emp_data.json()

    emp_task = requests.get('{}todos?userId={}'.format(url, sys.argv[1]))
    j_task = emp_task.json()
    all_task = []
    for task in j_task:
        all_task.append({"task": task["title"],
                         "completed": task["completed"],
                         "username": j_res.get('username')})
    filename = "{}.json".format(sys.argv[1])
    with open(filename, 'w') as json_file:
        json.dump({sys.argv[1]: all_task}, json_file)
    with open(filename, 'r') as f:
        read_data = json.load(f)
        reverse_data = read_data[sys.argv[1]][::-1]
        with open(filename, 'w') as new_json:
            json.dump({sys.argv[1]: reverse_data}, new_json)
