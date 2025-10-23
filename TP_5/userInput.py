

def belongs_to_dictionary(word):
    with open('TP_5/words.txt', "r") as fichier:
        word.lower()
        find = False
        for line in fichier:
            dic = line.strip()
            if word == dic:
                find = True
                return find
        if find == False:
            return find
        
def ask_word_in_dictionary():
    correct = False
    while correct == False:
        word = input("Enter a word : ")
        word.lower()
        if belongs_to_dictionary(word):
            correct = True
            return word
        else:
            print("this word does not belong to the dictionnary for that hangman !! Try another one...")

def ask_letter(tried_letters):
    correct = False
    while correct == False:
        letter = input("Enter your guess : ")
        if len(letter) == 1:
            found = False
            for l in tried_letters:
                if l == letter:
                    found = True
            if found:
                print("you already guessed that one !")
            else:
                correct = True
                return letter
        else:
            print("Only one letter per guess !")

def is_the_letter_in_the_word(word, tried_letters):
    l = ask_letter(tried_letters)
    for letter in word:
        if l == letter:
            return True, l
    return False, l

def display_word(word, tried_letters):
    display_word = ""
    for l in word:
        if l in tried_letters:
            display_word += l
        else:
            display_word += "*"
    return display_word

def display_word(word, tried_letters):
    display_word = ""
    for l in word:
        if l in tried_letters:
            display_word += l
        else:
            display_word += "*"
    return display_word


def if_word_is_guessed(word, tried_letters):
    display_word = ""
    for l in word:
        if l in tried_letters:
            display_word += l
    return display_word == word


if __name__ == "__main__":
    print(display_word("salut", ["a", "b", "c"]))
