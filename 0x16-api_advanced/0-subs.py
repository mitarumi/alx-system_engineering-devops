#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API
    - If not a valid subreddit, return 0.
    """
    try:
        req = requests.get(
            "https://www.reddit.com/r/{subreddit}/about.json",
            headers={"User-Agent": "mita"},
        )

        if req.status_code == 200:
            data = req.json()
            return data['data']['subscribers']
        return 0
    except requests.RequestException:
        return 0
