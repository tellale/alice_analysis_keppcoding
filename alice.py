import nltk
import matplotlib.pyplot as plt


def remove_stopwords(text, stopwords):
    """Takes a list and a set and removes everything present on the list from the set.
    Returns a new list."""
    remainder = []
    for word in text:
        if word not in stopwords:
            remainder.append(word)
    return remainder

def remove_non_alphabetic(text):
    """Removes all non alphabetic characters from a list."""
    results = []
    for word in text:
        if word.isalpha():
            results.append(word)
    return results

def count_words(list_words):
    """Takes a list of words and returns a dictionary with the count of how many times a word appears in the list of words.
    """
    count_words = {}
    # go through the list of words
    for word in list_words:
    #check if the word if on the dict
        if word in count_words.keys():
            count_words[word] += 1
    #add to count if it is
        else:
            count_words[word] = 1
    #if not, add to dict with value 1
    return count_words

def word_probability(dict_words):
    """ Gets a dict of words with values and returns another dict with the same keys, but the values are the probability of each.
    """
    #iterate through a dict
    probability = {}
    for key, value in dict_words.items():
    #divide the value of each element with the total number of elements
        prob = value / (sum(dict_words.values()))
        prob = prob * 100
        probability[key] = prob
    return probability

def sort_percentages(dict):
    sorted_dict = {}
    sorted_keys = sorted(dict, key=dict.get)

    for k in sorted_keys:
        sorted_dict[k] = dict[k]
    return sorted_dict

def display_histogram(dict_probs):
    fig, ax = plt.subplots()

    words = dict_probs.keys()
    counts = dict_probs.values()
    bar_labels = len(dict_probs)
    bar_colors = ['tab:pink']

    ax.bar(words, counts, label=bar_labels, color=bar_colors)

    ax.set_ylabel('Probability')
    ax.set_title('Probability of word to appear')
    #ax.legend(title='Fruit color')

    plt.show()

#Opens and tokenize the .txt files - Alice in Wonderland
file_text = open('alice_text.txt', encoding='utf8')
alice_text = file_text.read()
alice_text = alice_text.lower()
tokens = nltk.word_tokenize(alice_text)

#Opens and tokenize the .txt file - stopwords in English
file_stopwords = open('stopwords.txt', encoding='utf8')
stopwords = file_stopwords.read()
tokens_stopwords = nltk.word_tokenize(stopwords)

#Creates a set of the list tokens_stopswords.
stopwords_set = set(tokens_stopwords)

#Remove stopwords from Alice text and puts the clean text in a new list
without_stopwords = remove_stopwords(tokens, stopwords_set)

#removes all non alphanetic words from the clean Alice text --> Punctuation, apostrophes. 
clean_words = remove_non_alphabetic(without_stopwords)

#Create a dict to count the apperance of a word
count = count_words(clean_words)

#Takes the previous dict and calculates the probability of a word to appear in the text --> count of apperances / total lenght of text
probability = word_probability(count)

#Sorts the dict by smallest probability to biggest probability
sorted_dict = sort_percentages(probability)
print(sorted_dict)

#Prints a histogram to visualize data
display_histogram(sorted_dict)

