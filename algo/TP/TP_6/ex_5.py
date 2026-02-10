def produit_matriciel(A, B):
    m = 0
    n = 0
    n2 = 0
    p = 0

    # calculer m et n
    for l in A:
        m += 1
    for c in A[0]:
        n += 1

    # calculer n et p
    for l in B:
        n2 += 1
    for c in B[0]:
        p += 1

    if n != n2:
        return None

    # creation matrice rep :
    i = 0
    row = []
    while i < m:
        row2 = [0]*p
        row.append(row2)
        i += 1
    print(row)
            

    i = 0
    while i < m:
        j = 0
        while j < p:
            k = 0
            rep = 0
            while k < n:
                rep += A[i][k] * B[k][j]
                k += 1
            row[i][j] = rep
            j += 1
        i += 1

    return row

print(produit_matriciel([[1, 5], [2, 6], [3, 7]], [[2, 0, 1], [3, 6, 2]]))