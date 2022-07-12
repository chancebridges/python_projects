current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 ==0:
        continue

    print(current_number)

# once inside the while loop we increment the count by one
# the if statement then checks the module of the number and 2, if the modulo is 0
# then the continue statement tells python to ignore the rest of the loop 
# and return to the beginning