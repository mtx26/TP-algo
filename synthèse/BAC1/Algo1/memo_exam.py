#fonction à connaitre pour l'exam

#Algo de tri

 # 1. Tri par Selection (O(n²))

def selection_sort(t):
    n = len(t)                                      # n est le nbr d'elem dans t
    for i in range(n-1):                            # pour tout elem de la liste, on suppose que i est le + petit (on s'arrete à l'avant dernier -> dernier est trié)
        small = i
        for j in range(i+1, n):
            if t[j] < t[small]:                     # pour tout elem après i, on regarde si il est + petit, si oui, il devient small
                small = j                           # -> on trouve le plus petit
        (t[i],t[small]) = (t[small],t[i])           # le + petit prend la place de i et i prend sa place puis on reco avec le suivant
    return t


  # 2. Tri par Insertion (O(n²))

def insertion_sort(t):
    n = len(t)
    for i in range(1, n):                         # on regarde tout les elements à partir du 2e
        clef = t[i]                               # l'elem qu'on va placer est le ieme, la clef
        j = i - 1                                 # on s'interesse a l'elem avant le ieme
        while j >= 0 and t[j] > clef :            # tant que j est dans l'index et qu'il est plus grand que i, on decale i, pour cela :
            t[j + 1] = t[j]                          # on avance j de 1
            j = j - 1                                # on regarde l'elem anterieur en décrémentant j

            # on refait tant que j > i et que j n'est pas négatif (cad y a plus d'elem, on a fait le 1er)

        t[j+1] = clef                             #on met la clef à sa bonne place, la ou on s'est arreté
                                                    # on recommence pour chaque elem
    return t



    # 3. Tri par Fusion (O(nlog(n)))

def merge_sort(t):
    n = len(t)
    if n > 1 :
        (t1,t2) = split(t)                         # on divise la liste en 2 parties
        t1 = merge_sort(t1)
        t2 = merge_sort(t2)                        # on trie récursivement les 2 sous listes
        return merge(t1,t2)                        # on retourne les 2 listes assemblées
    else :
        return t                                   # si la liste n'a qu'un seul elem, on retourne juste la liste
    

    # split et merge O(n²)

def split(t):
    mid = len(t)//2
    t1 = t[:mid]
    t2 = t[mid:]
    return t1, t2

def merge(t1,t2):
    if len(t1) == 0 :                             # si une des 2 listes est vide, il suffit de retourner l'autre (cas de base)
        return t2
    if len(t2) == 0 :
        return t1
    elif t1[-1] > t2[-1] :                        # si le dernier de t1 est + grand que celui de t2
        last = t1.pop()                           # on enleve le dernier elem de t1 et on stock dans last
        new = merge(t1,t2)                        # on fusionne recursivement t1 et t2
        new.append(last)                          # on rajt last a la fin
        return new                                # on retourne la fusion
    else :
        last = t2.pop()                           # si c'est le dernier de t2 le + grand : on fait la meme mais on pop t2
        new = merge(t1, t2)
        new.append(last)
        return new
    

    # 4. Tri à bulle O(n²)

def bubble_sort(t):
    n = len(t)
    flag = True
    while flag :
        cnt = 0
        i = 0
        while i < n-1 :                            # si l'elem anterieur est plus grand que l'elem suivant, on switch et on "met une croix"
            if t[i] > t[i+1] :
                cnt = cnt + 1
                (t[i],t[i+1]) = (t[i+1],t[i])
            i = i + 1
        if cnt == 0 :                           # si on a rien touché (pas de "croix") -> c'est trié -> STOP
            flag = False
    return t

    
# Recherche d'un element dans une liste


    # Recherche linéaire O(n):

def linear_search(x, t):
    for i in range(len(t)-1) :
        if t[i] == x :                           # on parcour tout, si on trouve x on retourne la pos, sinon on retourne -1
            return i + 1
    return -1

    # Recherche dichotomique iteratif O(log(n))

def dicho_search_ite(x, t):
    start = 0                                     # on initialise le start et le end de la zone de recherche
    end = len(t) - 1
    mid = start + (end - start) // 2              # on calcule le milieu de la zone de recherche sur cette base
    while (end - start > 0) and x != t[mid] :     # tant que la zone de recherche est non-nulle et qu'on a pas trouvé x sur un milieu
        if x < t[mid] : 
            end = mid - 1                         # si x est + petit que le milieu, on raccourci par le haut
        else :
            start = mid + 1                       # si x est + grand que le milieu, on raccourci par le bas
        mid = start + (end - start) // 2          # on réévalue le milieu sur base des nouveaux start et end
    if len(t) > 0 and t[mid] == x :
        return mid
    else :                                        # il reste un elem, si  c'est x on donne la pos (mid) sinon on retourne -1
        return -1

    
    # Recherche dichotomique récursif O(???)

def dicho_search_rec(x, t):
    if len(t) == 0 :
        return False
    mid = len(t)//2
    if x < t[mid] :
        return dicho_search_rec(x, t[:mid])
    elif x > t[mid] :
        return dicho_search_rec(x, t[mid+1:])
    elif x == t[mid]:
        return True


# Produit matriciel 

def produit_matriciel(A, B):
    if len(A[0]) == len(B) :                      # on check si nbr de colonnes de A = nbr de lignes de B
        C = []                                    # on créé notre matrice vide qui sera A x B = C
        i = 0                
        while i < len(A) :                        # on parcours toutes les lignes de A
            j = 0
            sous_liste = [] 
            while j < len(B[0]):                  # on parcours toutes les colonnes de B
                k = 0
                somme = 0
                while k < len(B):
                    somme = somme + A[i][k]*B[k][j]       # on fait la multiplication en suivant la formule (par ex : 1er elem 1ere ligne A x 1er elem 1ere colonne B)
                    k = k + 1                               # on parcours tout les elements avec k et on en fait la somme qu'on ajt à la sous liste (on crée une ligne de C)
                sous_liste.append(somme)
                j = j + 1                                 # on continue avec les colonnes de B suivantes
            C.append(sous_liste)                 # on ajt les lignes à la matrice C
            i = i + 1                                  # on refait tt avec les lignes de A suivantes 
        return C
    # on retourne la matrice C
    else :
        return None                     # si le produit matriciel n'a aucun sens --> None
         

