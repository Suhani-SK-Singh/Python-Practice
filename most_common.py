#Student name : Suhani
#Student number: 119220491

#A program to find most_common word in a string in alpahbetical order.

def most_common(text, n) :
    ##A Function to find most_common word in a string and return it in alpahbetical order.
    
    #Argument: text- represnt string to be considered. n-represents top "n" most common words.
    #returns: List of top "n" most common words present in the text in alphabetical order.
    
    
import string

words_frequency = {}


def most_common(text, n) :
    # Created a temporary text to manipulate text literal
    tmp_text = ''
    for char in text :
        if char in string.punctuation :
            tmp_text += ' '
        else :
            tmp_text += char

    # Made temporary text case insensitive
    tmp_text = tmp_text.casefold()

    words = [word for word in tmp_text.split() if len(word) > 0]
    for word in words :
        if word not in words_frequency :
            words_frequency[word] = 1
        else :
            words_frequency[word] += 1

    words_tuple = [(k, words_frequency[k]) for k in sorted(words_frequency, key=words_frequency.get, reverse=True)]
    highest_freq_tuple = words_tuple[0 : n]
    final_list = [i[0] for i in highest_freq_tuple]
    Sort_final=sorted(final_list)

    return Sort_final

