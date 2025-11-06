import math


def is_squared(nb):
    nb_2 = math.isqrt(nb)
    if (nb_2 * nb_2 == nb):
        return True
    else:
        return False





def map(list, fct):
    rep = []
    for l in list:
        rep += [fct(l)]
    return rep

# print(map(["a", "b", "c"], str.upper))
# print(map([], math.sqrt))

def filter(list, fct):
    rep = []
    for l in list:
        rep += [fct(l)]
    return rep

# print(filter([3, 4, 16, 7], is_squared))

def reduce(list, fct):
    len = 0
    for l in list:
        len += 1
    if len == 0:
        return
    
    i = -1
    rep = list[i]
    while i > -len:
        rep = fct(rep, list[i-1])
        
        i += -1

    return rep

# print(reduce([2, 3, 4], math.pow))