invite_list = ['elon musk', 'brigett phillips', 'ryan reynolds']
invite = 'Hello, '
invite_end = ' you have been invited to a dinner with Chance. Lucky you!'
print(invite + invite_list[0].title() + invite_end)
print(invite + invite_list[1].title() + invite_end)
print(invite + invite_list[-1].title() + invite_end)

print('Oh no! ' + invite_list[0].title() + " won't be able to make it!")

invite_list[0] = 'George Washington'

print(invite + invite_list[0].title() + invite_end)
print(invite + invite_list[1].title() + invite_end)
print(invite + invite_list[-1].title() + invite_end)
