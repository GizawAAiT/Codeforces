def solve(a: list[int]) -> int:
    cnt = {}
    _max_frequency = 0
    for num in a:
        cnt[num] = cnt.get(num, 0) + 1
        _max_frequency = max(_max_frequency, cnt[num])
    
    return _max_frequency

for t in range(int(input())):
    n = int(input())
    a = [int(_) for _ in input().split()]
    print(solve(a))