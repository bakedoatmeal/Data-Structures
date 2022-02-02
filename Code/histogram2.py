# from string import punctuation

def histogram_list(source_text):
    f = open(source_text, 'r')
    text = f.read()
    f.close()
    punctuation = '''!()-[]{\}\;:"”“\,<>./?@#$%^&*_~'''
    # remove posessives? 
    # change all text to lowercase
    text = text.lower()

    # remove punctuation
    for element in text:
        if element in punctuation:
            text = text.replace(element, "")

    # split into list of separate words
    all_words = text.split()
    histogram = []

    # loop through list of all words
    for word in all_words:
        word_found = False
        # loop through minilist and look for the word
        # if the word is found, increment count
        # if word is not in histogram, append it
        for minilist in histogram: 
            if minilist[0] == word: 
                minilist[1] += 1
                word_found = True
                break
        if word_found is False: 
            histogram.append([word, 1])

    return histogram

def unique_words(histogram):
    #return the count of unique words
    return len(histogram)

def frequency(word, histogram):
    #return the number of times that word appears in a text
    for minilist in histogram: 
        if minilist[0] == word.lower():
            return minilist[1]
    return 0

if __name__ == '__main__':
    hist = histogram_list('fish.txt') #dictionary {'one':1...}
    words = unique_words(hist)
    hist.sort(key = lambda x: x[0])
    print(hist)
    print(words)
    count = frequency('scandal', hist)
    print(count)
    
