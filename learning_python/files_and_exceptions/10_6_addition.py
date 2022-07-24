"""Add two numbers together and catch the TypeError that occurs if text 
is inputted."""
import os
def test():
    dirname = os.path.dirname(__file__)
    print(os.getcwd())
    #filename = os.path.join(dirname, 'relative/path/to/file/you/want')

def main():
    while True:
        try:
            num_1 = (input("Please enter the first number to add: "))
            num_1 = int(num_1)
            num_2 = (input("Please enter the first number to add: "))
            num_2 = int(num_2)
        except ValueError:
            print("You must enter a valid number")
        else:
            print("You number was: " + str(num_1))

if __name__ == "__main__":
    test()
