def peut_aller(piece1, piece2, portes, eviter):
        if piece1 == piece2:
            return True
    
        for (p_dep, p_arr) in portes:
            if p_dep == piece1 and p_arr not in eviter:
                if peut_aller(p_arr, piece2, portes):
                    return True

def chemin(piece1, piece2, portes, eviter):
    pass

def plus_court_chemin(piece1, piece2, portes, eviter):
    pass

if __name__== "__main__":
    pass