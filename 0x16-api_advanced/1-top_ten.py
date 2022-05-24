#!/usr/bin/python3
"""
This module solves the following requirements and relies on the file
test/1-main.py

Write a function that queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit.

Requirements:

    - Prototype: def top_ten(subreddit)
    - If not a valid subreddit, print None.
    - NOTE: Invalid subreddits may return a redirect to search results.
      Ensure that you are not following redirects.
"""

import requests


def top_ten(subreddit):
    """ Prints the titles of the first 10 hot posts of a given subreddit """
    headers = {'User-Agent': 'viajeradelaluz'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    call = requests.get(url, headers=headers, allow_redirects=False)

    if call.status_code != 200:
        print('None')
        return

    posts = call.json().get('data').get('children')
    if not posts:
        print('None')
        return

    for post in posts:
        print(post.get('data').get('title'))
