"""Count words in file."""

def get_word_count(text_file):                                      # define function that takes text file as parameter
    
    text_file = open(text_file)                                     # open text file for iteration later
    word_counts = {}                                                # make an empty dictionary
    
    for line in text_file:                                          # parse through each line of the text file
        words = line.rstrip().split()
        for word in words:                                          # loop through text file word by word
            word_counts[word] = word_counts.get(word, 0) + 1        # add one for each word to new dictionary
    for key, value in word_counts():
        print(f"{key}, {value}")

    # return word_counts


