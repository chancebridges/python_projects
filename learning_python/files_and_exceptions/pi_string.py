filename = 'C:/Users/Chance Bridges/Desktop/python_work/learning_python/files_and_exceptions/pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# We start by opening the file and storing each line of digits in a list, 
# just as we did previously. at line 6 we create a varaible to hold to digits
# of pi.

# At line 7 we then create a loop that adds each line of digits to pi_string and
# removes the newline character from each line. 

# When python reads from a text file, it interprets all text in the file as 
# a string. If you read in a number and want to work with that value in a 
# numreical context, you'll have to convert it to an integer using the int()
# function or convert it to a float using the float() function. 