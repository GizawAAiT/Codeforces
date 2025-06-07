def solve(_2n):
    seen = set()
    result = []
    for ch in _2n:
        if ch not in seen: result.append(ch)
        seen.add(ch)

    return result

for t in range(int(input())):
    n = int(input())
    _2n = input().split()
    print(*solve(_2n))