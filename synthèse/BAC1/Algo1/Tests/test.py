def word_verlan(word):
    reverse_word = ''
    i = 0
    while i < len(word):
        reverse_word = reverse_word + word[len(word)-1-i]
        i = i + 1
    return reverse_word

def sentence_verlan(sentence):
    new_sentence = ''
    current_word = ''
    i = 0
    while i < len(sentence):
        if sentence[i] == ' ' :
            current_word = word_verlan(current_word)
            new_sentence = new_sentence + current_word + ' '
            current_word = ''
        else :
            current_word = current_word + sentence[i]
        if i == len(sentence) - 1 :
            current_word = word_verlan(current_word)
            new_sentence = new_sentence + current_word
        i = i + 1
    return new_sentence

print(sentence_verlan('Je suis ton père !'))