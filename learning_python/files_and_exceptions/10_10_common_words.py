
def count_words(filename):
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
        print("The file iliad.txt has the word 'the' " + str(contents.count('The')) + ' many times.')

        
filename = 'iliad.txt'
count_words(filename)