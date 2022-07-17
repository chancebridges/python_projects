filename = 'C:/Users/Chance Bridges/Desktop/python_work/learning_python/files_and_exceptions/programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
    
    # The call to open() in this example has two arguments on line 3, the 
    # first argument is still the name of the file we want to open. The second
    # argument, 'w', tells python that we want to open the file in write mode. 
    # you can open a file in read mode('r'), write mode('w'), append mode ('a'),
    # or a mode that allows you to read and write to the file ('r+'). If you 
    # omit the mode argument, python opens the file in read-only mode by default

#The open function automatically creates the file you're writing to if it does
# not already exist. 

# be careful opening a file in write mode ('w') because if the file does exist,
# python will erase the file before returning the file object.

# at line 4 we use the write() method on the file object to write a string
# to the file. This program has no terminal output, but if you open the file
# programming.txt, you'll see one line: "I love programming."

# Python can only write strings to a text file. If you want to store numberical
# data in a text file, you'll have to convert the data to a string format using
# the str() function.