def add_mat(A, B):
    C = []
    if len(A) == len(B) and len(A[0]) == len(B[0]) :
        i = 0
        while i < len(A) :
            j = 0
            sous_liste = []
            while j < len(A[0]):
                somme = A[i][j] + B[i][j]
                sous_liste.append(somme)
                j = j + 1
            C.append(sous_liste)
            i = i + 1
        return C
    
    else :
        return None

def determinant(m, det=0):
    if len(m) == 2 :
        det = m[0][0]*m[1][1] - m[0][1]*m[1][0]
        return det
    else :
        j = 0
        while j < len(m):
            n = suppression(m, 1, j)
            M = determinant(n)
            C = ((-1)**(1 + j)) * M
            a = m[1][j]
            det = det + a*C
            j = j + 1
        return det 

def suppression(m, i, j):
    n = []
    k = 0
    while k < len(m):
        l = 0
        sous_liste = []
        while l < len(m) :
            if k != i and l != j :
                sous_liste.append(m[k][l])
            l = l + 1
        if sous_liste != [] :
            n.append(sous_liste)
        k = k + 1
    return n

def creer_matrice(n_tache, contraintes):
    T = []
    i = 0
    while i < n_tache :
        j = 0
        sous_liste = []
        while j < n_tache :
            if (i, j) in contraintes :
                sous_liste.append(True)
            else :
                sous_liste.append(False)
            j = j + 1
        T.append(sous_liste)
        i = i + 1
    return T




        



    
    









