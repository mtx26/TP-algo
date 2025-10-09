import random as rd
import math

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
CYAN = '\033[96m'
RESET = '\033[0m'


def random(n, p):
    return rd.randint(n, p)


def power(n, p):
    if n < 1 or p < 2:
        return False
    while n % p == 0:
        n //= p
    return n == 1


def is_odd(nb):
    print(CYAN + "Le nombre est pair" + RESET if nb % 2 == 0 else YELLOW + "Le nombre est impair" + RESET)


def is_three(nb):
    print(CYAN + "Le nombre est multiple de 3" + RESET if nb % 3 == 0 else YELLOW + "Le nombre n'est pas multiple de 3" + RESET)


def is_50(nb):
    print(CYAN + "Le nombre est inférieur ou égale à 50" + RESET if nb <= 50 else YELLOW + "Le nombre est supérieur à 50" + RESET)


def is_power(nb):
    print(CYAN + "Le nombre est une puissance de 2" + RESET if power(nb, 2) else YELLOW + "Le nombre n'est pas puissance de 2" + RESET)


def is_squared(nb):
    nb_2 = math.isqrt(nb)
    print(CYAN + "Le nombre est un carré parfait" + RESET if nb_2 * nb_2 == nb else YELLOW + "Le nombre n'est pas un carré parfait" + RESET)


def ask():
    user_nb = input(BLUE + "Entrez le nombre qui a été généré aléatoirement :\n" + RESET)
    try:
        return int(user_nb)
    except ValueError:
        print(RED + "Only number !!!!!!!" + RESET)
        return None


def step(nb, i):
    if i == 1:
        is_odd(nb)
    elif i == 2:
        is_three(nb)
    elif i == 3:
        is_50(nb)
    elif i == 4:
        is_power(nb)
    elif i == 5:
        is_squared(nb)


nb = random(1, 100)

for i in range(1, 6):
    step(nb, i)
    user_nb = ask()
    if user_nb is not None:
        if nb == user_nb:
            print(GREEN + "GG !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" + RESET)
            break
        elif i == 5:
            print(RED + "Dommage :( , le nombre étais " + RESET + GREEN + str(nb) + RESET)
        else:
            print(RED + "Pas de chance, essayez encore." + RESET)

