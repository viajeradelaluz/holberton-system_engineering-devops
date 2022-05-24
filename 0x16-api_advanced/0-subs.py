#!/usr/bin/python3
"""
This module solves the following requirements and relies on the file
test/0-main.py

Write a function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.

Hint: No authentication is necessary for most features of the Reddit API. If
you're getting errors related to Too Many Requests, ensure you're setting
a custom User-Agent.

Requirements:

    - Prototype: def number_of_subscribers(subreddit)
    - If not a valid subreddit, return 0.
    - NOTE: Invalid subreddits may return a redirect to search results.
      Ensure that you are not following redirects.
"""

import requests


def number_of_subscribers(subreddit):
    """ Returns the number of suscribers for a given subreddit """
    headers = {'User-Agent': 'viajeradelaluz'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    call = requests.get(url, headers=headers, allow_redirects=False)

    if call.status_code != 200:
        return 0
    response = call.json().get('data').get('subscribers', 0)

    return response
