def somme1(n):
    if n == 0:
        return 0
    else:
        # il manque le return
        somme1(n-1)+n


def somme2(n):
    if n == 0:
        return 0
    else:
        # dans la parenthese il faut n-1 pour diminuer le nombre a chaque a fois
        return somme2(n)+n


def somme3(n):
    if n == 0:
        return 0
    else:
        return n+somme3(n-1)
# c'est a bonne


def somme4(n):
    if n == 0:
        res = 0
    else:
        somme4(n)+n
        # le res n'est pas declaré ici
        return res


def somme5(n):
    # manque la condition de sortie
    return somme5(n-1)+n
