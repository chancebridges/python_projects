age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

# the elif line at line 5 is another if test, which only runs if the previous 
# test failed. at this point in the chain we know the person is at least four
# years old because the first test failed. if both the if and elif tests fail, 
# python runs the code in the else block. 

