import numpy as np
import math

def droite(p1, p2):
    """
    Calcule le triplet (a, b, c) de la droite passant par les points p1 et p2.
    p1, p2 : tuples (x, y)
    Retourne : (a, b, c) tel que a*x + b*y = c
    """
    p1 = np.array(p1)
    p2 = np.array(p2)
    a = p2[1] - p1[1]
    b = p1[0] - p2[0]
    c = a * p1[0] + b * p1[1]
    return (a, b, c)

def paralleles(d1, d2):
    """
    Vérifie si deux droites d1 et d2 sont parallèles.
    d1, d2 : triplets (a, b, c)
    Retourne : True si parallèles, False sinon
    """
    a1, b1, _ = d1
    a2, b2, _ = d2
    return np.isclose(a1 * b2, a2 * b1)

def intersection(d1, d2):
    """
    Calcule le point d'intersection des droites d1 et d2.
    d1, d2 : triplets (a, b, c)
    Retourne : tuple (x, y) ou None si pas d'intersection
    """
    a1, b1, c1 = d1
    a2, b2, c2 = d2
    A = np.array([[a1, b1], [a2, b2]])
    C = np.array([c1, c2])
    if np.isclose(np.linalg.det(A), 0):
        return None
    sol = np.linalg.solve(A, C)
    return tuple(sol)

def droite_normale(d, p):
    """
    Calcule le triplet (a, b, c) de la droite perpendiculaire à d passant par p.
    d : triplet (a, b, c)
    p : tuple (x, y)
    Retourne : (a', b', c')
    """
    a, b, _ = d
    x, y = p
    a_n = -b
    b_n = a
    c_n = a_n * x + b_n * y
    return (a_n, b_n, c_n)

def symetrie_orthogonale(d, p):
    """
    Calcule le point image de p par la symétrie orthogonale par rapport à la droite d.
    d : triplet (a, b, c)
    p : tuple (x, y)
    Retourne : tuple (x', y')
    """
    d_n = droite_normale(d, p)
    pied = intersection(d, d_n)
    if pied is None:
        return None
    p = np.array(p)
    pied = np.array(pied)
    sym = 2 * pied - p
    return tuple(sym)

def distance_droite_point(d, p):
    """
    Calcule la distance entre la droite d et le point p.
    d : triplet (a, b, c)
    p : tuple (x, y)
    Retourne : float
    """
    a, b, c = d
    x, y = p
    return np.abs(a * x + b * y - c) / np.hypot(a, b)