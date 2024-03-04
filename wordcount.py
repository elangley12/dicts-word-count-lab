"""Count words in file."""

def get_word_count(text_file):                                      # define function that takes text file as parameter
    word_counts = {}                                                # make an empty dictionary
    
    for word in text_file:                                          # loop through text file word by word
        word_counts[word] = word_counts.get(word, 0) + 1            # add one for each word to new dictionary

    return word_counts


