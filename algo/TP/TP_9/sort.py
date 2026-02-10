"""Voir commentaires concernant ce module dans l'enonce de la serie de TP."""

import random
import umons_cpu
from copy import deepcopy


def python_sort(t):
    """Tri "built-in" de la librairie standard Python, in-place.
    Utilise le Timsort (Tim Peters, 2002), un algorithme de tri hybride entre
    merge sort et le insertion sort.
    Complexité dans le pire des cas : O(n log n).
    """
    t.sort()


def insertion_sort(t):
    """Tri par insertion, in-place.
    Complexité dans le pire des cas : O(n²)."""
    n = len(t)
    for i in range(1, n):
        clef = t[i]
        j = i - 1
        while j >= 0 and t[j] > clef:
            t[j + 1] = t[j]
            j = j - 1
        t[j + 1] = clef


def selection_sort(t):
    """Tri par sélection des minima, in-place.
    Complexité dans le pire des cas : O(n²)."""
    n = len(t)
    for i in range(n - 1):
        small = i
        for j in range(i + 1, n):
            if t[j] < t[small]:
                small = j
        (t[i], t[small]) = (t[small], t[i])


def merge_sort(t):
    """Tri par fusion fonctionnel (non in-place)."""
    n = len(t)
    if n > 1:
        (t1, t2) = split(t) # aucun effet de bord
        # car split renvoie deux nouvelles listes
        t1 = merge_sort(t1)
        t2 = merge_sort(t2)
        return merge(t1, t2)
    else:
        return t


def split(t):
    """ precondition: len(t) >= 2 """
    mid = len(t) // 2
    t1 = t[:mid]
    t2 = t[mid:]
    return t1, t2


def merge(t1, t2):
    """Fusionne deux listes triées en une nouvelle liste triée.

    Préconditions:
      - t1 et t2 sont triées en ordre croissant.
    Effets de bord:
      - Cette implémentation utilise pop() et modifie t1 et t2 pendant la
        construction du résultat.
    Retour:
      - Une nouvelle liste contenant tous les éléments de t1 et t2 en ordre
        croissant.
    Complexité: O(n) où n = len(t1) + len(t2) en nombre d'opérations.
    """
    if len(t1) == 0:
        return t2
    elif len(t2) == 0:
        return t1
    elif t1[-1] > t2[-1]:
        last = t1.pop()
        new = merge(t1, t2)
        new.append(last)
        return new
    else:
        last = t2.pop()
        new = merge(t1, t2)
        new.append(last)
        return new


def dicho_search(t, x):
    """Recherche dichotomique (binaire) d'une valeur dans une liste triée.

    Préconditions:
      - t est triée en ordre croissant.
    Paramètres:
      - t : liste triée
      - x : valeur recherchée
    Retour:
      - L'indice i tel que t[i] == x si trouvé, sinon None.
    Complexité: O(log n) en temps, O(1) en mémoire auxiliaire.
    """
    start = 0
    end = len(t) - 1
    mid = start + (end - start) // 2
    while (end - start > 0) and x != t[mid]:
        if x < t[mid]:
            end = mid - 1
        else:
            start = mid + 1
        mid = start + (end - start) // 2
    if len(t) > 0 and x == t[mid]:
        return mid
    else:
        return None


def test(n):
    """Mesure et affiche les temps d'exécution pour plusieurs tris sur 3 listes.

    Comportement:
      - Construit trois listes de taille n : croissante, décroissante, aléatoire.
      - Mesure les temps (en ms) pour selection_sort, insertion_sort et merge_sort
        appliqués à chacune de ces listes via umons_cpu.cpu_time.
      - Affiche une ligne formatée contenant n et les temps mesurés.
    Paramètre:
      - n : taille des listes à tester (int)
    Effets:
      - Affiche une ligne sur la sortie standard.
    """
    t1 = list(range(n))
    t2 = list(range(n, 0, -1))
    t3 = []
    for i in range(n):
        t3.append(random.randint(0, n))
    print('%7d %7.2f %7.2f %7.2f %7.2f %7.2f %7.2f %7.2f %7.2f %7.2f' % (
        n,
        umons_cpu.cpu_time(selection_sort, t1),
        umons_cpu.cpu_time(insertion_sort, t1),
        umons_cpu.cpu_time(merge_sort, t1),
        umons_cpu.cpu_time(selection_sort, t2),
        umons_cpu.cpu_time(insertion_sort, t2),
        umons_cpu.cpu_time(merge_sort, t2),
        umons_cpu.cpu_time(selection_sort, t3),
        umons_cpu.cpu_time(insertion_sort, t3),
        umons_cpu.cpu_time(merge_sort, t3)))


def main():
    """Point d'entrée qui affiche un en-tête et lance des tests de performance.

    Comportement:
      - Affiche des explications sur les colonnes de sortie puis lance test(i)
        pour i allant de 100 à 900 par pas de 100.
    Effets:
      - Affiche plusieurs lignes sur la sortie standard.
    """
    print('n : taille des listes')
    print('t1 : temps pour des listes triées croissantes')
    print('t2 : temps pour des listes triées décroissantes')
    print('t3 : temps pour des listes remplies aléatoirement')
    print('Temps en millisecondes')
    print('      n '
          't1: sel '
          '    ins '
          '    mer '
          't2: sel '
          '    ins '
          '    mer '
          't3: sel '
          '    ins '
          '    mer')
    for i in range(100, 901, 100):
        test(i)


if __name__ == '__main__':
    main()
