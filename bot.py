import praw
import rambler
import json
import os.path
import time

autogator_on = ["autogator", "big gator", "test gator", "teeth", "ethics",
    "goober", "sjw", "intel"]

def get_handled(cache="handled.json"):
    if not os.path.exists(cache): return []
    with open(cache, "r") as f:
        return json.loads(f.read())

def save_handled(handled, cache="handled.json"):
    with open(cache, "w") as f:
        data = json.dumps(handled)
        f.write(data)

def get_credentials(cache=".credentials"):
    with open(cache, "r") as f:
        return json.loads(f.read())

redd = praw.Reddit("AutoGator, a GamerGate MarkovChain replier.", site="autogator")
creds = get_credentials()
redd.login(creds["user"], creds["password"])
gg = redd.get_subreddit("kotakuinaction")

handled = get_handled()
while(True):
    try:
        for subm in gg.get_hot(limit=10):
            title = subm.title.lower()
            gatory = any(s in title for s in autogator_on)
            if not subm.id in handled and gatory:
                msg = rambler.ramble()
                subm.add_comment(msg)
                handled += [subm.id]
    except: pass
    finally:
        save_handled(handled)
    time.sleep(60*10)