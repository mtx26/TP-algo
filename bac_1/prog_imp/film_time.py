hour = 21
min = 47
sec = 49

movie_hour = 3
movie_min = 48
movie_sec = 25

hour += movie_hour
min += movie_min
sec += movie_sec

hour += min // 60
min = min % 60

min += sec // 60
sec = sec % 60

hour = hour % 24

print('il est', hour, 'heure et', min, 'minutes et', sec, 'secondes')

