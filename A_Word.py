from typing import List
def solve(word: str):
    word = list(word)
    upper, lower = 0, 0
    for chr in word:
        if chr.islower():
            lower += 1
        else: upper += 1
    
    if upper > lower:
        for i in range(len(word)):
            word[i] = word[i].upper()
    else:
        for i in range(len(word)):
            word[i] = word[i].lower()
    
    return ''.join(word)

word = input().strip()
print(solve(word))


        