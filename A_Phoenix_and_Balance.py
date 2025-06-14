def solve(n):
    return 2**(n//2 + 1) - 2

for t in range(int(input())):
    print(solve(
        n = int(input())
    ))