def peut_aller(piece1, piece2, portes, eviter):
    if piece1 == piece2:
        return True

    eviter.append(piece1)
    
    for elem in portes:

        if elem[0] == piece1 and elem[1] not in eviter:

            if peut_aller(elem[1], piece2, portes, eviter):
                return True
    return False
        

def chemin(piece1, piece2, portes, eviter):

    if piece1 == piece2:
        return [piece1]
    
    eviter.append(piece1)
    
    for p1, p2 in portes:
        if p1 == piece1 and p2 not in eviter:
            chemin_suivant = chemin(p2, piece2, portes, eviter)
            if chemin_suivant:
                return [piece1] + chemin_suivant
    
    return None

    
                
        
portes = [('b','a'),('d','a'),('a','d'),('d','a'),('d','c')]
eviter = []
print(chemin('b','c',portes, eviter))
                
