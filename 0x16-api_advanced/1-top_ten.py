#!/usr/bin/python3

import requests

"""Top ten students"""


def top_ten(subreddit):
    rse = requests.get('https://reddit.com/r/{}.json?sort=hot&limit=10'.
                       format(subreddit), headers={'User-Agent': 'custom'})
    if (rse):
        for i in rse.json().get('data').get('children'):
            print(i.get('data').get('title'))
    else:
        print("None")
