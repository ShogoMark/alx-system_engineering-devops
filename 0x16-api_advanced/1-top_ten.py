#!/usr/bin/python3
"""
A function that queries the Reddit API and prints 
the titles of the first 10 hot posts 
listed for a given subreddit
"""

import json
import requests
import sys


def top_ten(subreddit):
    """Function takes in one parameter"""
    
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Custom User Agent"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()['data']['children']
        for post in data:
            print(post['data']['title'])
    else:
        print(None)
