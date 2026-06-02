def map(f, l):
    new_l = []
    for elem in l :
        current = f(elem)
        new_l.append(current)
    return new_l

def filter(f, l):
    new_l = []
    for elem in l :
        current = elem
        if f(current) == True :
                new_l.append(elem)
    return new_l
          
def reduce(f, l):
    new_l = []
    i = 1
    last = l[0]
    while i < len(l):
        current = l[i]
        add = f(last, current)
        last = add
        i = i + 1
    new_l.append(add)
    return new_l

def prime_numbers(n): 
     i = 1
     prime_found = 0
     prime_list = []
     while True :
        div_found = 0
        for nbr in range(1, i+1):
            if i%nbr == 0 :
                div_found = div_found + 1
        if div_found == 2 :
            prime_found = prime_found + 1
            prime_list.append(i)
        if prime_found == n :
            return prime_list
        i = i + 1

def is_prime(n):
    div_found = 0
    for nbr in range(1, n+1):
        if n%nbr == 0 :
            div_found += 1
    if div_found == 2 :
        return True
    else :
        return False
    
def insert(seq, n):
    i = 0
    if len(seq) == 0 :
        return [n]
    if seq[0] > n :
        pos = 0
    if seq[len(seq)-1] < n :
        seq.append(n)
        return seq
    else :
        found = False
        while i < len(seq) and not found:
            if seq[i] >= n:
                pos = i
                found = True
            i = i + 1
    new_seq = []
    cnt = 0
    for elem in seq :
        if cnt == pos :
            new_seq.append(n)
            new_seq.append(elem)
        else :
            new_seq.append(elem)
        cnt = cnt + 1
    return new_seq
        
def produit_matriciel(A, B):
    if len(A[0]) == len(B) :
        C = []
        i = 0
        while i < len(A) :
            j = 0
            sous_liste = [] 
            while j < len(B[0]):
                k = 0
                somme = 0
                while k < len(B):
                    somme = somme + A[i][k]*B[k][j]
                    k = k + 1
                sous_liste.append(somme)
                j = j + 1
            C.append(sous_liste)   
            i = i + 1
        return C

    else :
        return None
    


    


              
             


