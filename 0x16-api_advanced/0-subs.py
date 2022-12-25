#!/usr/bin/python3
"""Module that queries the `Reddit API`.

Query the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Get the number of subscribers for a given subreddit.

    Arg:
        subreddit (str): subreddit to query.

    Return:
        count (int): number of subscribers for a given reddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'python3_script'}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 404:
        return 0
    data = r.json().get('data')
    return data.get('subscribers')
