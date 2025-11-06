import math

def prime_number(n):
    i = 0
    rep = []
    num = 2

    while i < n:
        len = math.ceil(math.sqrt(num))
        j = 2
        isprime = True
        if num == len:
            rep += [num]
        while j <= len:
            if num % j == 0:
                isprime = False
            j += 1
        if isprime:
            rep += [num]
            i += 1
        num += 1
    return rep

print(prime_number(9))



