# each time you use the input() function, you should include a clear, 
# easy to follow prompt that tells the user exactly what kind of info youre
# looking for. 
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")

# The operator += takes the string that was stored in prompt and adds the new string onto the end
