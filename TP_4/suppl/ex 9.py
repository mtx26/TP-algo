def pgcd(x, y):
    if (y == 0):
        return x
    else:
        r = x % y
        return pgcd(y, r)

print(pgcd(34, 16))