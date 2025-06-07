def solve(arr, n):
    _min = float('inf')
    for idx in range(1, n):
        _min = min(_min, max(arr[idx], arr[idx-1]))

    return _min - 1

for t in range(int(input())):
    n = int(input())

    print(solve([int(_) for _ in input().strip().split()], n))