def solve(n: int, a: list[int]) -> int:
    # : sort the array a:
    a.sort()
    
    # median index (median_idx): ceil devision
    median_idx = (n+1)//2 - 1
    
    # median elem:
    median_elem = a[median_idx]
    
    cnt = 0
    while median_idx < n and a[median_idx] == median_elem:
        cnt += 1
        median_idx += 1
    
    return cnt

for t in range(int(input())):
    n = int(input())
    a = [int(_) for _ in input().split()]
    print(solve(n, a))