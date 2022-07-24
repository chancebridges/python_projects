filename_1 = 'learning_python/files_and_exceptions/cats.txt'
filename_2 = 'learning_python/files_and_exceptions/dogs.txt'
try:
    with open(filename_1, 'r') as file_1:
        print(file_1.read())
    with open(filename_2, 'r') as file_2:
        print(file_2.read())
except FileNotFoundError:
    print("Sorry, the file was not found.")
