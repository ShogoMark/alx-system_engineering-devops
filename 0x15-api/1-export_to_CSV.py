#!/usr/bin/python3
"""A script that, uses this REST API, for a given employee ID"""

import csv
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
    filename = "{}.csv".format(sys.argv[1])
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for task in j_task:
            values = [sys.argv[1], j_res.get('username'),
                      task['completed'], task['title']]
            writer.writerow(values)
