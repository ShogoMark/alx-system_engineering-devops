#!/usr/bin/python3
"""A function that queries the Reddit API and prints query"""

import requests


def top_ten(subreddit):
    """Function takes in one parameter"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "MyApp/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data').get('children')
        for entry in data:
            print(entry.get('data').get('title'))
    else:
        print(None)
