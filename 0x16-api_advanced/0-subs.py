#!/usr/bin/python3
"""retrieve the number of subscribers for a given subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""

    headers = {"User-Agent": "0-subs/1.0"}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    r = requests.get(url=url, headers=headers, allow_redirects=False)
    if r.status_code == 404:
        return 0
    results = r.json().get("data")
    return results.get("subscribers")
