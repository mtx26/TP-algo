def belong_to_dictionary(word) :
    
    with open('words.txt', 'r') as file :
        for line in file :
            if line.strip() == word :
                print('Bien reçu ! Merci Joueur 2 !')
                return True
        return False
    
def ask_word_in_dictionary():
    motMystere = input('Joueur 2, c\'est à toi d\'entrer un mot du dictionaire : ')
    if belong_to_dictionary(motMystere):
        return motMystere
    else :
        motMystere = input('Ce mot ne fait pas parti du dictionaire.. Recommence : ')
        return motMystere
    
def is_one_letter(s):
    return len(s) == 1 and s.isalpha()

def ask_letter(tried_letter):
    letter = input('Joueur 1, c\'est à ton tour d\'entrer une lettre : ').lower()
    cont = True
    while cont :
        if not is_one_letter(letter):
            letter = input('Joueur 1, donne moi exactement une lettre stp : ')
        elif letter in tried_letter :
            letter = input('Joueur 1, tu m\'as déjà donné cette lettre, essaye en une autre : ')
        else :
            cont = False
    return letter






