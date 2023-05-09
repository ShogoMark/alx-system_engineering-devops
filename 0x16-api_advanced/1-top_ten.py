#!/usr/bin/python3
"""A function that queries Reddit API returns no. of Subs"""

import requests
import sys

def top_ten(subreddit):
    """function takes in one parameter"""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Custom User Agent"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()['data']['children']
        for post in data:
            print(post['data']['title'])
    else:
        print(None)
