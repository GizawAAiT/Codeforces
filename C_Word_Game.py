from collections import Counter

def solve(a_words: list[str], b_words: list[str], c_words: list[str]
        ) -> list[int]:
    
    res = [0, 0, 0]
    _dic_words = Counter(a_words + b_words + c_words)
    
    for word in a_words:
        res[0] += 3 if _dic_words[word] == 1 else 1 if _dic_words[word] == 2 else 0
    
    for word in b_words:
        res[1] += 3 if _dic_words[word] == 1 else 1 if _dic_words[word] == 2 else 0
    
    for word in c_words:
        res[2] += 3 if _dic_words[word] == 1 else 1 if _dic_words[word] == 2 else 0
    
    return res

for _ in range(int(input())):
    n = input()
    a_words = input().strip().split()
    b_words = input().strip().split()
    c_words = input().strip().split()
    print(*solve(a_words, b_words, c_words))