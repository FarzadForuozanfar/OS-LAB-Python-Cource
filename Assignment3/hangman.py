import random

word_bank = ["tree", "book", "python", "sadjad", "linux", "mac", "oslab", "windows", "java"]
word = random.choice(word_bank)


joon = len(word_bank+1)

user_true_chars = []

while True:
    IS_WIN = True
    for char in word:
        if char in user_true_chars:
            print(char, end="")
        else:
            print("-", end="")
            IS_WIN = False

    if IS_WIN:
        print("\n\n You won the game.")
        break

    user_char = input("\nEnter a character: ")

    if user_char in word:
        print("✅")
        user_true_chars.append(user_char)
    else:
        joon -= 1
        print("❌")
    if joon == 0:
        print("\nGame over.")
        break