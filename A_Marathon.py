def solve(_dist):
    res = 0
    for idx in range(1, 4):
        res += _dist[0] < _dist[idx]
        
    print(res)
    
if __name__ == "__main__":
    for t in range(int(input())):
        _dist = [int(_) for _ in input().split()]
        
        solve(_dist)