def solve(a: list[int]) -> int:
    max_val = max(a)
        
    return a.count(max_val)

for t in range(int(input())):
    n = int(input())
    a = [int(_) for _ in input().split()]
    print(solve(a))