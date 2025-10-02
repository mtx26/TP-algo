import random as rd
import math

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
CYAN = '\033[96m'
RESET = '\033[0m'

i = 1


def random(n, p):
    """
        Cette fonction génere un nombre aléatoire entre n et p.

        Arguments:
            n : nombre minimal (int)
            p : nombre maximal (int)

        Return:
            Retourne un nombre aléatoire entre n et p.
    """
    nb = rd.randrange(n, p, 1)
    return nb
help(random)

def power(n, p):
    """
        Vérifie si n est une puissance de p.

        Arguments:
            n : nombre à tester (int)
            p : base de la puissance (int)

        Return:
            Retourne True si n est une puissance de p, False sinon.
    """
    for i in range (1, n):
        if p**i > n:
            return False
        elif p**i == n:
            return True
        
def is_odd(nb):
    """
        Affiche si le nombre est pair ou impair.

        Arguments:
            nb : nombre à tester (int)

        Return:
            Aucun retour, affiche le résultat.
    """
    if (nb % 2 == 0):
        print(CYAN + "Le nombre est pair" + RESET)
    else:
        print(YELLOW + "Le nombre est impair" + RESET)

def is_three(nb):
    """
        Affiche si le nombre est un multiple de 3.

        Arguments:
            nb : nombre à tester (int)

        Return:
            Aucun retour, affiche le résultat.
    """
    if (nb % 3 == 0):
        print(CYAN + "Le nombre est multiple de 3" + RESET)
    else:
        print(YELLOW + "Le nombre n'est pas multiple de 3" + RESET)

def is_50(nb):
    """
        Affiche si le nombre est inférieur ou égal à 50 ou supérieur à 50.

        Arguments:
            nb : nombre à tester (int)

        Return:
            Aucun retour, affiche le résultat.
    """
    if (nb <= 50):
        print(CYAN + "Le nombre est inférieur ou égale à 50" + RESET)
    else:
        print(YELLOW + "Le nombre est supérieur à 50" + RESET)

def is_power(nb):
    """
        Affiche si le nombre est une puissance de 2.

        Arguments:
            nb : nombre à tester (int)

        Return:
            Aucun retour, affiche le résultat.
    """
    if (power(nb, 2)):
        print(CYAN + "Le nombre est une puissance de 2" + RESET)
    else:
        print(YELLOW + "Le nombre n'est pas puissance de 2" + RESET)

def is_squared(nb):
    """
        Affiche si le nombre est un carré parfait.

        Arguments:
            nb : nombre à tester (int)

        Return:
            Aucun retour, affiche le résultat.
    """
    nb_2 = math.isqrt(nb)
    if (nb_2 * nb_2 == nb):
        print(CYAN + "Le nombre est un carré parfait" + RESET)
    else:
        print(YELLOW + "Le nombre n'est pas un carré parfait" + RESET)

nb = random(1, 100)

while(i < 6):

    if (i == 1):
        is_odd(nb)

    if (i == 2):
        is_three(nb)
    if (i == 3):
        is_50(nb)
    
    if (i == 4):
        is_power(nb)

    if (i == 5):
        is_squared(nb)

    user_nb = input(BLUE + "Entrez le nombre qui a été généré aléatoirement :\n" + RESET)
    
    if user_nb.isdigit():
        user_nb = int(user_nb)

        if (nb == user_nb):
            print(GREEN + "GG !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" + RESET)
            break
        else:
            if (i == 5):
                print(RED + "Dommage :( , le nombre étais " + RESET + GREEN + str(nb) + RESET)
            else:
                print(RED + "Pas de chance, essayez encore." + RESET)
            i += 1
    else:
        print(RED + "Only number !!!!!!!" + RESET)

