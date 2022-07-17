# When you think an error may occur, you can write a try-except block to 
# handle the exception that might be raised. You tell python to try running 
# some code, and you tell it what to do if the code results in a particular
# kind of exception. 

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# If the code inside a try block works, pytohn skips over the except block.

# If the code in the try block causes an error, python looks for an except 
# block whose error matches the one that was raised and runs the code in 
# that block. 

# if more code followed the try-except block, the program would countinue
# running because we told python how to handle the error. 

# Python attempts to run the code in the try statement. The only code that 
# should go in a try statement is code that might cause an exception to be raised.
# Sometime's you will have additional code that should run only if the try block 
# was successful; this code goes in the else block. The except block tells python
# what to do in case a certain exception arises when it tries to run the code in
# the try statement. 