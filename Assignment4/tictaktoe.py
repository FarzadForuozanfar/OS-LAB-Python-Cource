from os import system
from time import time
import colorama
from colorama import Fore
import random

game_board = [['_']*3, ['_']*3, ['_']*3]

def Basic_game_table():
    for i in range(3):
        for j in range(i):
            print('_ _ _')
    print()


def is_tile_full(x, y):
    i = int(x)
    j = int(y)
    if game_board[i][j] != '_':
        return True
    else:
        return False

def Identify_the_winner():
    for i in range(3):
        digitX = 0
        digitO = 0
        for j in range(3):
            if game_board[i][j] == 'X':
                digitX +=1
            elif game_board[i][j] == 'O':
                digitO += 1
        if digitO == 3:
            return "second person"
        elif digitX == 3:
            return "first person"
    for i in range(3):
        digitX = 0
        digitO = 0
        for j in range(3):
            if game_board[j][i] == 'X':
                digitX += 1
            elif game_board[j][i] == 'O':
                digitO += 1
        if digitO == 3:
            return "second person"
        elif digitX == 3:
            return "first person"
    if game_board[0][0] == 'x' and game_board[1][1] == 'X' and game_board[2][2] == 'X' or game_board[0][2] == 'X' and game_board[1][1] == 'X' and game_board[2][0] == 'X':
        return "first person"
    elif game_board[0][0] == 'O' and game_board[1][1] == 'O' and game_board[2][2] == 'O' or game_board[0][2] == 'O' and game_board[1][1] == 'O' and game_board[2][0] == 'O':
        return "second person"

def The_game_draw():
    digit_blank = 0
    for i in range(3):
        for j in range(3):
            if game_board[i][j] == '_':
                digit_blank += 1
    if digit_blank == 0:
        return True
    else:
        return False

def Show_game_board(): 
    print()
    for i in range(3):
        for j in range(3):
            if game_board[i][j]=='X':
                print(Fore.YELLOW + 'X', end=' ')
                print(Fore.WHITE, end='')
            elif game_board[i][j]=='O':
                print(Fore.LIGHTMAGENTA_EX + 'O', end=' ')
                print(Fore.WHITE, end='')
            else:
                print('_', end=' ')
        print()

                
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Main //////////////////////////


print("             \n\n\\\\\\\\Welcome To Tic-Toc-Toe Game////\n\n")
slct = int(input("1- Play With Computer\n\n2- Play With Player\n"))
if slct == 1:
    t = time()
    Basic_game_table()
    while True:
        row = int(input("Enter a number for row ="))
        col = int(input("Enter a number for col ="))
        if 0 <= row-1 <= 2 and 0 <= col-1 <= 2:
            while is_tile_full(row-1, col-1):
                print("this tile is full plz ty again\n")
                row = int(input("Enter a number for row ="))
                col = int(input("Enter a number for col ="))

            game_board[row-1][col-1] = 'X'
            Show_game_board()
            
            if Identify_the_winner () == "first person":
                system ('clear')
                Show_game_board()
                print("🏆🏅Yeeeeeaaaah You won The Game🏅🏆")
                print(" Time :" ,round(time() - t, 2) , " seconds")
                exit()
            elif The_game_draw():
                system ('clear')
                Show_game_board()
                print(" !!! The Game Is Draw !!! ")
                print(" Time :" ,round(time() - t, 2) , " seconds")
                exit()
            cm_row = random.randint(0,2)
            cm_col = random.randint(0,2)
            while is_tile_full(cm_row,cm_col):
                cm_row = random.randint(0,2)
                cm_col = random.randint(0,2)
            game_board[cm_row][cm_col] = 'O'
            Show_game_board()
            if Identify_the_winner () == "second person":
                system ('clear')
                Show_game_board()
                print("Computer Won The Game")
                print(" Time :" ,round(time() - t, 2) , " seconds")
                exit()
            elif The_game_draw():
                system ('clear')
                Show_game_board()
                print(" !!! The Game Is Draw !!! ")
                print(" Time :" ,round(time() - t, 2) , " seconds")
                exit()
        else:
            print("choose correct number between 1 2 3")
elif slct == 2:
    t1 = time()
    Basic_game_table()
    while True:
        row = int(input("Player 1 Enter a number for row ="))
        col = int(input("Player 1 Enter a number for col ="))
        if 0 <= row-1 <= 2 and 0 <= col-1 <= 2:
            while is_tile_full(row-1, col-1):
                print("this tile is full plz ty again\n")
                row = int(input("Player 1 Enter a number for row ="))
                col = int(input("Player 1 Enter a number for col ="))

            game_board[row-1][col-1] = 'X'
            Show_game_board()
            print(Identify_the_winner())
            if Identify_the_winner () == "first person":
                system ('clear')
                Show_game_board()
                print("🏆🏅Player 1 won The Game🏅🏆")
                print(" Time :" ,round(time() - t1, 2) , " seconds")
                exit()
            elif The_game_draw():
                system ('clear')
                Show_game_board()
                print(" !!! The Game Is Draw !!! ")
                print(" Time :" ,round(time() - t1, 2) , " seconds")
                exit()
        row = int(input("Player 2 Enter a number for row ="))
        col = int(input("Player 2 Enter a number for col ="))
        if 0 <= row-1 <= 2 and 0 <= col-1 <= 2:
            while is_tile_full(row-1, col-1):
                print("this tile is full plz ty again\n")
                row = int(input("Player 2 Enter a number for row ="))
                col = int(input("Player 2 Enter a number for col ="))

            game_board[row-1][col-1] = 'O'
            Show_game_board()
            
            if Identify_the_winner () == "second person":
                system ('clear')
                Show_game_board()
                print("🏆🏅Player 2 won The Game🏅🏆")
                print(" Time :" ,round(time() - t1, 2) , " seconds")
                exit()
            elif The_game_draw():
                system ('clear')
                Show_game_board()
                print(" !!! The Game Is Draw !!! ")
                print(" Time :" ,round(time() - t1, 2) , " seconds")
                exit()
