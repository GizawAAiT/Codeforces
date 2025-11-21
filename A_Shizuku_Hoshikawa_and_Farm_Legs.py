def solve(n: int)-> int:
    if n % 2 == 0:
        return n //4 + 1
    
    return 0

for t in range(int(input())):
    n = int(input())
    print(solve(n))