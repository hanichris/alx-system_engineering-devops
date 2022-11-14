#!/usr/bin/python3
"""Export data from a REST API to CSV."""
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

    filename = '%s.csv' % (user_id)
    with open(filename, mode='w', encoding='utf-8') as f:
        for entry in res:
            out_str = '"%s","%s"' % (user_id, username)
            _str = ',"%s","%s"\n' % (entry['completed'], entry['title'])
            out_str += _str
            f.write(out_str)
