def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}      # we make a dictionary to hold the user's profile
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value 
    return profile

user_profile = build_profile('Chance', 'Bridges',
                            age='24',
                            sex='male',
                            state='Indiana')

print(user_profile)

