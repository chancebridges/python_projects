print("Welcome to the weight converter v1.0" + "\nPlease enter the measurment you are converting from below")
print("Please type either 'kg' or'lb'")
types= input("Format: ")
print("enter the numerical weight below.")
weight= input("weight: ")
if types == 'kg':
    print(int(weight) * 2.20462)
if types == 'lb':
    print(int(weight)/2.20462)
print("Thank you for using weight converter v1.0")
