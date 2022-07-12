def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}      # we make a dictionary to hold the user's profile
    profile['first_nale'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value 
    return profile

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                              field='physics')

print(user_profile)


# The definition of build_profile() expects a first and last name, and then
# allows the user to pass in as many name-value pairs as they want

# the double asterisks before the parameter **user_info cause python to create
# an empty dictionary called user_info and pack whatever name-value pairs
# it receives into this dictionary. 

# within the function you can access the name-value pairs in user_info as 
# you would for any dictionary. 

# 