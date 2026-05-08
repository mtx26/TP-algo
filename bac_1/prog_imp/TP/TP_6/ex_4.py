

def insert(seq, n):
    i = 0
    len = 0
    for s in seq:
        len += 1

    while i < len and seq[i] < n:
        i += 1
    seq[i:i] = [n]
    return seq
print(insert(list(range(6)), 6))

