from userInput import *
from hangmantui import *

tried_letters = []

def main():
    i = 10
    print("P1 :")
    word = ask_word_in_dictionary()
    clear()
    print("P2 :")
    while 10 >= 0:
        print(i, "guess left !")
        print("Already guessed letters : ", tried_letters)
        print(display_word(word, tried_letters))
        success, l = is_the_letter_in_the_word(word, tried_letters)
        tried_letters.append(l)
        if success:
            print("Well done ! This letter is in the hidden word.")
        else:
            print("Try again !")
        
        if if_word_is_guessed(word, tried_letters):
            print("GG ! You guessed the correct word : ", word)
            break
    
        i = i - 1

main()