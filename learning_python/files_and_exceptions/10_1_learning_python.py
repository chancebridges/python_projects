learning = 'C:\\Users\\Chance Bridges\\Desktop\\python_work\\learning_python\\files_and_exceptions\\10_1_learning_python.txt'

with open(learning) as learning_py:
    lines = learning_py.readlines()
    lines_2 = learning_py.read()
    #for py in learning_py:
     #   print(py)

learn = ''
for line in lines:
    learn+= line
for x in range(0,3):
    print(learn)
    print("\n")
    
print(lines_2)