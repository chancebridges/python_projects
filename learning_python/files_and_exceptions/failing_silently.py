# sometimes you'll want the program to fail silently when an exception occurs
# and continue on as if nothing happened. To make a program fail silently, you
# write a try block as usual, but you explicitly tell python to do nothing in 
# the except block. 

# Python has a pass statement that tells it to do nothing in a block

def count_words(filename):
    """Count the appeoximate number of words in a file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        # Count approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)