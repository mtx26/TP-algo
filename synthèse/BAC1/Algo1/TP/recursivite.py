def puissance(x, n):
    if n == 0 :
        return 1
    else :
       return x*puissance(x, n-1)
    

def contient(n, d):
    if n % 10 == d :
        return True
    else :
        return contient(n//10, d)
        
def pgcd(x, y):
    if y == 0 :
        return x
    else :
        r = x % y
        return pgcd(y, r)


def est_multiple(n, d):
    if n < 0 :
        return False 
    if n == d :
        return True
    else :
        return est_multiple(n - d, d)
    
def ackermann(m, n):
    if m == 0 :
        return n + 1
    elif m > 0 and n == 0 :
        return ackermann(m - 1, 1)
    elif m > 0 and n > 0 :
        return ackermann(m - 1, ackermann(m, n-1))
    else :
        pass

def triangle_pascal(i, j) :
    if i < 0 or j < 0 :
        return 0
    if i == 0 and j == 0 :
        return 1
    else :
        return triangle_pascal(i - 1, j) + triangle_pascal(i - 1, j - 1)

