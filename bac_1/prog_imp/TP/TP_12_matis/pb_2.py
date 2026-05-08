
# liste = [(0,0),(-0.5,1),(0,1.5),(0.5,1), (1, 0)]
liste = [(0,0), (1,0), (1,1), (0,1)]  # Aire attendue : 1.0
import math
liste = [(math.cos(2*math.pi*i/5), math.sin(2*math.pi*i/5)) for i in range(5)]  # Aire ≈ 2.3776

def aire(liste):
    i = 0
    p = len(liste)
    print(liste)
    if p < 3:
        return 0
    elif p == 3:
        x1, y1 = liste[0]
        x2, y2 = liste[1]
        x3, y3 = liste[2]
        a = 1/2 * abs((x2 - x1)*(y3-y1)-(x3-x1)*(y2-y1))
        return a
    else:
        return aire(liste[0:p//2+1]) + aire([liste[0]] + liste[p//2:]) 
       
print(aire(liste))