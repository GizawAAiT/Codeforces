def solve(a: list[int], n: int):
    res = a[-1]
    
    cur = a[-1]
    for idx in range(-2, -n-1, -1):
        cur = min(a[idx], cur-1)
        
        if cur <= 0: break
        
        res += cur
    
    return res
def chocolates_quadratic(a):
    n = len(a)
    best = 0

    for last in range(n):                       # O(n)
        cur = a[last]
        total = cur
        for j in range(last - 1, -1, -1):       # O(n) per last
            cur = min(a[j], cur - 1)
            if cur <= 0:
                break
            total += cur
        best = max(best, total)
    return best


n = int(input())
a = [int(_) for _ in input().split()]
print(chocolates_quadratic(a))
        