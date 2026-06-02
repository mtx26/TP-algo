import math

# 1.1.1

def multiply(s, nb) :
    if nb == 1 :
        return s
    else :
        return s + multiply(s, nb - 1)

# 1.1.2

def print_from_middle(s, nb = 1):
    if nb == len(s):
        print(s)
    else :
        print_from_middle(s[1:len(s)-1], nb)
        print(s)

# 1.1.3

def print_pyramid(s, nb = 1):
    if nb == len(s):
        print(s)
    else :
        start = (len(s) - nb) // 2
        tirets = multiply('-', (len(s) - nb ) // 2)
        print(tirets+s[ start : start+nb ]+tirets)
        print_pyramid(s, nb + 2)
    

print_from_middle('recursivite')
    
# 1.2

def rech_dic(myTuple, elem):
    middle = (len(myTuple)) // 2
    if middle == 0 and elem != myTuple[middle] :
        return False
    if elem == myTuple[middle]:
        return True
    elif elem < myTuple[middle] :
       myTuple = myTuple[:middle]    
    else :
       myTuple = myTuple[middle + 1:]

    return rech_dic(myTuple, elem)
    
#print(rech_dic((0,1,3,5,6,8,10,11,14,15), 1))

# 1.3.1

def contient(mot, char):
    if len(mot) == 0:
        return False
    if mot[0] == char :
        return True
    else :
        mot = mot[1:]
    return contient(mot, char)

#print(contient('bateau','z'))

# 1.3.2

def palindrome(mot):
    if len(mot) == 1 :
        return True
    elif mot[0] != mot[-1]:
        return False
    else :
        return palindrome(mot[1:-1])

#print(palindrome('kayak'))
#print(palindrome('zoo'))

# 1.3.3

def longueur_paire(mot):
    if mot == '' :
        return True
    elif mot[1:] == '' :
        return False
    else :
        return longueur_paire(mot[2:])


# 1.4

def hanoi(d, start, inter, end):
    if d == 1 :
        print('Déplacer le disque depuis ',start,' jusque ',end)
        return
    hanoi(d-1, start, end, inter)
    print('Déplacer le disque depuis ',start,' jusque ',end)
    hanoi(d-1, inter, start, end)

#hanoi(3, 'A', 'B', 'C')

# 2.1

def f(x):
    return x


def approx_int(f, a, b, eps):
    n = 1
    found = False
    x = 0
    while not found :
        x_new = 0
        n = n*2
        delta = (b - a) / n
        for i in range(n):
            x_new = x_new + delta * f(a + i*delta)
        if abs(x-x_new) < eps :
            found = True
        x = x_new
    return x

#print(approx_int(f, 0, 4, 0.00001))
         

# 2.2

def crack_password(pwlenght):
    pwd = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lenght = 0
    pwdFound = False
    while not pwdFound and lenght <= pwlenght :
        i=0
        while not(is_letter_in_position(lenght, alphabet[i])):
            i = i + 1
        pwd = pwd + alphabet[i]
        if perfect_match(pwd):
            pwdFound = True
        lenght = lenght + 1
    return pwd


# 2.3

def f(x):
    return x**3 + 2*x + 5

def find_abs(f, d, a, b, eps):
    c_old = a
    c = (a + b) / 2
    while abs(c_old - c) > eps : 
        if f(c) > d :
            b = c
        elif f(c) < d :
            a = c
        else :
            return c
        c_old = c
        c = (a + b) / 2
    return c
    

#print(find_abs(f, 38, 2, 50, 0.00001))


#2.4

def tokenizer(chaine, delimiteur):
    i = 0
    res = ''
    start = False
    while i < len(chaine):
        current = chaine[i]
        if current == delimiteur :
            if start == True and len(res) != 0 :
                print(res)
            start = True
            res = ''
        else :
            res = res + current
        i = i + 1

# tokenizer('-chien-chat-poule-', '-')


#2.5

def dpc(v, alpha):
    dpc = (v**2 * math.sin(2*math.radians(alpha))) / 9.81
    return dpc

def angle(d, a, b, v, r):
    c = (a + b) / 2
    i = 1
    while dpc(v, c) <= d - r or dpc(v, c) >= d + r :
        if dpc(v, c) >= d + r :
            c = (a + (b-i)) / 2
        elif dpc(v, c) <= d - r :
            c = ((a+i) + b) / 2
        i = i + 1
    return c 

def angle_better(d, a, b, v, r):
    found = False
    while not found :
        c = (a + b) / 2
        if dpc(v,c) > d - r or dpc(v,c) < d + r :
            found = True
        if dpc(v,c) > d :
            b = c
        elif dpc(c) < d :
            a = c
    return c


#print(angle_better(5.1, 0, 45, 10, 0.01))
         
def is_reverse(mot1, mot2):
    if len(mot1) != len(mot2) :
        return False
    if len(mot1) == 0 :
        return True
    if mot1[0] == mot2[-1] :
        return is_reverse(mot1[1:], mot2[:-1])
    else :
        return False 
    
#print(is_reverse('hugo','oguh'))



     





                  













