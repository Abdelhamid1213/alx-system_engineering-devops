#!/usr/bin/python3
"""retrieve the number of subscribers for a given subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""

    headers = {"User-Agent": "ubuntu:alx/1.0"}
    url = 'https://old.reddit.com/r/{}/about.json'.format(subreddit)

    r = requests.get(url=url, headers=headers, allow_redirects=False)
    return 0 if r.status_code == 404 else r.json()['data']['subscribers']
