#!/usr/bin/python3
"""A module that contains function that queries the Reddit API and
prints the titles of the first 10 hot posts listed for a given subreddit.

Requirements:
- Prototype: def top_ten(subreddit)
- If not a valid subreddit, print None.

NOTE: Invalid subreddits may return a redirect to search results. Ensure
that you are not following redirects.
"""
import requests


def top_ten(subreddit):
    """The function that does as stated in the the documenttation above.
    """
    my_client = requests.session()

    # Set custom header to avoid "too many requests error (429)"
    custom_header = {'user-agent': 'Custom User Agent for task 2'}
    my_client.headers = custom_header

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    r = my_client.get(url, allow_redirects=False)
    if r.status_code == 200:
        list_of_hot_dicts = r.json()["data"]["children"]
        for item in list_of_hot_dicts:
            print(item['data']['title'])
    else:
        return None


if __name__ == "__main__":
    top_ten("programming")
