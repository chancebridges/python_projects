# Let's move the bulk of the word counting program to a function called
# count_words(). By doing this it will be easier to run the analysis for
# multiple books. 

# reference word_count.py 

# Now we can write a simple loop to count the words in any text we want to
# analyze. We do this by storing the names of the files we want to analyze
# in a list, and then we call count_words() for each file in the list. 

def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, 'r', encoding='utf-8') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = 'Sorry, the file ' + filename + ' does not exist.'
        print(msg)
    else:
        # Count the approximate number of words in the file. 
        words = contents.split()
        num_words = len(words)
        print('The file ' + filename + ' has about ' + str(num_words) +
        ' words.')
        
book_1 = 'alice.txt'
book_2 = 'pizza.txt'
book_3 = 'adventures_of_sherlock_holmes.txt'

filenames = [book_1, book_2, book_3]
for filename in filenames:
    count_words(filename)