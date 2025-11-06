import math
def is_prime(num):
    len = math.ceil(math.sqrt(num))
    j = 2
    isprime = True
    if num == len:
        return True
    while j <= len:
        if num % j == 0:
            isprime = False
        j += 1
    return isprime


print(is_prime(28))
    