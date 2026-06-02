#!/usr/bin/python
# -*- coding: utf-8 -*-

""" Module permettant de manipuler une tortue en mode impératif
    Utilisé dans le cadre du cours de Algorithmique et programmation impérative
    (H. Mélot, Université de Mons, à partir de 2013)
"""

import turtle

""" initialise la fenêtre """
screen = turtle.Screen()

def setTitle(s):
    """ permet de mettre à jour le titre de la fenêtre
    
        s - le titre de la fenêtre  """
    screen.title(s)
    
def umonsTurtle():
    """ Retourne une tortue qui peut évoluer dans la fenêtre
    (déjà initialisée) """
    t = turtle.Turtle()
    return t
  
def setSpeed(t, s):
    """ Change la vitesse d'une tortue
    
        t - une tortue
        s - vitesse (0 = pas d'animation, 
                     sinon entier entre 1 (lent) et 10 (rapide))
    """
    t.speed(s)

def hideTurtle(t):
    """ Cache la tortue t """
    t.hideturtle()
    
def showTurtle(t):
    """ Montre la tortue t """
    t.showturtle()

def setColor(t, c):
    """ Permet de changer la couleur d'un tortue
    
        t - une tortue
        c - nom de la couleur, en anglais ("blue", "red", "green", ...) """
    t.color(c)
    
def setShape(t, s):
    """ Permet de changer la forme d'une tortue
    
        t - une tortue
        s - la forme parmi : “arrow”, “turtle”, “circle”,
            “square”, “triangle”, “classic”           """
    t.shape(s)

def setPensize(t, s):
    """ Permet de changer la largeur du trait 
    
        t - une tortue
        s - la largeur (en pixel) du trait
    """
    t.pensize(s)
  
def wait():
    """ permet que la fenêtre ne se ferme pas à la fin du srcipt :
        il faut quitter manuellement """
    turtle.done()
    
def moveForward(t, x):
    """ Fait avancer une tortue t de x pixels.

    t - une tortue
    x - nombre de pixels    """
    t.fd(x)
    
def moveBackward(t, x):
    """ Fait reculer une tortue t de x pixels.

    t - une tortue
    x - nombre de pixels    """
    t.bk(x)
    
def turnRight(t, a=90):
    """ Fait tourner une tortue t de a degrés vers la droite.

    t - une tortue
    a - angle en degrés (par défaut 90)   """
    t.rt(a)

def turnLeft(t, a=90):
    """ Fait tourner une tortue t de a degrés vers la gauche.

    t - une tortue
    a - angle en degrés (par défaut 90)   """
    t.lt(a)
    
def dropPen(t):
    """ Demande à une tortue t de soulever son stylo

    t - une tortue         """
    t.up()
    
def usePen(t):
    """ Demande à une tortue t d'abaisser son stylo

    t - une tortue         """
    t.down()
    
def goto(t, x, y):
    """ Déplace une tortue (sans qu'elle ne dessine)
        en position (x, y)
        
        t    - une tortue
        x, y - coordonnées de la position d'arrivée
    """
    dropPen(t)
    t.goto(x, y)
    usePen(t)
    
def jump(t, length):
    """ Fait faire un saut de longueur lenght à une tortue
        
        t      - une tortue
        lenght - longueur (en pixel) du saut
    """
    dropPen(t)
    moveForward(t, length)
    usePen(t)

def turnEast(t):
    """ Oriente une tortue vers l'Est (droite) 
        
        t - une tortue  """
    t.setheading(0)
    
def turnSouth(t):
    """ Oriente la tortue vers le Sud (bas)
        
        t - une tortue  """
    t.setheading(270)
    
def turnWest(t):
    """ Oriente la tortue vers l'Ouest (gauche)
        
        t - une tortue  """
    t.setheading(180)
    
def turnNorth(t):
    """ Oriente la tortue vers le Nord (haut)
        
        t - une tortue  """
    t.setheading(90)

if __name__ == '__main__':
    setTitle("Test du module uTurtle")
    bob = umonsTurtle()
    moveForward(bob, 100)
    turnRight(bob)
    moveForward(bob, 100)
    dropPen(bob)
    moveForward(bob, 50)
    usePen(bob)
    turnLeft(bob, 120)
    moveBackward(bob, 50)
    wait()
        
