def solve(n: int, a: list[int]) -> float:
    _max, total = float('-inf'), 0
    for num in a:
        _max = max(_max, num)
        total += num
    
    return round(_max + (total - _max)/(n-1), 7)

for t in range(int(input())):
    n = int(input())
    a = [int(_) for _ in input().split()]
    print(solve(n, a))