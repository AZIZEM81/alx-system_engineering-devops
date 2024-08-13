#!/usr/bin/python3
"""Module for recursively querying the Reddit API and returning hot posts."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): The list to store hot post titles (used for recursion).
        after (str): The parameter for pagination (used for recursion).

    Returns:
        list: A list of hot post titles, or None if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:0.1 (by /u/elhassanelas)"}
    params = {"limit": 100, "after": after}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    hot_list.extend([post["data"]["title"] for post in data.get("children", [])])

    after = data.get("after")
    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list
