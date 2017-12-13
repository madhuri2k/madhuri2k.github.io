#!/usr/bin/env python3

import random
import rfeed
from flask import Flask

def truncate(s, n):
    x = len(s)
    if x > n and n > 2:
        s = ''.join([s[:(n-3)], '...'])
    return s

rss_len=10
title_len = 20
datafile = 'data.txt'

def get_rows(fn, size):
    with open(fn) as f:
        rows = random.sample(f.readlines(), size)
    print("Selected {} items.".format(len(rows)))
    return rows

def create_random_feed(filename, feed_length, title_length):
    selec = get_rows(filename, feed_length)
    content_list = []

    for it in selec:
        it = it.strip()
        fi = rfeed.Item( title = truncate(it, title_length), description = it )
        content_list.append(fi)

    feed = rfeed.Feed(
        title = "Sample RSS Feed",
        link = "https://github.com/madhuri2k/fantastic-spoon",
        description = "A Random selection of items",
        language = "en-US",
        items = content_list)

    print("Feed is {}".format(feed.rss()))

    return feed

app = Flask(__name__)
@app.route("/")
def get_news():
    feed = create_random_feed(datafile, rss_len, title_len)
    if feed:
        return feed.rss()
    else:
        return "No news is good news."

if __name__ == '__main__':
    # Run once locally
    create_random_feed(datafile, rss_len, title_len) 
    app.run(port=5000, debug=True)
