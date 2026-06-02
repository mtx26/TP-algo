def caractere(s, i):
    if i > len(s) or i <= 0 :
        return None
    else :
        return s[i-1]
    
def caracteres(s, i, j):
    if i > j or i >= len(s) or j >= len(s) or i < 0 or j < 0 :
        return None
    else :
        return s[i:j]

def change_caractere(s, i, a):
    if i > len(s) or i <= 0 :
        return None
    else :
        res = ''
        k = 0
        while k < len(s) :
            if k == i - 1 :
                res = res + a
            else :
                res = res + s[k]
            k = k + 1
        return res
    
def change_caracteres(s, i, j, t):
    if i > j or i > len(s) or j > len(s) or i < 0 or j < 0 :
        return None
    else :
        res = ''
        k = 0
        while k < len(s):
            if k < i - 1 or k > j - 1 :
                res = res + s[k]
            if k == i - 1 :
                res = res + t
            k = k + 1
        return res 
    
def decouvre(s1, s2, x):
    i = 0
    res = ''
    while i < len(s2):
        if s1[i] == x :
            res = res + x
        else :
            res = res + s2[i]
        i = i + 1
    return res 



