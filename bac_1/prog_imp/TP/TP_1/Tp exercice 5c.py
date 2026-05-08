def distance(km, min, s):

    ml = km/1.61

    s += min * 60

    ml_h = ml/s
    ml_h = ml_h * 3600

    s_ml = s/ml
    return (s_ml)
result = distance(10, 43, 30)
print(result)