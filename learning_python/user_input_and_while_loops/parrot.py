# we'll define a quit value and then keep the program running as long as the 
# user has not entered the quit value
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

# this works well except that it prints the word 'quit' as if it were an actual message
# refer to parrot 2.0 for how to fix this
