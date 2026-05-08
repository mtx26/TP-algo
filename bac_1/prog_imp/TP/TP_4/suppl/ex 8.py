def contient(n, d):
    if n <= 0:
        return False
    elif n % 10 == d:
        return True
    else:
        return contient(n // 10, d)

print(contient(56767, 3))