alien_color = ['green']

if 'green' in alien_color:
    print("You get 5 points!")
else:
    print("You get 10 points!")

alien_color[0] = 'red'

if 'green' in alien_color:
    print("You get 5 points!")
else:
    print("You get 10 points!")