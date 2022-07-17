# When you are reading a file, you will often want to examine each line 
# of the file. 

# you can use a for loop on the file object to examine each line frmo a file
# one at a time. 

filename = 'C:/Users/Chance Bridges/Desktop/python_work/learning_python/files_and_exceptions/pi_digits.txt'

with open (filename) as file_object:
    for line in file_object:
        print(line)
        #print(line.rstrip))

# At line 7 we store the name of the file we are reading from in the variable
# filename. This is a commom convention when working with files. Because
# the variable filename does not represent the actual file, its just a string
# telling python where to find the file - you can easily swap out the path for
# another path of another file you want to work with. 

# At line 9 after we call open(), an object representing the file and its 
# contents is stored in the variable file_object

# Even more blank lines appear when running this becuase an invisible newline
# character is at the end of each line in the text file. 
# reference line 12 for the added rstrip() that will get rid of all the white
# space. 