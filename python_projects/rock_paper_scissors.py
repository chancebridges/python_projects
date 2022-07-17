# This will be a basic rock paper scissors game facing the computer.
from random import randint

print("Welcome to rock-paper-scissors v1.0")
print("please email cbridges98@protonmail.com with any concerns or problems.")
print("\nWould you like to play rock-paper-scissors?")

game = ''

while game =='':
    start_program = input("Please enter 'yes' or 'no': ")
    if start_program == 'no':
        game = False
    elif start_program == 'yes':
        game = True
    else:
        print("I'm sorry I don't understand, please enter 'yes' or 'no'.")
        continue

num_of_games = input("Please enter the number of games you'd like to play: " )


for x in range(0,int(num_of_games)):
    print("Please enter 'rock', 'paper', or 'scissors'")
    selection = input("Choice: ")
    
    ai = randint(0,3)
    if ai == 0:
        ai_selection = 'rock'
    elif ai == 1:
        ai_selection = 'paper'
    elif ai == 2:
        ai_selection = 'scissors'
        
    if selection == 'rock':
        if ai_selection == 'rock':
            print("The computer chose rock, its a tie")
        elif ai_selection == 'paper':
            print("The computer chose paper, you lose.")
        elif ai_selection == 'scissors':
            print("The computer chose scissors, you win!")
    elif selection == 'paper':
        if ai_selection == 'rock':
            print("The computer chose rock, you win!")
        elif ai_selection == 'paper':
            print("The computer chose paper, its a tie.")
        elif ai_selection == 'scissors':
            print("The computer chose scissors, you lose.")
    elif selection == 'scissors':
        if ai_selection == 'rock':
            print("The computer chose rock, you lose.")
        if ai_selection == 'paper':
            print("The computer chose paper, you win!")
        if ai_selection == 'scissors':
            print("The computer chose scissors, its a tie.")
    
    