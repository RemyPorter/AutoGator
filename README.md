A simple Reddit bot that uses a data file scraped from /r/KotakuInAction to generate a Markov chain. That chain is used to generate word-salad posts in response to very specific keywords used in /r/GamerGhazi.

Run using:

    $ python3 bot.py

Credentials must be stored in a .credentials file, as a JSON dict: {"user": username, "password": pass}. I know I should use praw.ini, but I couldn't get it to actually work.

Depends on praw and PyMarkovChain. PyMarkovChain is included, because I thought I was going to have to make some minor changes to it. Yes, it probably shouldn't be, since I didn't. This is sloppy, and ugly, but it's a stupid Reddit bot that makes fun of GamerGaters.

Sample post:
    o I did find it rather annoying that Koster tries to compare. Jezebel is just as a *prize for men. Should they just want to touch it because we lack enough 'credible' sources to cite. It flatly won't work. I do think there is no reporting or record of SJW stalking, harassment, or threats. Moderates within the context I'm assuming you're a writer as well. Instead of defending the rights of creators and consumers, he helps burn the bridge of creativity that he was a misanthrope more than passingly familiar with. Why would you be checking back on this one, but it's also pretty silly to literally gas people in GG probably relate, but not much clear exposure of serious wrongdoing. No matter what you would want to keep working at this point that the primary purpose of denigrating conservatives and (reportedly) conspiring to support the then-presidential candidate Barrack Obama. * Gizmodo – Gadget and technology lifestyle. 
