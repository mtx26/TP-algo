import random
import math

a = input('Bonjour, tu vas devoir deviner un nombre aléatoire d\'une plage que tu va définir, sélectionne donc la 1ere borne de cet ensemble : ')
b = input('Très bien, maintenant la 2e borne afin de clôturer la plage du jeu : ')
if a.isdigit() and b.isdigit :
   a = int(a)
   b = int(b)
   print('Parfait ! Nous jouons dans un ensemble de nombres naturels entre ',a,' et ',b)
else :
   print('Oups, on dirait que tu \'as pas indiqué un nombre, recommence !')
   exit()

randomNumber = random.randint(a, b)


def demander():
    """
    La fonction a pour but de demander un entier à l'utilisateur
    
    Arguments :
        None

    Returns :
        Retourne la valeur entrée en veillant à ce que ce soit un naturel
        Dans le cas où l'utilisateur entre autre chose qu'un naturel, la fonction retourne -1.
    """
    guess = input('Entrez le nombre qui a été généré aléatoirement :')
    if guess.isdigit():
      guess = int(guess)
      if guess <= 0 :
         return -1
      else :
         return guess
    else :
      print('Tu n\'as pas écrit un nombre, recommence.')
      demander()
    
def hint1(randomNumber):
   """
   La fct a pour but de donner le 1er indice

   Arguments :
   randomNumber : le nombre aléatoire
   Returns :
   None
   """
   if randomNumber % 2 == 0 :
      print('Voici un indice : le nombre est pair.')
   else :
      print('Voici un indice : le nombre est impair.')
   
def hint2(randomNumber):
   """
   La fct a pour but de donner le 2e indice

   Arguments :
   randomNumber (le nombre aléatoire)
   Returns :
   None
   """
   if randomNumber % 3 == 0 :
      print('Voici un indice : le nombre est un multiple de 3.')
   else :
      print('Voici un indice : le nombre n\'est pas un multiple de 3.')
   
def hint3(randomNumber):
   """
   La fct a pour but de donner le 3e indice

   Arguments :
   randomNumber (le nombre aléatoire)
   Returns :
   None
   """
   if randomNumber <= b/2 :
      print('Voici un indice :le nombre est inférieur à ',a+((b-a)/2))
   else :
      print('Voici un indice :le nombre est strictement supérieur à',a+((b-a)/2 ))
   
def hint4(randomNumber):
   """
   La fct a pour but de donner le 4e indice

   Arguments :
   randomNumber (le nombre aléatoire)
   Returns :
   None
   """
   if math.log(randomNumber) % 1 == 0 :
      print('Voici un indice : le nombre est une puissance de 2.')
   else :
      print('Voici un indice : le nombre n\'est pas une puissance de 2.')
   

def hint5(randomNumber):
   """
   La fct a pour but de donner le 5e indice

   Arguments :
   randomNumber (le nombre aléatoire)
   Returns :
   None
   """
   if math.sqrt(randomNumber) % 1 == 0 :
      print('Voici un indice : le nombre est un carré.')
   else :
      print('Voici un indice : le nombre n\'est pas un carré.')

def step(randomNumber, hint_function):
   """
   
   Arguments :
   un naturel randomNumber qui correspond au
   nombre à deviner, et une fonction hint_function correspondant à la fonction à appeler pour donner
   l'indice.

   Returns :
   l'indice correspondant à l'étape
   """
   hint_function(randomNumber)
   if randomNumber == demander():
      print('Félicitation ! Il s\'agit bien du nombre aléatoire !')
      exit()
   else :
      print('Pas de chance, essaye encore !')


step(randomNumber, hint1)
step(randomNumber, hint2)
step(randomNumber, hint3)
step(randomNumber, hint4)
step(randomNumber, hint5)
print('Dommage, tu n\'as pas trouvé le nombre... Il s\'agissait de  ',randomNumber)