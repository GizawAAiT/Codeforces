def solve(n):
    return n//4 if n%4==0 else n//4 + 1

for t in range(int(input())):
    n = int(input())
    print(solve(n))