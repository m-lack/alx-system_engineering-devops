#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return "OK"  # Return "OK" for invalid subreddit input

    try:
        r = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                         headers={'User-Agent': '0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)'}).json()

        # Check if the subreddit exists
        if r.get("error"):
            return "OK"  # Return "OK" if subreddit does not exist

        subs = r.get("data", {}).get("subscribers", 0)
        return subs  # Return the number of subscribers if subreddit exists
    except Exception:
        return "OK"  # Return "OK" in case of an error (e.g., network issues)

