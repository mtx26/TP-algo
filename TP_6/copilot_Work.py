"""code made by copilot to help us understanding certains things while doing this by ourselves"""

import math
from typing import Callable, List, Optional, Any


def map(func: Callable[[Any], Any], seq) -> list:
    """Applique func à chaque élément de seq et retourne une nouvelle liste."""
    result = []
    for x in seq:
        result.append(func(x))
    return result


def filter(func: Callable[[Any], bool], seq) -> list:
    """Retourne une nouvelle liste ne contenant que les éléments pour lesquels func(x) est vrai."""
    result = []
    for x in seq:
        if func(x):
            result.append(x)
    return result


def reduce(func: Callable[[Any, Any], Any], seq) -> Any:
    """Combine les éléments de seq en appliquant func successivement (left-fold).
    Précondition: len(seq) >= 2
    """
    if len(seq) < 2:
        raise ValueError("reduce requires at least two elements")
    acc = seq[0]
    for x in seq[1:]:
        acc = func(acc, x)
    return acc


def prime_numbers(n: int) -> List[int]:
    """Retourne la liste des n premiers nombres premiers.
    On utilise la méthode de test par division par les premiers déjà trouvés jusqu'à sqrt(i).
    """
    if n <= 0:
        return []
    primes: List[int] = []
    candidate = 2
    while len(primes) < n:
        is_p = True
        limit = int(math.isqrt(candidate))
        for p in primes:
            if p > limit:
                break
            if candidate % p == 0:
                is_p = False
                break
        if is_p:
            primes.append(candidate)
        candidate += 1
    return primes


def is_prime(n: int) -> bool:
    """Teste si n est premier."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(math.isqrt(n))
    i = 3
    while i <= limit:
        if n % i == 0:
            return False
        i += 2
    return True


def insert(seq: List[int], n: int) -> None:
    """Insère n dans seq (triée) pour que seq reste triée. Modifie seq en place.
    Utilise uniquement append/pop et les opérateurs []/slice.
    """
    i = 0
    while i < len(seq) and seq[i] < n:
        i += 1
    seq[i:i] = [n]


def produit_matriciel(A: List[List[float]], B: List[List[float]]) -> Optional[Any]:
    """Calcule le produit matriciel A (m x n) * B (n x p).
    Retourne None si les dimensions ne conviennent pas.
    Si le résultat est 1x1, retourne un scalaire.
    """
    if not A or not B:
        return None
    m = len(A)
    n = len(A[0])
    for row in A:
        if len(row) != n:
            return None
    nb_rows_B = len(B)
    if nb_rows_B != n:
        return None
    p = len(B[0])
    for row in B:
        if len(row) != p:
            return None

    C: List[List[float]] = []
    for i in range(m):
        rowC = []
        for j in range(p):
            s = 0.0
            for k in range(n):
                s += A[i][k] * B[k][j]
            rowC.append(s)
        C.append(rowC)

    if m == 1 and p == 1:
        return C[0][0]
    return C


if __name__ == "__main__":
    import math as _m
    print("Tests myList:")
    print("map sqrt [] ->", map(_m.sqrt, []))
    print("map sqrt [2.0,4.0,6.0,100.0] ->", map(_m.sqrt, [2.0,4.0,6.0,100.0]))
    print("map str.upper 'hello' ->", map(str.upper, list('hello')))
    print("filter primes <20 ->", filter(is_prime, range(20)))
    print("filter isalpha 'r2d2' ->", filter(str.isalpha, list('r2d2')))
    print("reduce pow [2,2] ->", reduce(_m.pow, [2,2]))
    print("reduce pow [2,3,4] ->", reduce(_m.pow, [2,3,4]))
    print("prime_numbers(1) ->", prime_numbers(1))
    print("is_prime(1,2,3,33) ->", is_prime(1), is_prime(2), is_prime(3), is_prime(33))
    seq = list(range(6))
    insert(seq, -1)
    print("insert(range(6), -1) ->", seq)
    seq2 = list(range(6))
    insert(seq2, 3)
    print("insert(range(6), 3) ->", seq2)
    print("produit_matriciel tests ->")
    print(produit_matriciel([[2,0,1],[3,6,2]], [[1,5],[2,6],[3,7]]))
    print(produit_matriciel([[1,5],[2,6],[3,7]], [[2,0,1],[3,6,2]]))
    print(produit_matriciel([[1.0,2.5]], [[3.0],[4.5]]))
    print(produit_matriciel([[1.0,2.5]], [[3.0,4.5]]))
    print(produit_matriciel([[1,5],[2,6],[3,7]], [[1,5],[2,6],[3,7]]))
