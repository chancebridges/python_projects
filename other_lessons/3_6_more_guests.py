invite_list = ['elon musk', 'brigett phillips', 'ryan reynolds']
invite = 'Hello, '
invite_end = ' you have been invited to a dinner with Chance. Lucky you!'
print(invite + invite_list[0].title() + invite_end)
print(invite + invite_list[1].title() + invite_end)
print(invite + invite_list[-1].title() + invite_end)

invite_list.insert(0,'Justen Mantz')
print(invite_list)

invite_list.insert(2,"Nick Connar")
print(invite_list)

invite_list.append('Justin Singer')
print(invite_list)

print(invite + invite_list[0].title() + invite_end)
print(invite + invite_list[1].title() + invite_end)
print(invite + invite_list[2].title() + invite_end)
print(invite + invite_list[-1].title() + invite_end)
print(invite + invite_list[-2].title() + invite_end)
print(invite + invite_list[-3].title() + invite_end)
