filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
    
# In this example, the code in the try block produces a FileNotFoundError, 
# so python looks for an except block that matches that error. 