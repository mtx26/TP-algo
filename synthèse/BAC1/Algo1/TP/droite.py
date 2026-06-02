import math


def droite(p1, p2) :
    
    if p1 != p2 :
        x1 , y1 = p1[0] , p1[1]
        x2 , y2 = p2[0] , p2[1]

        vecteurDirecteur = (x2 - x1 , y2 - y1) #-b a
        (a, b) = ( y2 - y1 , -  x2 + x1) #vecteur normal

        c = a*x1 + b*y1

        return (a, b, c)



def appartient(d, p) :

    a, b, c = d[0] , d[1] , d[2]
    x , y = p[0] , p[1]

    if a*x + b*y == c :
        return True
    else :
        return False
    

def paralleles(d1, d2) :

    a1, b1 = d1[0] , d1[1]
    a2, b2 = d2[0] , d2[1]
    
    if a1*b2 - a2*b1 == 0 :
        return True
    else :
        return False
    
def intersection(d1, d2) :

    a1, b1, c1 = d1[0] , d1[1] , d1[2]
    a2, b2, c2 = d2[0] , d2[1] , d2[2]

    if a1*b2 - a2*b1 != 0 :
        determinant = a1*b2 - a2*b1
        return ((c1*b2 - c2*b1)/determinant , (c2*a1 - c1*a2)/determinant)
    
def droite_normale(d, p) :
    a,b = -d[1] , d[0]
    x,y = p[0], p[1]
    c = a*x + b*y
    return(a,b,c)

def distance_droite_point(d3, p3) :

    d2 = droite_normale(d3, p3)
    (x, y) = intersection(d3, d2)
    return math.sqrt((p3[0] - x)**2 + (p3[1] - y)**2)
    



    

    
    

