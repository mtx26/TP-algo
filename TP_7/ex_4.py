import random

def creerEnchevetrements(bag, i, max):
    res = []
    nb_ench = random.randrange(0, max)
    # print(nb_ench)
    for j in range(nb_ench):
        x = random.choice(bag)
        while x == i:
            x = random.choice(bag)

        already_in = False

        if res != []:
            already_in = False
            for l in res:
                if l == [x, i]:
                    already_in = True
                    # print("-", [x, i])
        if not already_in:
            res.append([x, i])
        

    return res

# print(creerEnchevetrements([0, 1, 2, 3, 4, 5], 2, 10))

def inverser(list):
    copy_list = list[:]
    copy_list[0], copy_list[1] = copy_list[1], copy_list[0]
    return copy_list

def creerMikado(bag):
    game = []
    for i in bag:
        row = creerEnchevetrements(bag, i, len(bag))
        for new_ench in row:
            already_in = False
            for g in game:
                if inverser(new_ench) == g:
                    already_in = True
                    # print("-", new_ench)

            if not already_in:
                game.append(new_ench)

    return game

# print(creerMikado([0, 1, 2, 3, 4, 5]))

def peutRetirer(i, bag, game):
    res = True
    for g in game:
        # print(g, g[0] == i, g[1] in bag, (g[0] == i) and (g[1] in bag))
        if (g[0] == i) and (g[1] in bag):
            res = False
    return res

def which(bag, game):
    res = []
    if len(bag) == 1:
        return bag
    else:
        for x in bag:
            if peutRetirer(x, bag, game):
                res.append(x)
                bag.remove(x)
                rep = which(bag, game)
                if rep != None:
                    return res + rep
        return None

def main(bag):
    game = creerMikado(bag)
    return which(bag, game), game

if __name__ == "__main__":
    sac_initial = [0, 1, 2, 3, 4, 5, 6]
    ordre, contraintes = main(sac_initial[:])

    print("\n========== Mikado ==========")
    print(f"Sac initial : {sac_initial}")
    
    print("\nContraintes (i dépend de j) :")
    if contraintes:
        for a, b in sorted(contraintes):
            print(f"  - {a} dépend de {b}")
    else:
        print("  (aucune)")
    
    if ordre is None:
        print("\nOrdre de retrait : impossible")
    else:
        print("\nOrdre de retrait :")
        print("  " + " -> ".join(map(str, ordre)))
    print("============================\n")

