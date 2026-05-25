def solve(a: list[int], b: list[int]) -> str:
    set_a = set(a)
    set_b = set(b)
    if len(set_a) > 2 or len(set_b) > 2 or (len(set_a) > 1 and len(set_b) > 1):
        return 'YES'
    
    return 'NO'

for t in range(int(input())):
    n = int(input())
    a = [int(_) for _ in input().split()]
    b = [int(_) for _ in input().split()]
    print(solve(a, b))