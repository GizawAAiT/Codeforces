def symetric(a: int, n: int):
    return n%2 == a%2

def solve(n: int, a: int, b: int) -> int:
    # :check blue symetry (b):
    if not symetric(b, n):
        return 'NO'
    
    # : If Red(a) either not symetry nor inclusive by Blue(b), return 'NO'
    if not symetric(a, n) and a > b:
        return 'NO'
    
    return 'YES'd

for t in range(int(input())):
    n, a, b = map(int, input().split())
    print(solve(n, a, b))