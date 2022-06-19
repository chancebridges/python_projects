magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# "for" indicates that we are doing a loop
# think of it like "for every magician in the list of magicians, print the magicians name"
# when using a loop the set of steps is repeated once for each item in the list

for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you, everyone. That was a great magic show!")
