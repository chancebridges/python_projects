def show_magicians(our_list):
    for value in our_list:
        print(value)

def make_great(our_list):
    for i in range(len(our_list)):
        our_list[i] = our_list[i] + " the Great"

magicians= ['houdini', 'niel patrick harris', 'davinci']
new_magicians = magicians[:]
make_great(new_magicians)
show_magicians(new_magicians)

print(magicians)