def better_s(s):
    s_new = ''
    for val in s :
        if val.isdigit():
            s_new = s_new + val
    return s_new

def find_winner(s):
    new_s = better_s(s)
    i = 0
    winner = 0
    while i < len(new_s) :
        current = int(new_s[i])
        if current > winner :
            winner = current
            pos = i + 1
        i = i + 1
    return pos

#print(find_winner('4 2 1 3 1'))



def check_syntax(s):
    if len(s) == 0 :
        return False
    if s[0] != '_' and not s[0].isalpha():
        return False
    for val in s :
        if not val.isalnum and val != '_':
            return False
    return True


def premier(n):
    x = 2
    nombre_premier_trouve = 0
    while True :
        cnt = 0
        for i in range(1, x+1):
            if x%i == 0:
                cnt = cnt + 1
        if cnt == 2 :
            nombre_premier_trouve = nombre_premier_trouve + 1
        if n == nombre_premier_trouve :
            return x
        x = x + 1


def word_verlan(word):
    res = ''
    i = 0
    while i < len(word) :
        res = res + word[len(word)-i-1]
        i = i + 1
    return res

def sentence_verlan(sentence):
    current_word = ''
    new_sentence = ''
    i = 0
    for char in sentence :   
        if char == ' ':
            current_word = word_verlan(current_word)
            new_sentence = new_sentence + current_word + " "
            current_word = ""
        else :
            current_word = current_word + char
        if i == len(sentence) - 1:
            current_word = word_verlan(current_word)
            new_sentence = new_sentence + current_word 
        i = i + 1
    return new_sentence

def double_ite(s):
    i = 0
    res = ""
    while i < len(s):
        if s[i].isalpha() and s[i].lower() != 'l' :
            res = res + 2*s[i]
        else :
            res = res + s[i]
        i = i + 1
    return res

def double_rec(s):
    if len(s) == 0 :
        return ''
    else :
        if s[0].isalpha() and s[0].lower() != 'l':
            return 2*s[0] + double_rec(s[1:])
        else :
            return s[0] + double_rec(s[1:])


def rech_dic_rec(x, a,b, cnt=0):
    mid = (a + b)//2
    if mid == x :
        return cnt + 1
    elif x > mid :
        a = mid + 1
    else :
        b = mid -1
    return rech_dic_rec(x, a, b, cnt + 1)
    
def rech_dic_ite(x, a, b, cnt=0):
    mid = (a + b)//2
    while mid != x:
        if x > mid :
            a = mid + 1
        else :
            b = mid - 1
        cnt = cnt + 1
        mid = (a + b)//2
    return cnt + 1


        
        
    





                









    


        
    
        
    


    
    

            




        


        