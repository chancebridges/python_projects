class User():
    """Describes a person."""
    def __init__(self, first_name, last_name, **other):
        """Describes the first and last name of a person."""
        profile = {}
        profile['first_name'] = last_name
        profile['last_name'] = last_name
        for key, value in other.items():
            profile[key] = value

    def describe_user(self):
        print(profile)
    
    def greet_user(self):
        print("Hello, " +first_name)

myself = User('Chance','Bridges',age='twenty-four', sex='male')
print(myself.first_name.title())


