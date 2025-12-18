def peut_aller(piece1, piece2, portes, eviter):
        if piece1 == piece2:
            return True
    
        for (p_dep, p_arr) in portes:
            if p_dep == piece1 and p_arr not in eviter:
                if peut_aller(p_arr, piece2, portes):
                    return True

def chemin(piece1, piece2, portes, eviter):
    chemin = []
    if piece1 == piece2:
        return [piece1]
    
    nouvel_eviter = eviter + [piece1]
    
    for (p_dep, p_arr) in portes:
        if p_dep == piece1 and p_arr not in eviter:
            resultat = chemin(p_arr, piece2, portes, nouvel_eviter)
            if resultat is not None:
                return [piece1] + resultat
    return None

if __name__== "__main__":
    pass