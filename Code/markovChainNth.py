from dictogram import Dictogram
import random
from readtext import read_file
from tokens import tokenize
from readcsv import read_csv

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


def build(word_list, n):
  markovchain = {}
  if len(word_list) < n:
    return {}  

  window = word_list[0:n:1]
  index = n - 1

  for index in range(len(word_list)-n):
    # first_word = word_list[index]
    # second_word = word_list[index + 1]
    # third_word = word_list[index + 2]
    first_tuple = tuple(window)
    if first_tuple not in markovchain:
      markovchain[first_tuple] = Dictogram()
    index += 1
    window.pop(0)
    window.append(word_list[index])
    markovchain[first_tuple].add_count(tuple(window))
  # print(markovchain)
  return markovchain
    

"""
create markov chain dict
for three words at a time in wordlist:
  see if tuple of first two words are in markovchain
  if not
    add tuple of first two words to markovchain, value is a hictogram  
  markovchain[tuple of first two words].add_count(tuple of second and third word)
"""

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
  # print(markovchain.keys())
  first_pair = random.choice(list(markovchain.keys()))
  sentence = first_pair[0]

  while wordcount < length:
    next_pair = markovchain[first_pair].sample()
    sentence += f' {next_pair[1]}'
    first_pair = next_pair

    if first_pair not in markovchain:
      first_pair = random.choice(list(markovchain.keys()))

    wordcount += 1
  return sentence

if __name__ == '__main__':
  text = 'Let’s look at a concrete example. Say we start at state A. Our first random choice is between states man and dog,, each with probability 1/2 - say we take dog,. Now we don’t have any choice,'.split(' ')
  text2 = read_file("./sanderson.txt")

  simpsonsDict = read_csv('./simpsons_dataset.csv')
  text3 = tokenize(simpsonsDict['Homer Simpson'])
  chain = build(text3, 3)
  sentence = write_sentence(20, chain)
  print(sentence)
# print(len(chain.keys()))
