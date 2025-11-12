
i = 563545
l = 1
result = 0
while i > 9:
    while l > 0:
        a = i % 10
        i = i // 10
        
        result += a
        if (i == 0):
            l = 0
        print(result)
    i = result
    print(i)

print(result)



