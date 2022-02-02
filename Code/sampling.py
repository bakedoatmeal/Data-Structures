import random

def getOneWord(hist):
  words = list(hist.keys())
  return random.choice(words)

def getWeightedWord(hist):
  totalWords = 0
  for number in hist.values(): 
    totalWords += number
  # print(f"Total words: {totalWords}")

  random_index = random.randint(1, totalWords)
  # print(f"Number: {random_index}")

  #find word 
  where_current_goalpost_ends = 0
  for word in hist.keys():
    where_current_goalpost_ends += hist[word]
    if where_current_goalpost_ends >= random_index: 
      return word

  # [one, fish, fish, fish, fish, two, red, blue]

def test(hist, numberOfTests):
  results = {}
  for i in range(numberOfTests):
    word = getWeightedWord(hist)
    if word in results: 
      results[word] += 1
    else: 
      results[word] = 1
  print(results)

if __name__ == '__main__':  
  hist = {
    'one': 1,
    'fish': 4,
    'two': 1, 
    'red': 1,
    'blue': 1
    }

  hist_list = [
    ['one', 1], 
    ['two', 1], 
    ['fish', 1], 
    ['fish', 1], 
    ['fish', 1],
    ['fish', 1]
  ]
  
  print(getWeightedWord(hist))
  test(hist, 10000)