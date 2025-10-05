from collections import defaultdict
def solve(keys: str, word: str):
    _ord = defaultdict(int)
    for idx, k in enumerate(keys):
        _ord[k] = idx
    
    total = 0
    for i in range(1, len(word)):
        total += abs(_ord[word[i]] - _ord[word[i-1]])
        
    print(total)

for t in range(int(input())):
    keys = input().strip()
    word = input().strip()
    solve(keys, word)