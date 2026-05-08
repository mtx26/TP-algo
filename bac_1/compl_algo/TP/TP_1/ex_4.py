def square_even(t):
    return [x**2 for x in t if x % 2 == 0]

print(square_even([1, 2, 3, 4, 5, 6]))

def same_square_odd(t, u):
    return list(set(x**2 for x in t if x % 2 != 0) & set(x**2 for x in u if x % 2 != 0))

print(same_square_odd([1, 2, 3, 3, 5, 7, 9], [3, 4, 7, 5, 3, 7, 11]))

def runner(times :list):
    return sorted([ (t // 60, t % 60) for t in times if t // 60 < 10 ], reverse=True)

print(runner([620, 450, 800, 390, 720, 550]))