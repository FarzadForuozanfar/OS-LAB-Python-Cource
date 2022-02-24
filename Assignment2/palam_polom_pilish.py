import random
from os import system
user_wins = 0
computer1_wins = 0
computer2_wins = 0
counter_ = 0
round_ = 1
print("Welcome To The ✋🎮🤚  Palam,Polom,Plish   Game✋🎮🤚")
while counter_ < 5:
    computer1_select = random.randint(1,2)
    computer2_select = random.randint(1,2)
    print("Choose Your Act")
    print("1- On Hand ✋")
    print("2- Back Hand🤚")
    user_select = int(input())
    counter_ += 1
    if(user_select == 1 and computer2_select == 2 and computer1_select == 2 or user_select == 2 and computer2_select == 1 and computer1_select == 1):
        user_wins += 1
        print("!! You Win !! Round :",round_)
        print("user score :",user_wins)
        print("computer 1 score :",computer1_wins)
        print("computer 2 score :",computer2_wins)
    elif(user_select == 1 and computer2_select == 2 and computer1_select == 1 or user_select == 2 and computer2_select == 1 and computer1_select == 2):
        computer2_wins += 1
        print("!! computer 2 Win !! Round :",round_)
        print("user score :",user_wins)
        print("computer 1 score :",computer1_wins)
        print("computer 2 score :",computer2_wins)
    elif(user_select == 1 and computer2_select == 1 and computer1_select == 2 or user_select == 2 and computer2_select == 2 and computer1_select == 1):
        computer2_wins += 1
        print("!! computer 1 Win !! Round :",round_)
        print("user score :",user_wins)
        print("computer 1 score :",computer1_wins)
        print("computer 2 score :",computer2_wins)
    elif(user_select == computer1_select == computer2_select):
        print("!! match equalised !! Round!:",round_)
        print("user score :",user_wins)
        print("computer 1 score :",computer1_wins)
        print("computer 2 score :",computer2_wins)
    else:
        print("command not found")
        round_ -=1
    round_ += 1
    if(counter_ == 5):
        system('clear')
        if(user_wins > computer2_wins and user_wins > computer1_wins):
            print("   Congratulations   ")
            print("   !! You Win This Game !!  ")
            print("user score :",user_wins)
            print("computer 1 score :",computer1_wins)
            print("computer 2 score :",computer2_wins)
            break
        elif(user_wins < computer2_wins and computer2_wins > computer1_wins):
            print("   !! You Lost This Game !!  ")
            print("Computer 2 Has Won Match")
            print("user score :",user_wins)
            print("computer 1 score :",computer1_wins)
            print("computer 2 score :",computer2_wins)
            break
        elif(user_wins < computer1_wins and computer2_wins < computer1_wins):
            print("   !! You Lost This Game !!  ")
            print("Computer 1 Has Won Match")
            print("user score :",user_wins)
            print("computer 1 score :",computer1_wins)
            print("computer 2 score :",computer2_wins)
            break
        elif(user_wins == computer1_wins or user_wins == computer2_wins or computer2_wins == computer1_wins):
            print("  !! This Match is Equalised  !!")
            print("user score :",user_wins)
            print("computer 1 score :",computer1_wins)
            print("computer 2 score :",computer2_wins)
            break
        break

