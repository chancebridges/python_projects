magicians = ['alice', 'david', 'carolina']
for magician in magicians:
 print(magician.title() + ", that was a great trick!")
print("I can't wait to see your next trick, " + magician.title() + ".\n")

# the print statement is not indented the second time, so it only recognizes the most recent "magician" value
