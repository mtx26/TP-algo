from uturtle_prof import *

def koch(t, x, seuil):
    if seuil == 0:
        moveForward(t, x/3)
        turnLeft(t, 60)
        moveForward(t, x/3)
        turnRight(t, 120)
        moveForward(t, x/3)
        turnLeft(t, 60)
        moveForward(t, x/3)
    else:
        koch(t, x/3, seuil-1)
        turnLeft(t, 60)
        koch(t, x/3, seuil-1)
        turnRight(t, 120)
        koch(t, x/3, seuil-1)
        turnLeft(t, 60)
        koch(t, x/3, seuil-1)

if __name__ == '__main__':
    screen = turtle.Screen

    t = turtle.Turtle()
    setSpeed(t, 0)
    koch(t, 500, 3)
    wait()