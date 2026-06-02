"""Voir commentaires concernant ce module dans l'enonce de la serie de TP."""

import random
import umons_cpu
from copy import deepcopy
import displayCpu

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

def bubble_sort(list):
    flag = True
    while flag :
        cnt = 0
        i = 0
        while i < (len(list) - 1) :
            if list[i] > list[i+1] :
                cnt = cnt + 1
                (list[i],list[i+1]) = (list[i+1],list[i])
            i = i + 1
        if cnt == 0 :
            flag = False
    return list

def dicho_search(t, x):
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
    
def linear_search(t, x):
    i = 0
    for elem in t :
        if x == elem :
            return i
        i = i + 1
    return None

'''
def test(n):
    t1 = list(range(n))
    x1 = n
    t2 = list(range(n))
    x2 = random.randint(0,n)
    print('%7d %7.2f %7.2f %7.2f %7.2f' % (
        n,
        umons_cpu.cpu_time(dicho_search, t1, x1),
        umons_cpu.cpu_time(linear_search, t1, x1),
        umons_cpu.cpu_time(dicho_search, t2, x2),
        umons_cpu.cpu_time(linear_search, t2, x2))
        )
    
def main():
    print('n : taille des listes')
    print('t1, x1 : temps pour des listes triées et l\'element pas dans la liste')
    print('t2, x2 : temps pour des listes triées et l\'element à une place aléatoire dans la liste')
    print('Temps en millisecondes')
    print('      n '
          't1: dic '
          '    lin '
          't2: dic '
          '    lin ')
    for i in range(100, 901, 100):
        test(i)

if __name__ == '__main__':
    main() 
'''
    
#comparaison sel/ins/mer/bub


sel_times = []
ins_times = []
mer_times = []
bub_times = []


def test(n):
    t1 = list(range(n))
    t2 = list(range(n, 0, -1))
    t3 = []
    for i in range(n):
        t3.append(random.randint(0, n))
    print('%7d %7.2f %7.2f %7.2f %7.2f %7.2f %7.2f %7.2f %7.2f %7.2f %7.2f %7.2f %7.2f' % (
        n,
        umons_cpu.cpu_time(selection_sort, t1),
        umons_cpu.cpu_time(insertion_sort, t1),
        umons_cpu.cpu_time(merge_sort, t1),
        umons_cpu.cpu_time(bubble_sort, t1),
        umons_cpu.cpu_time(selection_sort, t2),
        umons_cpu.cpu_time(insertion_sort, t2),
        umons_cpu.cpu_time(merge_sort, t2),
        umons_cpu.cpu_time(bubble_sort, t2),
        umons_cpu.cpu_time(selection_sort, t3),
        umons_cpu.cpu_time(insertion_sort, t3),
        umons_cpu.cpu_time(merge_sort, t3),
        umons_cpu.cpu_time(bubble_sort, t3)))
    
    sel_times.append(umons_cpu.cpu_time(selection_sort, t3))
    ins_times.append(umons_cpu.cpu_time(insertion_sort, t3))
    mer_times.append(umons_cpu.cpu_time(merge_sort, t3))
    bub_times.append(umons_cpu.cpu_time(bubble_sort, t3))



def main():
    print('n : taille des listes')
    print('t1 : temps pour des listes triées croissantes')
    print('t2 : temps pour des listes triées décroissantes')
    print('t3 : temps pour des listes remplies aléatoirement')
    print('Temps en millisecondes')
    print('      n '
          't1: sel '
          '    ins '
          '    mer '
          '    bub '
          't2: sel '
          '    ins '
          '    mer '
          '    bub '
          't3: sel '
          '    ins '
          '    mer'
          '    bub ')
    for i in range(100, 901, 100):
        test(i)


if __name__ == '__main__':
    main()

if __name__ == '__main__':

    afficheur = displayCpu.CpuPlot([100, 200, 300, 400, 500, 600, 700, 800, 900])   

    afficheur.prepare(sel_times, "sel")
    afficheur.prepare(ins_times, "ins")
    afficheur.prepare(mer_times, "mer")
    afficheur.prepare(bub_times, "bub")

    afficheur.draw()

    input("Press [Enter] to exit.")


#comparaison mer/pyth sort
'''
merge_times = []
python_sort_times = []

def test(n):
    t1 = list(range(n))
    t2 = list(range(n, 0, -1))
    t3 = []
    for i in range(n):
        t3.append(random.randint(0, n))
    print('%7d %7.2f %7.2f %7.2f %7.2f %7.2f %7.2f' % (
        n,
        umons_cpu.cpu_time(merge_sort, t1),
        umons_cpu.cpu_time(python_sort, t1),
        umons_cpu.cpu_time(merge_sort, t2),
        umons_cpu.cpu_time(python_sort, t2),
        umons_cpu.cpu_time(merge_sort, t3),
        umons_cpu.cpu_time(python_sort, t3)))
    
    merge_times.append(umons_cpu.cpu_time(merge_sort, t3))
    python_sort_times.append(umons_cpu.cpu_time(python_sort, t3))



def main():
    print('n : taille des listes')
    print('t1 : temps pour des listes triées croissantes')
    print('t2 : temps pour des listes triées décroissantes')
    print('t3 : temps pour des listes remplies aléatoirement')
    print('Temps en millisecondes')
    print('      n '
          't1: mer '
          '    pyt '
          't2: mer '
          '    pyt '
          't3: mer '
          '    pyt ')
    for i in range(100, 901, 100):
        test(i)


if __name__ == '__main__':
    main()

if __name__ == '__main__':

    afficheur = displayCpu.CpuPlot([100, 200, 300, 400, 500, 600, 700, 800, 900])   

    afficheur.prepare(merge_times, "mer")
    afficheur.prepare(python_sort_times, "pyth sort")

    afficheur.draw()

    input("Press [Enter] to exit.")
'''