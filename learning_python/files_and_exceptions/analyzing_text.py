# You can analyze text files containing entire books. Many classic works of
# literature are available as simple text files because they are in the public 
# domain. 

# Lets pull in the text of Alice in Wonderland and try to count the number
# of words in the text. We will use the string method split(), which can build
# a list of words from a string. Below is an example of this being used. 

#title = 'Alice in Wonderland'
#print(title.split())

# The split() method separates a string into parts whereverv it finds a space
# and stores all the parts of the string in a list. 

filename = 'C:\\Users\\Chance Bridges\\Desktop\\python_work\\alice.txt'

try:
    with open(filename, 'r', encoding='utf-8') as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    # Count the approximate number of words in the file
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")

# At line 25 we take the string contents, now containing the entire text of 
# alice in wonderland as one long string, and use the split() method to 
# produce a list of all the words in the book. 

# When we use len() on this list to examine its length, we get a good 
# approximation of the number of words in the original string. line 26

