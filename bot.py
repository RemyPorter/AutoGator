import praw
import rambler
import json
import os.path

autogator_on = ["autogator", "big gator", "test gator", "teeth", "ethics",
    "goober", "sjw"]

def get_handled(cache="handled.json"):
    if not os.path.exists(cache): return []
    with open(cache, "r") as f:
        return json.loads(cache.read())

def save_handled(handled, cache="handled.json"):
    with open(cache, "w") as f:
        data = json.dumps(handled)
        f.write(data)

redd = praw.Reddit("AutoGator, a GamerGate MarkovChain replier.")
redd.login()
gg = redd.get_subreddit("gamerghazi")

handled = get_handled()

for subm in gg.get_hot(limit=10):
    title = subm.title.lower()
    gatory = any(s in title for s in autogator_on)
    if not subm.id in handled and gatory:
        msg = rambler.ramble()
        subm.add_comment(msg)
        handled += [subm.id]

save_handled(handled)