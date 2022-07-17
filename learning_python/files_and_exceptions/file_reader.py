with open('C:/Users/Chance Bridges/Desktop/python_work/learning_python/files_and_exceptions/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
    
# On line one you need to enter the path for python to find the file to open.
# You first need to open the file to do any work with a file. The open() 
# function needs one argument: the name of the file you want to open. 
# Python looks for this file in the directory where the program that's 
# currently being executed is stored. Here the open() function returns
# an object representing the file. Python stores this object in file_object
#, which we'll work with later in the program.

# The keyword 'with' closes the file once access to it is no longer needed. 

# once we have a file object representing pi_digits.txt, we use the read()
# method in the second line of our program to read the entire contents of the
# file and store it as one long string in contents. 

# when python prints the file it will print an extra blank line at the end of
# the output. If you want to remove the extra blank line, you can use rstrip()
# in the print statement.
# print(contents.rstrip())