#!/usr/bin/python3
"""Gather data from a REST API."""
import requests
import sys


if __name__ == "__main__":
    user_url = "https://jsonplaceholder.typicode.com/users/"
    todo_url = "https://jsonplaceholder.typicode.com/todos/"
    emp_id = sys.argv[1]

    response = requests.get('%s%s' % (user_url, emp_id)).json()
    name = response['name']
    user_id = response['id']

    res = requests.get('%s?userId=%s' % (todo_url, user_id)).json()
    completed = list(filter(lambda x: (x['completed'] is True), res))

    total_tasks = len(res)
    completed_tasks = len(completed)

    first_line = 'Employee %s is done with tasks(%d/%d):' %\
        (name, completed_tasks, total_tasks)
    print(first_line)
    for task in completed:
        print('\t %s' % (task['title']))
