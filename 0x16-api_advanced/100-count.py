#!/usr/bin/python3
"""Recursive function to query the Reddit API.

Make a query to the Reddit API, parse the title of all
hot articles and print a sorted count of given keywords.
"""
import requests


def _util_count_words(subreddit, word_list, hot_list=[], after=''):
    """Return a list containing the titles of all the hot posts.

    Args:
        subreddit (str): subreddit to be queried.
        word_list (list): list of keywords to search for.
        hot_list (list): list of titles of hot articles.
        after (str): Next page to visit.

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
        title = post.get('data').get('title')
        _x = list(filter(lambda x: x in word_list, title.lower().split()))
        if len(_x) > 0:
            hot_list.extend(_x)
    if after:
        return _util_count_words(subreddit, word_list, hot_list, after)
    else:
        return hot_list


def count_words(subreddit, word_list):
    """Print sorted count of given keywords.

    Queries the Reddit API and parses the title of all hot articles
    to generate a list of them before processing it to generate
    a dictionary of the given keywords.
    Args:
        subreddit (str): subreddit to be queried.
        word_list (list): list of keywords to search for.
    """
    word_list = [word.lower() for word in word_list]
    hot_list = _util_count_words(subreddit, word_list)
    if hot_list is None:
        return None
    result = {}
    for word in hot_list:
        if word not in result:
            result[word] = 1
        elif word in result:
            result[word] += 1
    from collections import Counter
    count = Counter(word_list)
    for key, value in count.items():
        if value > 1:
            result[key] *= value
    for key, value in sorted(result.items(),
                             key=lambda x: x[1], reverse=True):
        print('{}: {}'.format(key, value))
