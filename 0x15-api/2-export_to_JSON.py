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
    print(j_task)
