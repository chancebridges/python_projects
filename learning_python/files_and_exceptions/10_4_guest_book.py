filename = 'C:/Users/Chance Bridges/Desktop/python_work/learning_python/files_and_exceptions/guest_book.txt'



print("Please enter your name below.")
print("When done enter: Done")
names = True
while names == True:
    name = input("Enter your name: ")
    if name == "Done":
        names = False
    else:
        print("Hello " +name)
        with open (filename, 'a') as file_object:
            file_object.write(str(name) + "\n")
