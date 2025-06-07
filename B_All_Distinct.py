def solve(arr, n):
    dup = n - len(set(arr))

    return n - dup if dup%2==0 else n - dup - 1

for _ in range(int(input())):
    n = int(input())
    arr = [int(_) for _ in input().split()]
    print(solve(arr, n))
