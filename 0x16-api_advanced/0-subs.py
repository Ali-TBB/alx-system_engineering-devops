#!/usr/bin/python3
"""
This function queries the Reddit API and returns
the number of subscribers for a given subreddit.
If the subreddit is invalid, the function returns 0.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Retrieve the number of subscribers for a given subreddit.
    """
    req = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"},
    )

    if req.status_code == 200:
        data = req.json()
        if 'data' not in data or 'subscribers' not in data['data']:
            return 0
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
