#!/usr/bin/python3
"""This module contains a function to retrieve the number of subscribers for
 a given subreddit."""
import requests


def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    r = requests.get(url=url, headers=headers).json()
    return 0 if 'error' in r else r['data']['subscribers']
