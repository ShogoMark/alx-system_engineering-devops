#!/usr/bin/python3
"""Function to query a list of all hot posts for a given subreddit"""

import requests


def recurse(subreddit, hot_list=[], after=None):

    """A function takes in one parameter"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    if after:
        url += f"?after={after}"

    headers = {"User-Agent": "Chrome/88.0.4324.182 Safari/537.36"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()['data']
        articles = data['children']
        for article in articles:
            list_title = article['data']['title']
            hot_list.append(list_title)

        if data['after'] is not None:
            return recurse(subreddit, hot_list, after=data['after'])
        else:
            return hot_list

    else:
        return None
