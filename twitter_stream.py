"""
twitter_timeline.py
Mayank Gureja
01/21/2013
CS 480
"""


import tweetstream
import codecs

username = 'mayankgureja'
password = ''

filters = ["#snow", "#philly", "#philadelphia"]

try:
    # with tweetstream.TweetStream(username, password) as stream:
    with tweetstream.FilterStream(username, password, track=filters) as stream:
        for tweet in stream:
            if "text" in tweet:
                print "%-16s\t: %s" % (tweet["user"]["screen_name"], tweet['text'].encode('ascii', 'ignore'))
except tweetstream.ConnectionError, e:
    print "Disconnected from twitter. Reason:", e.reason
