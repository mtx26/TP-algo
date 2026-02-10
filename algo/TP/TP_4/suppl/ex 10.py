def est_multiple(n, d):
    e = 1
    rec(n, d, e)
    
    

def rec(n, d, e):
    if n * e == d:
        return True
    elif e > d:
        return False
    else:
        return rec(n, d, e + 1)
    
print(est_multiple(40, 4))