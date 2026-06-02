def compresser(s):
    new_s = ''
    i = 0
    while i < len(s):
        if i == 0 or s[i] != s[i-1]:
            j = i + 1
            cnt = 1
            while j < len(s) and s[i] == s[j]:
                cnt = cnt + 1
                j = j + 1
            if cnt == 1 :
                new_s = new_s + s[i]
            else :
                new_s = new_s + str(cnt) + s[i]
        i = i + 1
    return new_s


#mot = 'aaabaccccaa'


def decompresser(s):
    new_s = ''
    i = 0
    while i < len(s):
        if s[i].isdigit():
            flag = True
            cnt = s[i]
            j = i + 1
            while s[j].isdigit() and j < len(s):
                cnt = cnt + s[j]
                j = j + 1
            i = j - 1
        else :
            if flag :
                new_s = new_s + int(cnt)*s[i]
                flag = False
            else :
                new_s = new_s + s[i]
        i = i + 1
    return new_s

mot = '3aba4c2a'

print(decompresser(mot))

            
                








    

    