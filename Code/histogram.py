def histogram_dict(source_text):
    f = open(source_text, 'r')
    text = f.read()
    f.close()
    text = text.lower()
    punctuation = '''!()-[]{\}\;:"”“\,<>./?@#$%^&*_~'''
    histogram = {}

    # remove punctuation
    for element in text:
        if element in punctuation:
            text = text.replace(element, "")

    all_words = text.split()

    # loop through list of all words
    # if word is already in histogram, increment count
    # else, add word to histogram
    for word in all_words:
        if word in histogram:
            histogram[word] += 1
        else: 
            histogram[word] = 1
    
    #return histogram as a dictionary
    return histogram

def unique_words(histogram):
    #return the count of unique words
    return len(histogram.keys())

def frequency(word, histogram):
    #return the number of times that word appears in a text
    if word.lower() in histogram:
        return histogram[word.lower()]
    else:
        return 0

if __name__ == '__main__':
    hist = histogram_dict('sampletext.txt') #dictionary {'one':1...}
    print(hist)
    words = unique_words(hist)
    print(words)
    count = frequency('Red', hist)
    print(count)
    
