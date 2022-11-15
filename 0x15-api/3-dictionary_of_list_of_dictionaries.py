#!/usr/bin/python3
"""Export data from a REST API to JSON."""
from collections import defaultdict
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/"
    filename = 'todo_all_employees.json'

    users = requests.get(url).json()

    data_json = defaultdict(list)
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        tasks = requests.get('{}{}/todos'.format(url, user_id)).json()
        for task in tasks:
            data = {}
            data['task'] = task.get('title')
            data['completed'] = task.get('completed')
            data['username'] = username
            data_json[user_id].append(data)
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(data_json, f)
