def solve(n):
    _min = n//2 + 1
    _max = n-1
    return max(0, _max - _min + 1)

for t in range(int(input())):
    n = int(input())
    print(solve(n))