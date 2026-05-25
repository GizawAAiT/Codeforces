def solve(n: int, a: list[int]) -> int:
    time = 0
    max_cut = 0
    for idx in range(1, n-1):
        a1, a2, a3 = a[idx-1], a[idx], a[idx+1]
        
        # Update travel time:
        time += abs(a2-a1)
        
        if a2 > a1 and a2 > a3 or a2 < a1 and a2 < a3:
            max_cut = max(max_cut, 2*min(abs(a2-a1), abs(a2-a3)))
    
    # Update travel time from an-1 to an:
    time += abs(a[-1] - a[-2])
    
    # consider the first and last element removal for the impact on max_cut:
    max_cut = max(max_cut, abs(a[1] - a[0]), abs(a[-1] - a[-2]))
    
    return time - max_cut

for t in range(int(input())):
    n = int(input())
    a = [int(_) for _ in input().split()]
    print(solve(n, a))