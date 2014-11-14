from pymarkovchain import MarkovChain
import os.path

markovFile = "markov"
dataFile = "nov14.txt"

needs_build = not os.path.exists(markovFile)
mc = MarkovChain(markovFile)

if needs_build:
    with open(dataFile) as f:
        mc.generateDatabase(f.read())

def get_string():
    s = mc.generateString()
    while len(s) < 15:
        s = mc.generateString()
    return s + ". "

def ramble(length=10):
    return "".join([get_string()for _ in range(length)])
