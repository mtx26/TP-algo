import random

def peut_retirer(i, bag, jeu):
    if i not in bag :
        return False
    else :
        for couple in jeu :
            if i == couple[0]:
                return False
        return True
    
def est_jouable(bag, jeu):
    if len(jeu) == 0 :
        return True
    else :
        for i in bag :
            if peut_retirer(i, bag, jeu):
                new_jeu = []
                new_bag = []
                for couple in jeu :
                    if i != couple[1]:
                        new_jeu.append(couple)
                for elem in bag :
                    if elem != i :
                        new_bag.append(elem)
                return est_jouable(new_bag, new_jeu)
        return False 
    

my_bag = [0,1,2,3,4,5]
#my_jeu = [(0,1),(1,2),(2,0)]
#print(est_jouable(my_bag,my_jeu))

def creerEnchevetrements(bag, i, max):
    if i not in bag :
        return None
    if max > len(bag) -1 :
        max = len(bag)-1
    list_enchev = []
    x_used = []
    nbr_enchev = random.randint(0,max-1)
    if nbr_enchev == 0 :
        return []
    while len(list_enchev) <= nbr_enchev :
        x = random.randint(0,len(bag)-1)
        if x not in x_used and x != i :
            list_enchev.append((i,x))
            x_used.append(x)
    return list_enchev

#print(creerEnchevetrements(my_bag, 2, 4))

       
def creerMikado(bag):
    mikado = []
    for i in bag :
        mikado = mikado + creerEnchevetrements(bag, i, len(bag))
    return mikado

#print(creerMikado(my_bag))


mikado = creerMikado(my_bag)
while not est_jouable(my_bag, mikado) :
    mikado = creerMikado(my_bag)


def quelOrdre(bag, jeu, path=[]):
    if len(jeu) == 0 :
        return path
    else :
        for i in bag :
            if peut_retirer(i, bag, jeu):
                new_jeu = []
                new_bag = []
                for couple in jeu :
                    if i != couple[1]:
                        new_jeu.append(couple)
                for elem in bag :
                    if elem != i :
                        new_bag.append(elem)
                path.append(i)
                return quelOrdre(new_bag, new_jeu, path)
        return False

print('Pour résoudre le mikado :' ,mikado, '. Suivez les instructions suivantes : ' )
print(quelOrdre(my_bag,mikado))


