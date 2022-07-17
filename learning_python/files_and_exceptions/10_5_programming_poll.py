filename = 'C:/Users/Chance Bridges/Desktop/python_work/learning_python/files_and_exceptions/responses.txt'

print("Please enter why you like programming below.")
print("When done enter: Done")
names = True
while names == True:
    name = input("Enter your reason: ")
    if name == "Done":
        names = False
    else:
        with open (filename, 'a') as file_object:
            file_object.write(str(name) + "\n")
