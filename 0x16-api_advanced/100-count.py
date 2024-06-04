#!/usr/bin/python3
"""
This script counts the occurrences of given
words in the titles of hot posts from a specified subreddit on Reddit.
"""

import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """
    Recursive function that queries the Reddit API,
    parses the title of all hot articles,
    and prints a sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit to search.
        word_list (list): A list of words to count occurrences of.
        after (str, optional): A token indicating the starting point
        for the next batch of posts. Defaults to None.
        counts (dict, optional): A dictionary to store the word counts.
        Defaults to an empty dictionary.

    Returns:
        None
    """
    if not word_list or word_list == [] or not subreddit:
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}

    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()
    children = data["data"]["children"]

    for post in children:
        title = post["data"]["title"].lower()
        for word in word_list:
            if word.lower() in title:
                counts[word] = counts.get(word, 0) + title.count(word.lower())

    after = data["data"]["after"]
    if after:
        count_words(subreddit, word_list, after, counts)
    else:
        sorted_counts = sorted(counts.items(),
                               key=lambda x: (-x[1], x[0].lower()))
        for word, count in sorted_counts:
            print(f"{word.lower()}: {count}")
