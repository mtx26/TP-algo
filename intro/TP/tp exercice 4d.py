# marche normal
min = 8
s = 15
km = 2

s += min * 60
result = s * km
# marche rapide
min_2 = 7
s_2 = 12
km_2 = 3

s_2 += min * 60
result_fast = s_2 * km_2

# heure
heure = 6
minute = 52
seconde = 0

total_time = result + result_fast

h = total_time // 3600
rest = total_time % 3600

min = rest // 60
s = rest % 60

print(h, min, s)

heure += h
minute += min
seconde += s

heure += minute // 60
minute = minute % 60

minute += seconde // 60
seconde = seconde % 60

print(heure, minute, seconde)
