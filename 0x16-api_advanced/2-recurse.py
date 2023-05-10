#!/usr/bin/python3
"""A function that queries Reddit API returns no. of Subs"""

import json
import requests
import sys

def recurse(subreddit, hot_list=[], after=None):
    """function takes in one parameter"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    if after:
        url += f"&after={after}"
    headers = {"User-Agent": "Custom User Agent"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
       data  = response.json()['data']
       articles = data['children']
       for article in articles:
            list_title = article['data']['title']
            hot_list.append(list_title)
       print(len(hot_list))

       #if data['after'] is not None:
        #    return recurse(subreddit, hot_list, after=data['after'])
    #else:
      #  return None

    #return hot_list
