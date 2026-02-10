import random


def creerEnchevetrements(bag, i, max):
    """Crée des enchevêtrements aléatoires pour la baguette i."""
    nb = random.randint(0, max)
    autres = [x for x in bag if x != i]
    random.shuffle(autres)
    return [(x, i) for x in autres[:nb]]


def creerMikado(bag):
    """Crée un jeu de Mikado à partir d'un ensemble de baguettes."""
    jeu = []
    for i in bag:
        jeu += creerEnchevetrements(bag, i, len(bag))
    return jeu


def peutRetirer(i, bag, jeu):
    """Détermine si la baguette i peut être retirée du jeu."""
    for (a, b) in jeu:
        if a == i and b in bag:
            return False
    return True


def quelOrdre(bag, jeu):
    """Détermine l'ordre possible pour retirer les baguettes."""
    if not bag:
        return []

    for i in bag:
        if peutRetirer(i, bag, jeu):
            nouveau_bag = [x for x in bag if x != i]
            suite = quelOrdre(nouveau_bag, jeu)
            if suite is not None:
                return [i] + suite

    return None


if __name__ == "__main__":
    bag = [0, 1, 2, 3]
    jeu = [(0, 1), (0, 2), (3, 2)]
    print("Baguettes :", bag)
    print("Enchevêtrements :", jeu)
    print("Ordre possible :", quelOrdre(bag, jeu))

    bag2 = list(range(5))
    jeu2 = creerMikado(bag2)
    print("\n=== Mikado aléatoire ===")
    print("Baguettes :", bag2)
    print("Enchevêtrements générés :", jeu2)
    print("Ordre possible :", quelOrdre(bag2, jeu2))