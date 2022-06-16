# to check whether two conditions are both true simultaneously, use the 
#keyword and to combine two conditional tests. If each test passes, the 
#overall expression evaluates to True. If either test fails, or if both tests
# fail, the expression evaluates to False

age_0 = 22
age_1 = 18
print(age_0 >=21 and age_1 >= 21)

age_1 = 22
print((age_0 >=21) and (age_1 >=21))
