def peut_aller(piece1, piece2, portes, eviter=None):
    if eviter is None:
        eviter = []
    if piece1 == piece2:
        return True
    for porte in portes:
        p1, p2 = porte
        if p1 == piece1 and p2 not in eviter:
            if peut_aller(p2, piece2, portes, eviter + [p2]):
                return True
    return False
print(peut_aller("a", "d", [("a", "c"), ("a", "b"), ("b", "c"), ("c", "d")]))

def chemin(piece1, piece2, portes, eviter=None):
    if eviter is None:
        eviter = []
    if piece1 == piece2:
        return [piece1]
    for porte in portes:
        p1, p2 = porte
        if p1 == piece1 and p2 not in eviter:
                return [piece1] + chemin(p2, piece2, portes, eviter + [p2])
    return []

print(chemin("a", "d", [("a", "c"), ("a", "b"), ("b", "c"), ("c", "d")]))