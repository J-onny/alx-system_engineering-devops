#!/usr/bin/python3

from json import loads
from requests import get

def number_of_subscribers(subreddit):
    """Function that queries the Reddit API and returns the number
    of subscribers for a given subreddit. If the subreddit is invalid or there
    is an error in the request, the function returns 0."""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) \
        Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)'
    }

    try:
        response = get(url, headers=headers)
        response.raise_for_status()  # Raise exception for HTTP errors
        reddits = response.json()
        subscribers = reddits.get('data', {}).get('subscribers', 0)
        return int(subscribers)
    except Exception as e:
        print("An error occurred while making the request:", str(e))
        return 0

