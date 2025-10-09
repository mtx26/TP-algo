import math

### On tarvaille avec la forme ax + by + c = 0
### le triplet (a, b, c)

def triplet_droite(x1, y1, x2, y2):
    """
    Calcule le triplet (a, b, c) représentant la droite passant par deux points.

    Arguments:
        x1, y1 : Coordonnées du premier point.
        x2, y2 : Coordonnées du second point.

    Return:
        Retourne le triplet (a, b, c) de la droite.
    """
    a = y1 - y2
    b = x2 - x1
    c = x1 * y2 - x2 * y1
    return a, b, c

def sousrtaireDeuxPoint(p1, p2):
    """
    Calcule le vecteur allant du point p1 au point p2.

    Arguments:
        p1 : Tuple (x, y) du premier point.
        p2 : Tuple (x, y) du second point.

    Return:
        Retourne le vecteur (x, y) correspondant à p2 - p1.
    """
    x1, y1 = p1
    x2, y2 = p2

    x = x2 - x1
    y = y2 - y1
    return (x, y)

def additionnerPointVecteur(p, v):
    """
    Additionne un point et un vecteur.

    Arguments:
        p : Tuple (x, y) du point.
        v : Tuple (vx, vy) du vecteur.

    Return:
        Retourne le point résultant de l'addition (x, y).
    """
    x1, y1 = p
    vx, vy = v

    x = x1 + vx
    y = y1 + vy

    return (x, y)

def droite(p1, p2):
    """
    Calcule le triplet (a, b, c) de la droite passant par deux points.

    Arguments:
        p1 : Tuple (x, y) du premier point.
        p2 : Tuple (x, y) du second point.

    Return:
        Retourne le triplet (a, b, c) de la droite.
    """
    a, b, c = triplet_droite(p1[0], p1[1], p2[0], p2[1])
    c = -c

# print(droite((-2, 0), (1, 1.5)))

def appartient(d, p1):
    """
    Vérifie si un point appartient à une droite.

    Arguments:
        d : Triplet (a, b, c) de la droite.
        p1 : Tuple (x, y) du point à tester.

    Return:
        Retourne True si le point appartient à la droite, False sinon.
    """
    if (d[0] * p1[0]) + (d[1] * p1[1]) + d[2] == 0 :
        return True
    else:
        return False

# print(appartient((-0.5, 1, 1.0), (0, 0)))

def paralleles(d1, d2):
    """
    Vérifie si deux droites sont parallèles.

    Arguments:
        d1 : Triplet (a, b, c) de la première droite.
        d2 : Triplet (a, b, c) de la seconde droite.

    Return:
        Retourne True si les droites sont parallèles, False sinon.
    """
    i = d1[0] * d2[1]
    j = d1[1] * d2[0]
    if i == j :
        return True
    else:
        return False
    
# print(paralleles((0, 1, 1), (0, 2, 3)))

def intersection(d1, d2):
    """
    Calcule le point d'intersection de deux droites.

    Arguments:
        d1 : Triplet (a, b, c) de la première droite.
        d2 : Triplet (a, b, c) de la seconde droite.

    Return:
        Retourne le point d'intersection (x, y) ou None si les droites sont parallèles.
    """
    a1, b1, c1 = d1
    a2, b2, c2 = d2

    det = a1 * b2 - a2 * b1
    if (det == 0):
        return None
    else:
        x = (c1 * b2 - c2 * b1) / det
        y = (a1 * c2 - a2 * c1) / det
        return (x, y)

# print(intersection((-0.5, 1, 1.0), (0, 2, 3)))

def droite_normal(d, p):
    """
    Calcule la droite perpendiculaire à une droite donnée passant par un point.

    Arguments:
        d : Triplet (a, b, c) de la droite.
        p : Tuple (x, y) du point.

    Return:
        Retourne le triplet (a, b, c) de la droite normale.
    """
    a1, b1, c1 = d
    x1, y1 = p

    a2 = -b1
    b2 = a1

    c2 = a2 * x1 + b2 * y1
    return (a2, b2, c2)

# print(droite_normal((-0.5, 1, 1.0), (-2, 0)))

def symetrie_orthogonale(d, p):
    """
    Calcule l'image d'un point par la symétrie orthogonale par rapport à une droite.

    Arguments:
        d : Triplet (a, b, c) de la droite.
        p : Tuple (x, y) du point à transformer.

    Return:
        Retourne le point image (x, y) par la symétrie orthogonale.
    """
    d2 = droite_normal(d, p)
    p2 = intersection(d, d2)
    v = sousrtaireDeuxPoint(p, p2)
    p3 = additionnerPointVecteur(p2, v)
    return p3

# print(symetrie_orthogonale((-0.5, 1, 1.0), (-2, 0)))

def distance_droite_point(d, p):
    """
    Calcule la distance entre une droite et un point.

    Arguments:
        d : Triplet (a, b, c) de la droite.
        p : Tuple (x, y) du point.

    Return:
        Retourne la distance (float) entre la droite et le point.
    """
    d2 = droite_normal(d, p)
    p2 = intersection(d, d2)
    p3 = sousrtaireDeuxPoint(p, p2)
    x3, y3 = p3
    d = math.sqrt(x3**2 + y3**2)
    return d

# print(distance_droite_point((-0.5, 1, 1.0), (-2, 0)))








