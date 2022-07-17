filename = 'C:/Users/Chance Bridges/Desktop/python_work/learning_python/files_and_exceptions/programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a broswer.\n")

# at line 3 we use the 'a' argument to open the file for appending rather
# than writing over the existing file.

# at line 4 we write two new lines, which are added to programming.txt
