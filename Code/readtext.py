def read_file(filename):
  word_list = []
  with open(filename, 'r') as f:
  #   for line in f:
  #     line = line.lower()
  #     words = line.split(' ')
  #     for word in words:
  #       # if element in punctuation:
  #       #   text = text.replace(element, "")
  #       word_list.append(word)
    text = f.read()
    text = text.replace("\n", " ")
    text = text.lower()

    punctuation = '''!()-[]{\}\;:"”“\,<>./?@#$%^&*_~'''

    # remove punctuation
    for element in text:
        if element in punctuation:
            text = text.replace(element, "")
    
    word_list = text.split(' ')
    # print(word_list)
  return word_list
  