A simple Reddit bot that uses a data file scraped from /r/KotakuInAction to generate a Markov chain. That chain is used to generate word-salad posts in response to very specific keywords, in reply to /r/KiA.

Run Redditbot using:

    $ python3 bot.py

Run Twitterbot using:

    $ python3 twit.py

Twitterbot always tweets with the hashtag #GamerGate.

Credentials must be stored in a .credentials file, as a JSON dict, with the following keys:

* user : reddit username
* password : reddit password
* consumerkey : twitter consumer key
* consumersecret : twitter consumer secret
* accesstoken : twitter OAuth access token
* accesssecret : twitter OAuth access secret


Data file is nov14.txt, which is just a scrape of KiA, gathered using downloader.py. Run that using:

    $ python3 downloader.py > destfile.txt

I also manually entered some data from various pro-GG articles. I'm not really closely monitoring sources, so the data isn't super great.

PyMarkovChain pickles its database into a file called "markov". If this file doesn't exist, it will rescan the data file.

Depends on praw, PyMarkovChain and Twitter. PyMarkovChain is included, because I thought I was going to have to make some minor changes to it. Yes, it probably shouldn't be, since I didn't. This is sloppy, and ugly, but it's a stupid Reddit bot that makes fun of GamerGaters.

Sample post:

    So I did find it rather annoying that Koster tries to compare. Jezebel is just as a *prize for men. Should they just want to touch it because we lack enough 'credible' sources to cite. It flatly won't work. I do think there is no reporting or record of SJW stalking, harassment, or threats. Moderates within the context I'm assuming you're a writer as well. Instead of defending the rights of creators and consumers, he helps burn the bridge of creativity that he was a misanthrope more than passingly familiar with. Why would you be checking back on this one, but it's also pretty silly to literally gas people in GG probably relate, but not much clear exposure of serious wrongdoing. No matter what you would want to keep working at this point that the primary purpose of denigrating conservatives and (reportedly) conspiring to support the then-presidential candidate Barrack Obama. * Gizmodo – Gadget and technology lifestyle. 
