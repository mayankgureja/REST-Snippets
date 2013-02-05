"""
twitter_timeline.py
Mayank Gureja
01/16/2013
CS 480
"""


import oauth2 as oauth
import json

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_SECRET = ""

HOME_TIMELINE = "http://api.twitter.com/1/statuses/home_timeline.json"


def oauth_req(url, key, secret, http_method="GET", post_body="", http_headers=""):
    consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    token = oauth.Token(key=key, secret=secret)
    client = oauth.Client(consumer, token)

    resp, content = client.request(
        url,
        method=http_method,
        body=post_body,
        headers=http_headers
    )
    return resp, content


def main():
    home_resp, home_timeline = oauth_req(
        HOME_TIMELINE, ACCESS_TOKEN, ACCESS_SECRET)

    io = json.loads(home_timeline)

    for x in io:
        try:
        # can print str.encode('utf-8') to avoid encoding exception here
            print x['created_at'] + ': ' + x['user']['screen_name'] + ' said ' + x['text']
        except:
            print "Bad tweet"


if __name__ == '__main__':
    main()
