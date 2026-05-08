

def reg_lin(liste):
    
    l = len(liste)
    x_bar = 0
    y_bar = 0
    for li in liste:
        x, y = li
        x_bar += x
        y_bar += y
    x_bar /= l
    y_bar /= l
    
    
    var = 0
    for li in liste:
        x, y = li
        var += (x - x_bar)**2
    var /= l
    
    covar = 0
    for li in liste:
        x, y = li
        covar += (x - x_bar) * (y - y_bar)
    covar /= l
    
    a = covar/var
    b = y_bar - (x_bar*covar)/var
    return a, b
    
points = [
    (2, 4),
    (3, 5),
    (5, 7),
    (7, 10),
    (8, 12),
    (10, 15),
    (12, 17),
    (13, 19),
    (15, 22),
    (18, 25)
]

print(reg_lin(points))