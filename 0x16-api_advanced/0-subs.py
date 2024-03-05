#!/usr/bin/python3
"""This module contains a function to retrieve the number of subscribers for
 a given subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    headers = {
        "User-Agent": "0-subs/1.0"
    }
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    r = requests.get(url=url, headers=headers, allow_redirects=False).json()
    return 0 if 'error' in r else r['data']['subscribers']
