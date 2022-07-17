#When you use 'with', the file object returned by open() is only available 
# inside the 'with' block that contains it. If you want to retain access
# to a file's contents outside the with block, you can store the file's lines
# in a list inside the block and then work with that list.

# You can process parts of the file immediately and postpone some processing
# for later in the program.

# The following example stores the lines of pi_digits.txt in a list inside
# the with block and then prints the lines outisde the with block. 

filename = 'C:/Users/Chance Bridges/Desktop/python_work/learning_python/files_and_exceptions/pi_digits.txt'
#filename = '/Users/Chance Bridges/Desktop/python_work/learning_python/files_and_exceptions/pi_digits.txt'
with open(filename) as file_object:
    lines  = file_object.readlines()

for line in lines:
    print(line.rstrip())
    
# at line 15 the readlines() method takes each line from the file and stores it
# in a list. This list is then stored in 'lines', which we can continue to work
# with after the with block ends.

# at line 17 we use a simple for loop to print each line from lines. Because 
# each line corresponds to each line in the file, the output matches the 
# contents of the file exactly. 