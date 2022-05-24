#!/usr/bin/python3
"""
This module solves the following requirements and relies on the file
test/2-main.py

Write a recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit. If no results
are found for the given subreddit, the function should return None.

Hint: The Reddit API uses pagination for separating pages of responses.

Requirements:

    - Prototype: def recurse(subreddit, hot_list=[])
    - Note: You may change the prototype, but it must be able to be called
      with just a subreddit supplied.
      AKA you can add a counter, but it must work without supplying a starting
      value in the main.
    - If not a valid subreddit, return None.
    - NOTE: Invalid subreddits may return a redirect to search results.
      Ensure that you are not following redirects.

"""

import requests


def recurse(subreddit, hot_list=[], after='null'):
    """ Returns a list with the titles of hot articles for a subreddit """
    headers = {'User-Agent': 'viajeradelaluz'}
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'
    call = requests.get(
        url.format(subreddit, after), headers=headers, allow_redirects=False)

    if call.status_code != 200:
        return None

    posts = call.json().get('data').get('children')
    for post in posts:
        hot_list.append(post.get('data').get('title'))

    after = call.json().get('data').get('after')
    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list
