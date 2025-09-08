def solve(n, magnets):
    groups = 1
    for idx in range(1, n):
        groups += magnets[idx] != magnets[idx-1]
    
    print(groups)

n = int(input())
magnets = []
for _ in range(n):
    magnet = input().strip()
    magnets.append(magnet)
    
solve(n, magnets)