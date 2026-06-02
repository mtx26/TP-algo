def fibo(n):
    a = 0
    b = 1
    cnt = 1
    yield a
    yield b
    while cnt < n :
        a, b = b, a+b
        yield b
        cnt += 1


#gen = fibo(15)
#for elem in gen :
    #print(elem)


def permutations(elements, current = []):
    if len(elements) == 0:                      # si on a plus rien dans éléments, on a tous placé --> Ok, on yield la permutation
        yield current
    else :
        for i in range(len(elements)):          # pour chaque élément de la liste 
            for p in permutations(elements[:i]+elements[i+1:], current + [elements[i]]):   # on fait toutes les permutations ou elements[i] est 1er (les éléments restants sont ceux d'avant sans elements[i])
                yield p                                                                    # on yield la pré-permutation

permu = permutations([1,2,3,4,5])

#for elem in permu :
    #print(elem)


def subsets(n, i=0, current= set()):
    if i == n:                                    # si on est arrivé à la taille max --> stop on retourne le subset
        yield current
    else :
        current.add(i)                            # cas ou on ajoute i
        yield from subsets(n, i+1, current)
        current.remove(i)                         # cas ou on ne met pas i
        yield from subsets(n, i+1, current)
    

for s in subsets(3):
    print(s)

    