filename = 'C:/Users/Chance Bridges/Desktop/python_work/learning_python/files_and_exceptions/guest.txt'
name = input("Please enter your name: ")
with open(filename, 'w') as file_object:
    file_object.write(name)