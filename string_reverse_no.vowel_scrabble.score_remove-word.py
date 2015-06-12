def reverse(text):
    y = len(text)
    rev = ""
    while y > 0:
        rev += text[y-1] 
        y -=1
    return (rev)

def anti_vowel(text):
    no_vowel = ""
    for letter in text:
        if letter not in "aeiouAEIOU":
            no_vowel += letter
    return (no_vowel)

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
         
def scrabble_score(word):
    word_lower = word.lower()
    total = 0
    for i in word_lower:
        for j in score:
            if i == j:
                total += score[j]
    return(total)


def censor(text, word):
    new_text = text.split()
    for i in range(0,len(new_text)):
        if new_text[i] == word:
            new_text[i] ='*'* len(word)
    return " ".join(new_text)
