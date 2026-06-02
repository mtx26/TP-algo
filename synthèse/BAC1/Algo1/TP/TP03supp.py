import math
import random


def delta(a, b, c) :
    delta = b**2 - (4*a*c)
    return delta

def racine(delta, a, b) :
    if delta < 0 :
        return None
    elif delta == 0 :
        return (-b / 2*a)
    else :
        x1 = (-b + math.sqrt(delta))/2*a
        x2 = (-b - math.sqrt(delta))/2*a
        return (x1, x2)
    
def equationSolver(a,b,c):
    discriminant = delta(a,b,c)
    return racine(discriminant, a, b)


def lancer(a, b) :
    firstDe = random.randint(a, b)
    secondDe = random.randint(a, b)
    thirdDe = random.randint(a, b)

    if (firstDe, secondDe, thirdDe) == (4, 2 ,1):
        return True
    else :
        return False
    
print(lancer(1, 4))

