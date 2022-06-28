def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# The function combines the two names and adds a space between them.
# in line 4 the value of full_name is converted to title case, and then 
# returned to the calling line 

