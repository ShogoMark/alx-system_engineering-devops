#!/usr/bin/python3
"""A function that queries Reddit API returns no. of Subs"""

import json
import requests
import sys

def number_of_subscribers(subreddit):
    """A function that takes in one parameter"""
    subreddit = sys.argv[1];
    
    
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom User Agent"}
    
    
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()['data']['subscribers']
        return data
    else:
        return 0
