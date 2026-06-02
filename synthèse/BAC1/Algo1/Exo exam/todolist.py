'''

Test 28 Octobre 2011 PB 1, 2, 3, 4 ----> OK

Examen 18 Janvier 2011 PB 4 ----> OK

Examen 11 Juin 2010 PB 1   ---> OK

Test 20 Novembre 2009 PB 1

'''
import math

def progressive_sum(m):
    S = []
    i = 0
    while i < len(m):
        j = 0
        sous_liste = []
        while j < len(m):
            rectangle = get_rectangle(m, i, j)
            sum = get_sum(rectangle)
            sous_liste.append(sum)
            j = j + 1
        S.append(sous_liste)
        i = i + 1
    return S

def get_rectangle(mat, k, l):
    rectangle = []
    i = 0
    while i <= k :
        j = 0
        sous_liste = []
        while j <= l :
            sous_liste.append(mat[i][j])
            j = j + 1
        rectangle.append(sous_liste)
        i = i + 1
    return rectangle

def get_sum(rectangle):
    i = 0
    somme = 0
    while i < len(rectangle):
        j = 0
        while j < len(rectangle[0]):
            somme = somme + rectangle[i][j]
            j = j + 1
        i = i + 1
    return somme

def anagrammes(mot1, mot2):
    if len(mot1) != len(mot2):
        return False
    if len(mot1) == 0 and len(mot2) == 0 :
        return True
    else :
        cnt = 0
        for lettre in mot2 :
            if mot1[0] == lettre :
                new = mot2[:cnt] + mot2[cnt+1:]
                return anagrammes(mot1[1:],new)
            cnt = cnt + 1
        return False

def scrabble(mot, fichier):
    anagrammes_list = []
    with open(fichier) as file :
        for line in file :
            word = line.strip()
            if anagrammes(word, mot):
                anagrammes_list.append(word)
        return anagrammes_list
    
def intersection(f, g, a, b, eps):
    if abs(f(a)-g(a)) <= eps :
        return (a, f(a))
    elif abs(f(b)-g(b)) <= eps :
        return (b, f(b))
    else :
        c = a + (b-a)/2
        if f(a) > g(a) and f(c) < g(c) :
            return intersection(f, g, a, c, eps)
        if f(c) > g(c) and f(b) < g(b) :
            return intersection(f, g, c, b, eps)
    
def fibonacci(borne):
    fibo_list = [1,2]
    fibo1 = 1
    fibo2 = 2
    last = 2
    while last <= borne:
        x = fibo1 + fibo2
        last = x
        if last > borne :
            return fibo_list
        fibo_list.append(x)
        fibo1 = fibo2
        fibo2 = x
    return fibo_list

def codage(nombre):
    liste = fibonacci(nombre)
    code = []
    decompte = nombre
    i = len(liste) - 1
    while decompte != 0 :
        if liste[i] <= decompte :
            decompte = decompte - liste[i]
            code.append(1)
            liste.pop()
        else :
            code.append(0)
            liste.pop()
        i = i - 1
    while liste != []:
        liste.pop()
        code.append(0)
    reverse_code = []
    i = len(code) - 1
    while i >= 0 :
        reverse_code.append(code[i])
        i = i - 1
    return reverse_code

def approxPI(d, i):
    x = math.sqrt(2*(d/2)**2)
    if i == 1 :
        return (4*x) / d
    else :
        k = 2
        while k <= i :
            a = math.sqrt((d/2)**2 - (x/2)**2)
            b = d/2 - a
            c = math.sqrt(b**2 + (x/2)**2)
            x = c
            k = k + 1
        perimetre = (2**(i+1)) * x
        approx = perimetre/d
        return approx