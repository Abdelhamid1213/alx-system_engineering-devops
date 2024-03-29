#!/usr/bin/python3
"""A script prints titles of top ten posts from a given subreddit."""
import requests


def top_ten(subreddit):
    """Prints the titles of the top ten posts from a given subreddit."""
    headers = {"User-Agent": "ubuntu:alx/1.0"}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'

    r = requests.get(url=url, headers=headers, allow_redirects=False)
    if r.status_code == 404:
        print(None)
    else:
        for post in r.json()['data']['children']:
            print(post['data']['title'])
