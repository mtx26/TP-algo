# hangman.py by gpt5
from userInput import *
import hangmantui as hangmantui

def reveal_letters(secret, hidden, letter):
    """Met à jour le mot caché avec la lettre trouvée."""
    new_hidden = ""
    for i in range(len(secret)):
        if secret[i].lower() == letter.lower():
            new_hidden += secret[i]
        else:
            new_hidden += hidden[i]
    return new_hidden


def play_hangman():
    secret_word = ask_word_in_dictionary()
    hidden_word = "*" * len(secret_word)
    tried_letters = []
    remaining_tries = 10

    while remaining_tries > 0 and hidden_word != secret_word:
        hangmantui.clear()
        hangmantui.hangman(remaining_tries)
        print(f"Tentatives restantes : {remaining_tries}")
        print(f"Lettres déjà jouées : {', '.join(tried_letters)}")
        print(f"Mot : {hidden_word}")

        letter = ask_letter(tried_letters)
        tried_letters.append(letter)

        if letter.lower() in secret_word.lower():
            hidden_word = reveal_letters(secret_word, hidden_word, letter)
            print("✅ Bonne lettre !")
        else:
            remaining_tries -= 1
            print("❌ Mauvaise lettre !")

    # Fin de partie
    hangmantui.clear()
    if hidden_word == secret_word:
        print(f"🎉 Bravo ! Le mot était {secret_word}.")
        score = len(set(secret_word.lower())) + remaining_tries - len(tried_letters)
        print(f"Votre score : {score}")
    else:
        hangmantui.hangman(0)
        print(f"💀 Perdu ! Le mot était : {secret_word}.")