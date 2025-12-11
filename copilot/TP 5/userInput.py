# userInput.py by gpt5

def belongs_to_dictionary(word):
    """Vérifie si le mot est présent dans words.txt (insensible à la casse)."""
    word = word.lower()
    with open("words.txt", "r", encoding="utf-8") as f:
        words = [w.strip().lower() for w in f.readlines()]
    return word in words


def ask_word_in_dictionary():
    """Demande à l’utilisateur un mot appartenant au dictionnaire."""
    while True:
        word = input("Joueur 2, entrez un mot présent dans le dictionnaire : ").strip()
        if belongs_to_dictionary(word):
            return word
        else:
            print("❌ Ce mot n’est pas dans le dictionnaire. Réessayez.")


def ask_letter(tried_letters):
    """Demande une lettre non encore essayée."""
    while True:
        letter = input("Proposez une lettre : ").strip().lower()
        if len(letter) != 1 or not letter.isalpha():
            print("❌ Entrez une seule lettre alphabétique.")
        elif letter in tried_letters:
            print("⚠️ Lettre déjà essayée. Essayez-en une autre.")
        else:
            return letter