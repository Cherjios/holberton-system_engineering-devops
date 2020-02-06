#!/usr/bin/python3

import requests

"""Number of subscriber"""


def number_of_subscribers(subreddit):
    rse = requests.get('https://reddit.com/r/{}/about.json'.format(subreddit),
                       headers={'User-Agent': 'custom'})
    if (rse):
        return rse.json().get('data').get('subscribers')
    else:
        return 0
