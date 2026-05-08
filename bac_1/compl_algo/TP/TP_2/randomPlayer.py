from joueur import Joueur, Mage, Guerrier
from random import choice, randint

def get_random_name(playerClass):
    if playerClass == Mage:
        names = ['Gandalf', 'Saruman', 'Radagast', 'Alatar', 'Pallando', 'Melian', 'Luthien', 'Galadriel', 'Arwen', 'Eowyn', 'Elwing', 'Nienor', 'Finduilas', 'Idril', 'Morwen', 'Nerdanel', 'Aredhel', 'Indis', 'Miriel', 'Varda', 'Yavanna', 'Nienna']
    elif playerClass == Guerrier:
        names = ['Aragorn', 'Boromir', 'Faramir', 'Theoden', 'Eomer', 'Eowyn', 'Gimli', 'Legolas', 'Bard', 'Beorn', 'Thorin', 'Dain', 'Dwalin', 'Balin', 'Bifur', 'Bofur', 'Bombur', 'Dori', 'Nori', 'Ori', 'Gloin', 'Oin', 'Fili', 'Kili']
    else:
        names = ['Frodo', 'Sam', 'Bilbo', 'Gollum', 'Smeagol', 'Pippin', 'Merry', 'Rosie', 'Estella', 'Goldberry', 'Lobelia', 'Belladonna', 'Primula', 'Lily', 'Iris', 'Daisy', 'Poppy', 'Ruby']   
    qualifier = ['Dark', 'Light', "Wise", "Brave", "Strong", "Swift", "Noble", "Fair", "Wise", "Mighty", "Evil", "Good", "Great", "Greedy", "Clever", "Wicked", "Kind", "Fierce", "Gentle", "Mad", "Wild", "Crazy"]
    return choice(qualifier) + ' ' + choice(names)

def new_player():
    playerClass = choice([Joueur, Mage, Guerrier])
    if playerClass == Guerrier:
        return playerClass(f"{get_random_name(playerClass)}", randint(1, 10), randint(5, 15))
    elif playerClass == Mage:
        return playerClass(f"{get_random_name(playerClass)}", randint(1, 10), randint(5, 20))
    else:
        return playerClass(f"{get_random_name(playerClass)}", randint(1, 10))

if __name__ == "__main__":
    for _ in range(5):
        p = new_player()
        print(p)
        print(repr(p))