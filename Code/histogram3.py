from string import punctuation


def histogram_counts(source_text):
    f = open(source_text, 'r')
    text = f.read()
    f.close()
    punctuation = '''!()-[]{\}\;:'"\,<>./?@#$%^&*_~'''
    # change all text to lowercase
    text = text.lower()

    # remove all punctuation
    for element in text:
        if element in punctuation:
            text = text.replace(element, "")

    # split text into list of separate words
    all_words = text.split()
    histogram = []

    for word in all_words:
        word_found = False
        # for each word, loop through histogram and check if word is in tuple
        for index in range(len(histogram)): 
            if word in histogram[index][1]: 
                # if word is found, we need to remove it and add it to the next tuple
                histogram[index][1].remove(word)
                if index + 1 < len(histogram):
                    histogram[index+1][1].append(word)
                else: 
                    histogram.append((index+2, [word]))
                word_found = True
                break
        # if this is the first time seeing a word, add to first tuple
        if word_found is False:
            if len(histogram) == 0:
                histogram.append((1, [word]))
            else: 
                histogram[0][1].append(word)

    return histogram

def unique_words(histogram):
    #return the count of unique words
    count = 0
    for tuple in histogram:
        count += len(tuple[1])
    return count

def frequency(word, histogram):
    #return the number of times that word appears in a text
    for tuple in histogram: 
        if word.lower() in tuple[1]: 
            return tuple[0]

if __name__ == '__main__':
    hist = histogram_counts('fish.txt') #dictionary {'one':1...}
    words = unique_words(hist)
    # hist.sort(key = lambda x: x[0])
    print(hist)
    print(words)
    count = frequency('blue', hist)
    print(count)
    
