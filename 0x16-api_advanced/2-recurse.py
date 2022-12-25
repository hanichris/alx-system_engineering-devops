#!/usr/bin/python3
"""Recursive function to query the Reddit API.

Make a query to return a list containing the titles of all
hot articles of a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """Return a list containing the titles of all the hot posts.

    Args:
        subreddit (str): subreddit to be queried.
        hot_list (list): titles of all the hot posts.

    Return:
        hot_list (list of str)
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    payload = {
            'after': after,
            'limit': 100}
    header = {'user-agent': 'python_script'}
    r = requests.get(url, params=payload, headers=header,
                     allow_redirects=False)
    if r.status_code == 404:
        return None
    r = r.json().get('data')
    after = r.get('after')
    data = r.get('children')
    for post in data:
        _x = post.get('data').get('title')
        hot_list.append(_x)
    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
