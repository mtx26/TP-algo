import math

# ==============================================================================
# PROBLÈME 1 : DÉPLACEMENTS DANS UNE MAISON
# [cite_start]Source : [cite: 7, 8, 13]
# ==============================================================================

def peut_aller(piece1, piece2, portes, eviter):
    """
    a) Retourne True si un chemin existe de piece1 à piece2 sans cycle.
    """
    if piece1 == piece2:
        return True
    
    # On ajoute la pièce actuelle aux pièces à éviter pour ne pas y revenir
    nouvel_eviter = eviter + [piece1]
    
    for (p_dep, p_arr) in portes:
        if p_dep == piece1 and p_arr not in eviter:
            if peut_aller(p_arr, piece2, portes, nouvel_eviter):
                return True
    return False

def chemin(piece1, piece2, portes, eviter):
    """
    b) Retourne une liste représentant le chemin ou None si impossible.
    """
    if piece1 == piece2:
        return [piece1]
    
    nouvel_eviter = eviter + [piece1]
    
    for (p_dep, p_arr) in portes:
        if p_dep == piece1 and p_arr not in eviter:
            resultat = chemin(p_arr, piece2, portes, nouvel_eviter)
            if resultat is not None:
                return [piece1] + resultat
    return None

def plus_court_chemin(piece1, piece2, portes, eviter):
    """
    c) Bonus : Retourne le chemin le plus court (liste de pièces).
    """
    if piece1 == piece2:
        return [piece1]
    
    nouvel_eviter = eviter + [piece1]
    meilleur_chemin = None
    
    for (p_dep, p_arr) in portes:
        if p_dep == piece1 and p_arr not in eviter:
            res = plus_court_chemin(p_arr, piece2, portes, nouvel_eviter)
            if res is not None:
                # Si c'est le premier chemin trouvé ou s'il est plus court que le précédent
                if meilleur_chemin is None or len(res) < len(meilleur_chemin):
                    meilleur_chemin = res
                    
    if meilleur_chemin is not None:
        return [piece1] + meilleur_chemin
    return None


# ==============================================================================
# PROBLÈME 2 : AIRE D'UN POLYGONE
# [cite_start]Source : [cite: 25, 26, 37]
# ==============================================================================

def aire(liste):
    """
    Calcule l'aire d'un polygone convexe de manière récursive.
    """
    n = len(liste)
    
    # [cite_start]Cas de base : Triangle (3 sommets) [cite: 30, 31]
    if n == 3:
        (x1, y1) = liste[0]
        (x2, y2) = liste[1]
        (x3, y3) = liste[2]
        # [cite_start]Formule du déterminant donnée dans l'énoncé [cite: 33]
        valeur = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)
        return 0.5 * abs(valeur)
    
    # Cas récursif : On coupe le polygone en un triangle (p1, p2, p3)
    # [cite_start]et le reste du polygone (p1, p3, p4...) [cite: 34, 36]
    # Note: L'énoncé suggère de diviser en deux polygones. Une façon simple
    # pour une liste ordonnée est d'isoler le triangle formé par les 3 premiers points.
    poly_triangle = [liste[0], liste[1], liste[2]]
    poly_reste = [liste[0]] + liste[2:] # Conserve p1 et la suite à partir de p3
    
    return aire(poly_triangle) + aire(poly_reste)


# ==============================================================================
# PROBLÈME 3 : UN PETIT RÉSEAU SOCIAL
# [cite_start]Source : [cite: 70, 71]
# ==============================================================================

class Personne:
    def __init__(self, nom, email):
        self.nom = nom
        self.email = email
        self.amis = [] 

    def ajouter_un_ami(self, ami):
        """
        b) Ajoute un ami si ce n'est pas soi-même et s'il n'est pas déjà présent.
        [cite_start]Source : [cite: 81, 82]
        """
        if ami is not self and ami not in self.amis:
            self.amis.append(ami)

    def ajouter_les_amis_d_amis(self):
        """
        c) Ajoute les amis des amis (niveau 2) à sa propre liste.
        [cite_start]Source : [cite: 84, 85, 86]
        """
        amis_a_ajouter = []
        for ami_direct in self.amis:
            for ami_dist in ami_direct.amis:
                # Vérifications : pas soi-même, pas déjà ami, pas déjà marqué pour ajout
                if (ami_dist is not self) and \
                   (ami_dist not in self.amis) and \
                   (ami_dist not in amis_a_ajouter):
                    amis_a_ajouter.append(ami_dist)
        
        # On étend la liste principale
        self.amis.extend(amis_a_ajouter)
        
    def __repr__(self):
        return f"{self.nom}"

class Reseau:
    def __init__(self):
        self.personnes = [] # Liste de Personnes [cite: 77]

    def non_narcissique(self):
        """
        a) Renvoie True si personne n'est ami avec soi-même.
        [cite_start]Source : [cite: 79, 80]
        """
        for p in self.personnes:
            # On vérifie si la personne p est dans sa propre liste d'amis
            if p in p.amis:
                return False
        return True


# ==============================================================================
# PROBLÈME 4 : RÉGRESSION LINÉAIRE
# [cite_start]Source : [cite: 90, 103]
# ==============================================================================

def reg_lin(liste):
    """
    a) Calcule a et b pour la droite y = ax + b par la méthode des moindres carrés.
    [cite_start]Complexité : O(n) car on ne parcourt la liste qu'une seule fois. [cite: 105, 107]
    """
    n = len(liste)
    if n == 0: return (0, 0) # Sécurité basique

    sum_x = 0
    sum_y = 0
    sum_xx = 0 # Pour calculer E[X^2]
    sum_xy = 0 # Pour calculer E[XY]

    # [cite_start]Un seul parcours pour calculer toutes les sommes nécessaires [cite: 105]
    for (x, y) in liste:
        sum_x += x
        sum_y += y
        sum_xx += x * x
        sum_xy += x * y

    # Calcul des moyennes
    moy_x = sum_x / n
    moy_y = sum_y / n
    moy_xx = sum_xx / n
    moy_xy = sum_xy / n

    # [cite_start]Calcul Variance et Covariance selon les formules [cite: 97]
    # Var(X) = E[X^2] - (E[X])^2
    var_x = moy_xx - (moy_x * moy_x)
    
    # Cov(X,Y) = E[XY] - E[X]*E[Y]
    cov_xy = moy_xy - (moy_x * moy_y)

    if var_x == 0:
        return (0, 0) # Éviter division par zéro (droite verticale)

    # [cite_start]Calcul de a et b [cite: 100, 102]
    a = cov_xy / var_x
    b = moy_y - (a * moy_x)

    return (a, b)


# ==============================================================================
# TESTS D'EXÉCUTION
# ==============================================================================
if __name__ == "__main__":
    print("--- Test Problème 1 (Maison) ---")
    pieces = ['a', 'b', 'c', 'd']
    portes_maison = [('a', 'b'), ('b', 'c'), ('a','c'), ('b', 'a'), ('d', 'b')]
    # Test chemin 'd' vers 'c'
    print(f"Chemin d->c : {chemin('d', 'c', portes_maison, [])}") 
    # Doit donner ['d', 'b', 'c'] ou ['d', 'b', 'a', 'c']

    print("\n--- Test Problème 2 (Aire Carré) ---")
    carre = [(0,0), (0,1), (1,1), (1,0)]
    print(f"Aire du carré 1x1 : {aire(carre)}") # Doit donner 1.0

    print("\n--- Test Problème 3 (Réseau Social) ---")
    alice = Personne("Alice", "a@a.com")
    bob = Personne("Bob", "b@b.com")
    charlie = Personne("Charlie", "c@c.com")
    
    r = Reseau()
    r.personnes = [alice, bob, charlie]
    
    alice.ajouter_un_ami(bob)   # Alice -> Bob
    bob.ajouter_un_ami(charlie) # Bob -> Charlie
    
    print(f"Amis d'Alice avant : {alice.amis}")
    alice.ajouter_les_amis_d_amis()
    print(f"Amis d'Alice après ajout amis d'amis : {alice.amis}") 
    # Devrait inclure Charlie maintenant

    print("\n--- Test Problème 4 (Régression) ---")
    # Points alignés y = 2x + 1 -> (1,3), (2,5), (3,7)
    points = [(1.0, 3.0), (2.0, 5.0), (3.0, 7.0)]
    a, b = reg_lin(points)
    print(f"Points: {points}")
    print(f"Résultat: y = {a:.2f}x + {b:.2f}") # Attendu a=2.0, b=1.0