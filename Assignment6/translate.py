import os

WORDS_BANK = []

def Load_data():
    with open("words_bank.txt" , 'r') as f: 
        big_text = f.read()
        words = big_text.split('\n')
    
    for i in range(0, len(words), 2) :  
        WORDS_BANK.append({'english' : words[i] , 'persian' : words[i+1]})   

def Translate_english_To_farsi(input_text):
    input_text= input("please insert your english sentence for translate to farsi :")
    user_words= input_text.split(' ')
    output_text= ''
    for user_word in user_words:
        for word in WORDS_BANK:
            if user_word == word['english']:
                output_text += word['persian'] + ' '
                break
        else:
            output_text += user_word + ' '
        
    print(output_text) 

def Translate_farsi_To_english(input_text):
    input_text= input("please insert your english sentence for translate to farsi :")
    user_words= input_text.split(' ')
    output_text= ''
    for user_word in user_words:
        for word in WORDS_BANK:
            if user_word == word['persian']:
                output_text += word['english'] + ' '
                break
        else:
            output_text += user_word + ' '
        
    print(output_text)

def Add_new_word():
    english_word = input("please insert English word :")
    farsi_word = input("please insert Farsi word :")
    duplicate_word = False
    while not duplicate_word: 
        for word in WORDS_BANK:
            if english_word == word["english"]:
                os.system("clear")
                print("!! This word is duplicate and can not be stored in the word bank !!")
                english_word = input("please insert English word :")
                farsi_word = input("please insert Farsi word :")
                break
        else:
            duplicate_word = True
            WORDS_BANK.append({'english' : english_word , 'persian' : farsi_word})
            print("Your word was successfully saved in the word bank")

def show_menu():
    print("""1- add new word
    2- translation english2persian
    3- translation persian2english
    4- Exit and save""") 

def save_data():
    f = open('words_bank.txt', 'w')
    f.write(WORDS_BANK)

def main_func():

    while(True):
        show_menu()
        select = int(input("please choice a number from menu :"))
        if select == 1:
            Add_new_word()
        elif select == 2:
            Translate_english_To_farsi
        elif select == 3:
            Translate_farsi_To_english
        elif select == 4:
            save_data()    
            exit()
        else:
            print("!! please insert correct number !!")
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ {MAIN-FUNC} //////////////////////////////////////////////////

Load_data()
main_func()