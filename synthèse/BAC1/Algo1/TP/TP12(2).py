def reg_lin(liste):
    somme_x = 0
    somme_y = 0
    for elem in liste :
        somme_x = somme_x + elem[0]
        somme_y = somme_y + elem[1]
    moyenne_x = somme_x / len(liste)
    moyenne_y = somme_y / len(liste)

    somme_x_carré = 0
    for elem in liste :
        somme_x_carré = somme_x_carré + (elem[0])**2
    moyenne_x_carré = somme_x_carré / len(liste)
    variance = moyenne_x_carré - moyenne_x**2

    somme_produit = 0
    for elem in liste :
        somme_produit = somme_produit + (elem[0]*elem[1])
    moyenne_somme_produit = somme_produit / len(liste)
    covariance = moyenne_somme_produit - (moyenne_x * moyenne_y)

    a = covariance/variance
    b = moyenne_y - a*moyenne_x
    return (a,b)

    
    



