# sometimes it makes sense to make an argument so that people using
# the function can choose to provide extra information only if they want to. 

# what if you want a function that can add a middle name but is okay without one too

def get_formatted_name(first_name, last_name, middle_name = ''):
    """Return a full, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)