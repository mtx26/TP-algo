from ex_3 import *
from uturtle_prof import *

def flocon(t, x, seuil):
    koch(t, x, seuil)
    turnRight(t, 120)
    koch(t, x, seuil)
    turnRight(t, 120)
    koch(t, x, seuil)


if __name__ == '__main__':
    screen = turtle.Screen

    t = turtle.Turtle()
    setSpeed(t, 0)

    flocon(t, 500, 2)
    wait()