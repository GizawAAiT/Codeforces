def solve(arr):
    _max, _min = max(arr), min(arr)
    return 2*(_max - _min)

for t in range(int(input())):
    n = int(input())
    arr = [int(_) for _ in input().split()]
    print(solve(arr))