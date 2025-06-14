def solve(arr: list[int]):
    return len(set(arr))

for _ in range(int(input())):
    n = int(input())
    arr = [int(_) for _ in input().split()]
    print(solve(arr))