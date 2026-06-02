from uturtle import *

bob = umonsTurtle() 

def koch(t, x, seuil=5) :
    if x < seuil:
        moveForward(t, x)

    else:
        koch(t, x / 3)
        turnLeft(t, 60)
        koch(t, x / 3)
        turnRight(t, 120)
        koch(t, x / 3)
        turnLeft(t, 60)
        koch(t, x / 3)


def flocon_koch(t, x) :
    for i in range(3):
        koch(t, x)
        turnRight(t, 120)

def carre(t, x, seuil=5) :
    if x < seuil:
        moveForward(t, x)

    else:
        carre(t, x / 4)
        turnLeft(t, 90)
        carre(t, x / 4)
        turnRight(t, 90)
        carre(t, x / 4)
        turnRight(t, 90)
        carre(t, x / 4)
        turnLeft(t, 90)
        carre(t, x / 4)



def arbre(t, x, a, n):

    if n ==0  :
        return

    else :
        moveForward(t, x)
        turnLeft(t, a)
        arbre(t, x/2, a, n-1)
        turnRight(t, 2*a)
        arbre(t, x/2, a, n-1)
        turnLeft(t, a)
        moveBackward(t, x)

#koch(bob, 200)
#flocon_koch(bob, 200)
#carre(bob, 1000)
#turnNorth(bob)
#arbre(bob, 200, 40, 5)

wait()