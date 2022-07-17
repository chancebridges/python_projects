import os
learning = '10_1_learning_python.txt'
#learning = 'C:\\Users\\Chance Bridges\\Desktop\\python_work\\learning_python\\files_and_exceptions\\10_1_learning_python.txt'

with open(learning, 'r') as file:
    filedata = file.read()
    
filedata = filedata.replace('python', 'C')

with open(learning, 'w') as file:
    file.write(filedata)

print(filedata)
