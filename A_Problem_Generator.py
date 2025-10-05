from collections import defaultdict

def solve(n: int, rounds: int, difficulty: str):
    _freq = defaultdict(int)
    
    # Update the map:
    for d in difficulty:
        _freq[d] += 1
    
    additional, levels = 0, 'ABCDEFG'
    for l in levels:
        additional += max(rounds-_freq[l], 0)
    
    print(additional)

for t in range(int(input())):
    n, rounds = (int(_) for _ in input().split())
    difficulty = input()
    solve(n, rounds, difficulty)