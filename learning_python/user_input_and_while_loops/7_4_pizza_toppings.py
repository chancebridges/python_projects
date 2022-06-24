prompt = "Please enter the toppings you would like on your pizza: "
prompt += "\n If you are done then enter 'quit'"
print(prompt)
message = ""
while message != 'quit':
    topping = input('topping: ')
    if topping == 'quit':
        break
    else:
         message = topping
         print("We will add " + message + " to your pizza.")
    