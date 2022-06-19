current_users = ['alpha', 'beta', 'gamma','delta', 'epsilon']
new_users = ['delta', 'Epsilon', 'Chance', 'Brigett', 'Greyson']

new = [x.lower() for x in new_users]
current = [x.lower() for x in current_users]

for new_user in new:
    if new_user in current:
        print("Please enter a new username.")
    else:
        print("Username is available.")