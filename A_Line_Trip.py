def solve(x, stations):
    stations.insert(0, 0)
    stations.append(x + (x-stations[-1]))
    
    return max(stations[i]- stations[i-1] for i in range(1, len(stations)))

for _ in range(int(input())):
    n, x = (int(_) for _ in input().split())
    stations = [int(_) for _ in input().split()]
    print(solve(x, stations))