"""
Download the top 100 posts and top comments from /r/kotakuinaction

Run using: python3 downloader.py 
"""
import sys
import re
import time
import praw
import traceback

url = re.compile("[\s\[:\(]http.+?[\s\]\)]")
def strip_urls(text):
    """This doesn't actually fully work. 
    I don't feel like spending more time debugging the regex.
    I've manually corrected the nov14.txt data file."""
    return url.sub("", text)

def download_sub(sub="kotakuinaction",num_posts=100):
    """This still throws out a shitton of "too many client requests"
    errors, which I assume is a side effect of the flatten_tree
    method, but again, I don't feel like spending any more time
    figuring it out."""
    red = praw.Reddit(user_agent="markov_slurper")
    for _ in range(20):
        try:
            sub = red.get_subreddit(sub)
            posts = sub.get_hot(limit=num_posts)
            time.sleep(3)
            for p in posts:
                print(p.title)
                print(strip_urls(p.selftext))
                try:
                    flat = praw.helpers.flatten_tree(p.comments)
                    for c in flat:
                        print(strip_urls(c.body))
                except Exception as e:
                    print(traceback.format_exc(), file=sys.stderr)
            break
        except Exception as e: 
            print(e, file=sys.stderr)

download_sub()
