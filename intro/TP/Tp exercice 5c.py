def distance(km):

    ml = km/1.61

    min = 43
    s = 30

    s += 43 * 60

    ml_h = ml/s
    ml_h = ml_h * 3600

    s_ml = s/ml
    return (s_ml)
result = distance(10)
print(result)