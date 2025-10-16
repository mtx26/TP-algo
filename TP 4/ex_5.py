from uturtle_prof import *

def carre(t, x, seuil):
    if seuil == 0:
        moveForward(t, x/3)
        turnLeft(t, 90)
        moveForward(t, x/3)
        turnRight(t, 90)
        moveForward(t, x/3)
        turnRight(t, 90)
        moveForward(t, x/3)
        turnLeft(t, 90)
        moveForward(t, x/3)
    else:
        carre(t, x/3, seuil-1)
        turnLeft(t, 90)
        carre(t, x/3, seuil-1)
        turnRight(t, 90)
        carre(t, x/3, seuil-1)
        turnRight(t, 90)
        carre(t, x/3, seuil-1)
        turnLeft(t, 90)
        carre(t, x/3, seuil-1)

if __name__ == '__main__':
    screen = turtle.Screen

    t = turtle.Turtle()
    setSpeed(t, 0)
    carre(t, 500, 5)
    wait()