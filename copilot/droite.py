def droite(p1, p2):
    """
    Retourne le triplet (a, b, c) représentant la droite passant par p1 et p2.
    Si p1 == p2, retourne None.
    """
    x1, y1 = p1
    x2, y2 = p2
    if p1 == p2:
        return None
    a = y2 - y1
    b = x1 - x2
    c = a * x1 + b * y1
    # On simplifie le triplet en divisant par le plus grand diviseur commun si possible
    # (optionnel, mais permet d'avoir des triplets plus "propres")
    return (a, b, c)

def appartient(d, p):
    """
    Retourne True si le point p appartient à la droite d, False sinon.
    """
    a, b, c = d
    x, y = p
    return abs(a * x + b * y - c) < 1e-9  # tolérance numérique

def paralleles(d1, d2):
    """
    Retourne True si d1 et d2 sont parallèles, False sinon.
    """
    a1, b1, _ = d1
    a2, b2, _ = d2
    # Les droites sont parallèles si leurs vecteurs normaux sont colinéaires
    return abs(a1 * b2 - a2 * b1) < 1e-9

def intersection(d1, d2):
    """
    Retourne le point d'intersection de d1 et d2 s'il existe, None sinon.
    """
    a1, b1, c1 = d1
    a2, b2, c2 = d2
    det = a1 * b2 - a2 * b1
    if abs(det) < 1e-9:  # droites parallèles ou confondues
        return None
    x = (b2 * c1 - b1 * c2) / det
    y = (a1 * c2 - a2 * c1) / det
    return (x, y)

def droite_normale(d, p):
    """
    Retourne la droite perpendiculaire à d passant par p.
    """
    a, b, _ = d
    x, y = p
    # La droite normale a pour vecteur normal (-b, a)
    a_normale = -b
    b_normale = a
    c_normale = a_normale * x + b_normale * y
    return (a_normale, b_normale, c_normale)

def symetrie_orthogonale(d, p):
    """
    Retourne le point symétrique de p par rapport à la droite d.
    """
    a, b, c = d
    x, y = p
    # Calcul de la projection de p sur d
    denom = a**2 + b**2
    if denom == 0:
        return p
    k = (a * x + b * y - c) / denom
    x_proj = x - a * k
    y_proj = y - b * k
    # Le symétrique est tel que (x_proj, y_proj) est le milieu de p et son symétrique
    x_sym = 2 * x_proj - x
    y_sym = 2 * y_proj - y
    return (x_sym, y_sym)

def distance_droite_point(d, p):
    """
    Retourne la distance entre la droite d et le point p.
    """
    a, b, c = d
    x, y = p
    return abs(a * x + b * y - c) / (a**2 + b**2)**0.5
