from uturtle_prof import *

def square(t, x, seuil):
    if seuil == 0:
        moveForward(t, x/2)
        turnLeft(t, 120)
        moveForward(t, x/4)
        turnRight(t, 120)
        moveForward(t, x/4)
        turnRight(t, 120)
        moveForward(t, x/4)
        turnLeft(t, 120)
        moveForward(t, x/2)
    else:
        square(t, x/2, seuil-1)
        turnLeft(t, 120)
        square(t, x/4, seuil-1)
        turnRight(t, 120)
        square(t, x/4, seuil-1)
        turnRight(t, 120)
        square(t, x/4, seuil-1)
        turnLeft(t, 120)
        square(t, x/2, seuil-1)

if __name__ == '__main__':
    screen = turtle.Screen

    t = turtle.Turtle()
    setSpeed(t, 0)
    square(t, 700, 3)
    turnRight(t, 120)
    square(t, 700, 3)
    turnRight(t, 120)
    square(t, 700, 3)
    turnRight(t, 120)
    wait()