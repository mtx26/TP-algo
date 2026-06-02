import userInput
import hangmantui

def is_letter_in_word(lettre, mot) :
    for char in mot :
        if char == lettre :
            return True
    return False

def guess(lettre, mot, res):
    i = 0
    result = ''
    while i < len(mot) :
        if lettre == mot[i]:
            result = result + lettre
        else :
            result = result + res[i]
            
        i = i + 1
    return result


def life_update(life):
    if is_letter_in_word(lettre, mot) :
        return life
    else :
        return life - 1
    
def how_many_letters_in_word(mot) :
    myList = []
    i = 0
    count = 0
    while i < len(mot) :
        if not mot[i] in myList :
            count = count + 1
            myList.append(mot[i])
        else :
            pass
        i = i + 1
    return count


print('Bienvenue dans le jeu du pendu ! Le joueur 1 va devoir trouver le mot choisi par le Joueur 2. Pour se faire, le Joueur 1 va entrer une lettre, si elle est contenue dans le mot, sa position est révelée et le Joueur 1 conserve ses vies, sinon, le Joueur 1 perd une vie. Si le mot n\'est pas découvert à la fin des 10 vies, c\'est le Joueur 2 qui l\'emporte.')
tried_letter = []
mot = userInput.ask_word_in_dictionary()
hangmantui.clear()
difficulty = how_many_letters_in_word(mot)
life = 10
res = '*' * len(mot)
print('Voici l\évolution du mot mystère : ',res)
while life > 0 :
    
    hangmantui.hangman(life)
    lettre = userInput.ask_letter(tried_letter)
    tried_letter.append(lettre)
    res = guess(lettre, mot, res)
    hangmantui.clear()
    print('Voici l\évolution du mot mystère : ',res)
    if res == mot :
        print('Bravo Joueur 1, tu as gagné ! Le mot choisi par Joueur 2 était bien', mot,'!')
        score = difficulty + life 
        print('Ton score est :', score ,'! Bravo !')
        exit()
    life = life_update(life)
    print('Il te reste : ', life,' vies')
    

print('Perdu ! C\'est le Joueur 2 qui gagne ! Le mot était',mot,'..')