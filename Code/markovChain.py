from dictogram import Dictogram
import random
from readtext import read_file

# 1: build Markov chain
"""
markovchain = {}
loop through words 
  for each (firstword, secondword): 
    if firstword is not in markovchain, add it {}
    if secondword is not in hist of firstword, add it
    else
      markovchain[firstword][secondword] += 1
    
"""
text = 'Let’s look at a concrete example. Say we start at state A. Our first random choice is between states man and dog,, each with probability 1/2 - say we take dog,. Now we don’t have any choice,'.split(' ')
text2 = read_file("./kanye.txt")

def build(word_list):
  markovchain = {}
  for index in range(len(word_list)-1):
    firstword = word_list[index]
    secondword = word_list[index+1]
    if firstword not in markovchain:
      markovchain[firstword] = Dictogram()
    markovchain[firstword].add_count(secondword)
  print(markovchain)
  return markovchain
    
chain = build(text2)

# 2: Walk on chain
"""
do we need a hist of the whole text? 
sentence = "" 

find a random starting word 
firstword = randomword

while length of sentence less than desired length
  nextword = markovchain[firstword].sample()
  sentence += nextword
  firstword = nextword


"""
def write_sentence(length, markovchain):
  wordcount = 0
  print(markovchain.keys())
  firstword = random.choice(list(markovchain.keys()))
  sentence = firstword

  while wordcount < length:
    nextword = markovchain[firstword].sample()
    sentence += f' {nextword}'
    firstword = nextword

    if firstword not in markovchain:
      firstword = random.choice(list(markovchain.keys()))

    wordcount += 1
  
  print(sentence)

write_sentence(20, chain)
print(len(chain.keys()))