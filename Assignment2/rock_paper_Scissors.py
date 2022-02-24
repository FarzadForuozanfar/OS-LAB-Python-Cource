import random
from typing import Counter
user_wins = 0
computer_wins = 0
Counter = 0
print("Welcome to the Rock✊,Paper✋,Scissors🤞,🎮Game🎮")
while (Counter < 5 ) :

    computer_number = random.randint(1,3)
    
    print("press number for play")
    print("1- Rock✊")
    print("2- Paper✋")
    print("3- Scissors🤞")
    print("4- Exit Program")
    user_number = int(input())
    Counter += 1
    #1= Rock 2=Paper 3-Scissor
    
    if(user_number == computer_number):
        print("To equalize")
    elif(user_number == 1 and computer_number == 3 or user_number == 2 and computer_number == 1 or user_number == 3 and computer_number == 2 and Counter < 5):
        user_wins +=1
        print("You win !!! AND Your score :",user_wins," AND Computer Score :",computer_wins)
    elif(user_number == 1 and computer_number == 2 or user_number == 2 and computer_number == 3 or user_number == 3 and computer_number == 1 and Counter < 5):
        computer_wins += 1
        print("You lose !!! AND Your score :",user_wins," AND Computer Score :",computer_wins)
    elif(user_number == 4):
        print("Game Over")
        break
    else:
        print("Your command not found plz try again")
    if(Counter == 5):
        if(user_wins > computer_wins):
            print("💪😍You Win This Game😍💪")
            print("Your Score :",user_wins)
            print("Computer Score :",computer_wins)
        elif(user_wins < computer_wins):
            print("❌😭You Lost This Game😭❌")
            print("Your Score :",user_wins)
            print("Computer Score :",computer_wins)
        elif(user_wins == computer_wins):
            print("The game equalised")
            print("Your Score :",user_wins)
            print("Computer Score :",computer_wins)
        print("🎌The Game Is Over🎌")
        break

        