def solve(n, gifts):
    received = [0 for _ in range(n)]
    for _ in range(n):
        idx = gifts[_]-1
        received[idx] = _+1
        
    print(*received)

n = int(input())
gifts = [int(_) for _ in input().split()]
solve(n, gifts)