def solve(intervals: list[int], req):
    for idx in range(1, len(intervals)):
        start, end = intervals[idx-1][1], intervals[idx][0]
        if end-start >= req:
            return "YES"
    
    return "NO"

for t in range(int(input())):
    n, s, m = (int(_) for _ in input().split())
    intervals = [(0, 0)]
    for _ in range(n):
        l, r = (int(_) for _ in input().split())
        intervals.append((l, r))
    
    intervals.append((m, m))
    
    print(solve(
        intervals= intervals,
        req = s
    ))