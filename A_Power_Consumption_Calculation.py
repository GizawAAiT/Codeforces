def total_power_consumption(
    n: int, p1: int, p2: int, p3: int, T1: int, T2: int, 
    intervals: list[tuple[int, int]]) -> int:
    total = (intervals[0][1] - intervals[0][0]) * p1
    
    for idx in range(1, n):
        i1, j1 = intervals[idx - 1]
        i2, j2 = intervals[idx]
        
        rng = i2 - j1
        
        # Normal time:
        total += min(rng, T1) * p1
        rng -= min(rng, T1)
        
        # Screensaver time:
        total += min(rng, T2) * p2
        rng -= min(rng, T2)
        
        # Sleep time:
        total += rng * p3
        
        # The current work range power:
        total += (j2 - i2) * p1
    
    return total

if __name__ == "__main__":
    n, p1, p2, p3, T1, T2 = map(int, input().split())
    intervals = []
    for _ in range(n):
        i, j = map(int, input().split())
        intervals.append((i, j))
    
    print(total_power_consumption(n, p1, p2, p3, T1, T2, intervals))