from pymarkovchain import MarkovChain
import os.path

markovFile = "markov"
dataFile = "nov14.txt"

needs_build = True
mc = MarkovChain()

if needs_build:
    with open(dataFile) as f:
        mc.generateDatabase(f.read())
        mc.dumpdb()

def get_string():
    s = mc.generateString()
    while len(s) < 15:
        s = mc.generateString()
    return s + ". "

def ramble(length=10):
    return "".join([get_string()for _ in range(length)])
