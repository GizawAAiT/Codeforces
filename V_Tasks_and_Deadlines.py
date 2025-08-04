def solve(intervals):
    intervals.sort(key=lambda x: x[0])   # sort by duration aᵢ
    t = 0
    reward = 0
    for a, d in intervals:
        t += a
        reward += d - t
    return reward
n = int(input())
intervals = []
for _ in range(n):
    t, d = (int(_) for _ in input().split())
    intervals.append((t, d))
print(solve(intervals))
    
    