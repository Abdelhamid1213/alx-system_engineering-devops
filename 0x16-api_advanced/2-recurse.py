#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests


def recurse(subreddit, after=None, count=0):
    """Returns a generator yielding titles of all hot posts on a given
 subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"User-Agent": "ubuntu:alx/1.0"}
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    with requests.Session() as session:
        while True:
            response = session.get(url, headers=headers, params=params,
                                   allow_redirects=False)
            if response.status_code == 404:
                return None

            results = response.json().get("data")
            after = results.get("after")
            count += results.get("dist")
            for c in results.get("children"):
                yield c.get("data").get("title")

            if after is None:
                break
            params['after'] = after
