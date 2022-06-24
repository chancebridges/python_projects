# for a program that should run only as long as many conditions are true, you 
# can define one variable that determines whether or not the entire program is
# active. This varuable, called a flag, acts as a signal to the program

# we can write our programs so that they run while the flag is set to True
# and stop running when any of several events sets the value fo the flag to False

# as a result of this our while statement needs to check only one condition: 
# whether or not the flag is currently True

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)