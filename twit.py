import rambler
from bot import get_credentials
from twitter import Twitter, OAuth
import time

hashtag = " #GamerGate"

twit_freq = 30

def next_tweet():
    res = ""
    while len(res) + len(hashtag) < 125:
        res += rambler.get_string()
    if len(res) + len(hashtag) > 140:
        res = res[:(140-len(hashtag))]
        res = res[:res.rindex(" ")]
        return (True, res + hashtag)
    return (False, res + hashtag)

def post_next(twitter, depth=0):
    if depth > 2: return
    nxt = next_tweet()
    twitter.statuses.update(status=nxt[1])
    if nxt[0]:
        time.sleep(10)
        post_next(twitter, depth+1)

def main():
    creds = get_credentials()
    twit = Twitter(auth=OAuth(
            creds["accesstoken"],
            creds["accesssecret"],
            creds["consumerkey"],
            creds["consumersecret"]
        ))
    while(True):
        post_next(twit)
        time.sleep(twit_freq*60)

if __name__ == "__main__":
    main()



