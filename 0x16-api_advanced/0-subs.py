#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of subscribers
    for a given subreddit. If an invalid subreddit is given, the function should
    return 0.

    Args:
        subreddit (str): The subreddit to query.

    Returns:
        int: The number of subscribers for the subreddit.
    """


    # set the custom User-Agent
    headers = {'User-Agent': 'Mozilla/5.0'}

    # make the request to the Reddit API
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers)

    # check if the request was successful

    if response.status_code != 200:
        return 0

    # extract the number of subscribers
    data = response.json().get('data')
    subscribers = data.get('subscribers')

    return subscribers
