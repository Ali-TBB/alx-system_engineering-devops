#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Function that queries the Reddit API and prints
    the titles of the top 10 hot posts in a subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None

    Prints:
        The titles of the top 10 hot posts in the specified subreddit.

    If the subreddit is not valid or the API request fails, it prints None.
    """
    req = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"limit": 10},
    )

    if req.status_code == 200:
        for get_data in req.json().get("data").get("children"):
            dat = get_data.get("data")
            title = dat.get("title")
            print(title)
    else:
        print(None)
