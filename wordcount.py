def get_word_count(text_file):                                      # define function that takes text file as parameter
    """Count words in a text file."""

    text_file = open(text_file)                                     # open text file for iteration later
    word_counts = {}                                                # make an empty dictionary
    
    for line in text_file:                                          # parse through each line of the text file
        words = line.rstrip().split()                               # remove each word, one line at a time
        for word in words:                                          # loop through text file word by word
            word_counts[word] = word_counts.get(word, 0) + 1        # add one for each word to new dictionary
    
    for key, value in word_counts.items():                          # loop over each key value pair in word_counts
        print(f"{key} {value}")                                     # print each key value pair on separate lines


