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


print('Oh no! I only have room for two guests!')

shrunk_guests = invite_list.pop(0)
print(shrunk_guests)
print("Sorry Justen Mantz I can not invite you to dinner")
print(invite_list)
invite_list.pop()
print("Sorry Justin Singer, I can not invite you to dinner")
print(invite_list)
invite_list.pop()
print("Sorry Ryan Reynolds, I can not invite you to dinner")
invite_list.pop()
print("Sorry Brigett Phillips, I can not invite you to dinner")
print(invite_list)
print( "Hello, " + invite_list[0] + " You are still invited to my diner")
print( "Hello, " + invite_list[1] + " You are still invited to my dinner")

del invite_list[0]
del invite_list[0]
print(invite_list)



