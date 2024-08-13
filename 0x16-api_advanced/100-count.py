#!/usr/bin/python3
"""Module for counting occurrences of keywords in hot post titles on Reddit."""
import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Recursively queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): List of keywords to count.
        after (str): Parameter for pagination (used for recursion).
        word_count (dict): Dictionary to store word counts (used for recursion).

    Returns:
        None
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:0.1 (by /u/elhassanelas)"}
    params = {"limit": 100, "after": after}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return

    data = response.json().get("data", {})

    for post in data.get("children", []):
        title = post["data"]["title"].lower()
        for word in word_list:
            word = word.lower()
            if word in title.split():
                word_count[word] = word_count.get(word, 0) + 1

    after = data.get("after")
    if after:
        count_words(subreddit, word_list, after, word_count)
    else:
        sorted_counts = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            if count > 0:
                print("{}: {}".format(word, count))
