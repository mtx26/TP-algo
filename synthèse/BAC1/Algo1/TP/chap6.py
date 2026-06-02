def word_3_double():
    with open('words.txt') as file :
        for line in file :
            word = line.strip()
            i = 0
            while i < len(word) - 6:
                current = word[i]
                if word[i] == word[i +1] :
                    if word[i +2] == word[i+3] :
                        if word[i+4] == word[i+5] :
                            return word
                i = i + 1

print(word_3_double())
                    
                
                
        