
def calculterCash(x1, x2, x3, x4, x5):
    cash = 0
    cash += x1 * 20
    cash += x2 * 10
    cash += x3 * 5
    cash += x4 * 2
    cash += x5 * 1
    return cash

def getnotes(noteEuro, prix):
    notes = prix // noteEuro
    rest = prix % noteEuro
    return notes, rest

def rendreMonnaie(prix, x1, x2, x3, x4, x5):
    cash = calculterCash(x1, x2, x3, x4, x5)
    print(cash)
    prix = cash - prix

    x1, rest = getnotes(20, prix)
    x2, rest = getnotes(10, rest)
    x3, rest = getnotes(5, rest)
    x4, rest = getnotes(2, rest)
    x5, rest = getnotes(1, rest)
    return x1, x2, x3, x4, x5

x1, x2, x3, x4, x5 = rendreMonnaie(42, 1, 2, 4, 1, 1)
print(x1, x2, x3, x4, x5)
