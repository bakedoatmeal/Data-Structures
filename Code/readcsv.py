import csv
from tokens import tokenize

def read_csv(filename):
  with open(filename, mode='r') as infile:
    reader = csv.reader(infile)
    dict = {}
    for character, line in reader:
      if character not in dict: 
        dict[character] = line
      else: 
        dict[character] += " " + line
  return dict

if __name__ == '__main__':
  simpsonsDict = read_csv('./simpsons_dataset.csv')
  print(tokenize(simpsonsDict['Homer Simpson']))