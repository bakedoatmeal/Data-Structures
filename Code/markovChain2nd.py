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
text2 = read_file("./sanderson.txt")

def build(word_list):
  markovchain = {}
  if len(word_list) < 2:
    return   

  for index in range(len(word_list)-2):
    first_word = word_list[index]
    second_word = word_list[index + 1]
    third_word = word_list[index + 2]
    window = (first_word, second_word)
    if window not in markovchain:
      markovchain[window] = Dictogram()
    markovchain[window].add_count((second_word, third_word))
  # print(markovchain)
  return markovchain
    
chain = build(text2)

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
  
  print(sentence)

write_sentence(20, chain)
# print(len(chain.keys()))