import random

def creerEnchevetrements(bag, i, max):
    """Génère aléatoirement une liste d'enchevêtrements pour l'élément i.

    Paramètres:
    - bag (list): liste des identifiants disponibles (entiers).
    - i (int): identifiant de la baguette pour laquelle on crée des enchevêtrements.
    - max (int): borne supérieure (exclu) du nombre maximal d'enchevêtrements à tenter.

    Retour:
    - list de paires [x, i] représentant des enchevêtrements où x empêche i.
    """
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
    """Retourne une copie de la liste de deux éléments avec l'ordre inversé.

    Paramètres:
    - list (list): liste de deux éléments [a, b].

    Retour:
    - list: nouvelle liste [b, a].
    """
    copy_list = list[:]
    copy_list[0], copy_list[1] = copy_list[1], copy_list[0]
    return copy_list

def creerMikado(bag):
    """Construit un jeu de Mikado (liste d'enchevêtrements) unique.

    Paramètres:
    - bag (list): liste des identifiants des baguettes.

    Retour:
    - list de paires [a, b] représentant les contraintes du jeu (a dépend de b).
    """
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
    """Indique si la baguette i peut être retirée du sac donné les contraintes.

    Paramètres:
    - i (int): identifiant de la baguette à tester.
    - bag (list): liste actuelle des baguettes encore présentes.
    - game (list): liste des contraintes [a, b] signifiant 'a dépend de b'.

    Retour:
    - bool: True si i peut être retiré (aucune contrainte active le bloquant), sinon False.
    """
    res = True
    for g in game:
        # print(g, g[0] == i, g[1] in bag, (g[0] == i) and (g[1] in bag))
        if (g[0] == i) and (g[1] in bag):
            res = False
    return res

def which(bag, game):
    """Calcule récursivement un ordre valide de retrait des baguettes si possible.

    Paramètres:
    - bag (list): liste des baguettes restantes (modifiée localement pendant la recherche).
    - game (list): contraintes du jeu.

    Retour:
    - list: ordre de retrait (liste d'identifiants) si une solution existe.
    - None: si aucun ordre complet n'est possible.
    """
    if len(bag) == 1:
        return bag
    else:
        for x in bag:
            if peutRetirer(x, bag, game):
                new_bag = []
                for y in bag:
                    if y != x:
                        new_bag.append(y)
                rep = which(new_bag, game)
                if rep is not None:
                    return [x] + rep
        return None

def main(bag):
    """Fonction principale pour générer un jeu et obtenir un ordre de retrait.

    Paramètres:
    - bag (list): sac initial de baguettes.

    Retour:
    - tuple: (ordre, game) où ordre est la liste de retrait ou None, et game la liste des contraintes.
    """
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

