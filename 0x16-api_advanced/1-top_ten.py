#!/usr/bin/python3
"""Module for querying the Reddit API and printing top 10 hot posts titles."""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:0.1 (by /u/elhassanelas)"}
    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get("data", {})
        for post in data.get("children", []):
            print(post["data"]["title"])
    else:
        print(None)
