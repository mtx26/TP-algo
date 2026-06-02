def aire(liste):
    if len(liste) == 3 :
        my_aire = abs((liste[1][0]-liste[0][0])*(liste[2][1]-liste[0][1]) - (liste[2][0]-liste[0][0])*(liste[1][1]-liste[0][1]))/2
        return my_aire
    else :
        p_i = 0
        p_j = len(liste)//2
        new_liste1 = liste[:p_j + 1]
        new_liste2 = liste[p_j:]
        new_liste2.append(liste[p_i])
        return aire(new_liste1) + aire(new_liste2)