def aire(liste):
    n = len(liste)

    if n == 3 :
        valeur = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)
        return 0.5 * abs(valeur)
    
if __name__== "__main__":
    pass