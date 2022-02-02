import random, sys

words = sys.argv[1:]

def rearrange():
    #shuffle list
    random.shuffle(words)
    #put together into a string
    shuffled = " ".join(words)
    print(shuffled)

rearrange()