#!/usr/bin/python3
"""Export data from a REST API to JSON."""
from collections import defaultdict
import json
import requests
import sys


if __name__ == "__main__":
    user_url = "https://jsonplaceholder.typicode.com/users/"
    todo_url = "https://jsonplaceholder.typicode.com/todos/"
    emp_id = sys.argv[1]

    response = requests.get('%s%s' % (user_url, emp_id)).json()
    username = response['username']
    user_id = response['id']

    res = requests.get('%s?userId=%s' % (todo_url, user_id)).json()

    data_json = defaultdict(list)
    for entry in res:
        data = {}
        data['task'] = entry['title']
        data['completed'] = entry['completed']
        data['username'] = username
        data_json[user_id].append(data)

    filename = '%s.json' % (user_id)
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(data_json, f)
