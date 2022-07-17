# Handling errors correctly is especially important when the program has more
# work to do after the error occurs. This happens often in programs that prompt
# users for input. 

# We can make a program more error resistant by wrapping the line that might
# produce errors in a try-except block. 

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
        
# We ask python to try and complete the division operation in a try block 
# at line 16. 

# The except block at line 18 tells python how to respond when a 
# ZeroDivisionError arises.