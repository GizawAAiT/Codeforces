def solve(n: int):
    if n%2: return 'Kosuke'
    
    return 'Sakurako'

for t in range(int(input())):
    n = int(input())
    print(solve(n))