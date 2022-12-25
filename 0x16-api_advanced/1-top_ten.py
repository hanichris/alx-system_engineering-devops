#!/usr/bin/python3
"""Module that queries the `Reddit API`.

Query the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """Print the titles of the top ten hot posts in a subreddit.

    Arg:
        subreddit (str): subreddit to query.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'user-agent': 'python3_script'}
    payload = {'limit': '10'}
    r = requests.get(url, headers=headers, params=payload,
                     allow_redirects=False)
    if r.status_code == 404:
        print(None)
        return
    data = r.json().get('data').get('children')
    titles = []
    for title in data:
        print(title.get('data').get('title'))
