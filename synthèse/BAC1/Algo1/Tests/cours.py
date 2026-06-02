def fact(x):
    if x == 0 :
        return 1
    else :
        return x * fact(x-1)

def exp(a, n):
    if n == 1 :
        return a
    else :
        return a * exp(a, n-1)
    
def fibo(n):
    if n == 0 :
        return 1
    elif n == 1 :
        return 1
    else :
        return fibo(n - 2) + fibo(n - 1)
    
def heron(a, x, eps):
    x_new = (x + (a/x))/2
    if abs(x - x_new) <= eps :
        return x_new
    else :
        return heron(a, x, eps)
    
def a2o(s):
    i = 0
    res = ''
    while i < len(s):
        if s[i] == 'a' :
            res = res + 'o'
        else :
            res = res + s[i]
        i = i + 1
    return res

def find(mot, char) :
    i = 0
    while i < len(mot):
        if mot[i] == char :
            return i
        i = i + 1
    return None
    
def invert(mot):
    res = ''
    i = 0
    while i < len(mot):
        res = res + mot[len(mot)-i-1]
        i = i + 1
    return res

def bin2dec(x):
    res = 0
    i = 0
    while i < len(x):
        if x[i] == '1':
            res = res + 2 ** (len(x)-i-1)
        elif x[i] != '0':
            return None
        i = i + 1
    return res

