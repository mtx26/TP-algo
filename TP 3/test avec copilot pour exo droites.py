def droite(p1, p2):
    """
    Calcule le triplet (a, b, c) de la droite passant par les points p1 et p2.
    p1, p2 : tuples (x, y)
    Retourne : (a, b, c) tel que a*x + b*y = c
    """
    x1, y1 = p1
    x2, y2 = p2
    a = y2 - y1
    b = x1 - x2
    c = a * x1 + b * y1
    return (a, b, c)

def paralleles(d1, d2):
    """
    Vérifie si deux droites d1 et d2 sont parallèles.
    d1, d2 : triplets (a, b, c)
    Retourne : True si parallèles, False sinon
    """
    a1, b1, _ = d1
    a2, b2, _ = d2
    # Deux droites sont parallèles si leurs coefficients a et b sont proportionnels
    return a1 * b2 == a2 * b1

def intersection(d1, d2):
    """
    Calcule le point d'intersection des droites d1 et d2.
    d1, d2 : triplets (a, b, c)
    Retourne : tuple (x, y) ou None si pas d'intersection
    """
    a1, b1, c1 = d1
    a2, b2, c2 = d2
    det = a1 * b2 - a2 * b1
    if det == 0:
        return None
    x = (c1 * b2 - c2 * b1) / det
    y = (a1 * c2 - a2 * c1) / det
    return (x, y)

def droite_normale(d, p):
    """
    Calcule le triplet (a, b, c) de la droite perpendiculaire à d passant par p.
    d : triplet (a, b, c)
    p : tuple (x, y)
    Retourne : (a', b', c')
    """
    a, b, _ = d
    x, y = p
    # La normale a pour coefficients (-b, a)
    a_n = -b
    b_n = a
    c_n = a_n * x + b_n * y
    return (a_n, b_n, c_n)