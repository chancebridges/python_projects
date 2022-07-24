
import os
filename = '/alice.txt'
directory = os.getcwd()

try:
    with open(directory + filename) as file:
        while True:
            char = file.read(1)
            if not char:
                break
            if not char.isascii():
                print("Character is not ascii: " + char)
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)