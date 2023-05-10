#!/usr/bin/python3
"""A function that queries Reddit API returns no. of Subs"""

import json
import requests
import sys


def number_of_subscribers(subreddit):
    """A function that takes in one parameter"""
    subreddit = sys.argv[1]

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Custom"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()['data']['subscribers']
        return data
    else:
        return 0
