# def solve(n: int, k: int, arr: list[int], brr: list[int]):
#     sum_a, max_b, res = 0, 0, 0
    
#     for idx in range(min(n, k)):
#         sum_a += arr[idx]
#         max_b = max(max_b, brr[idx])
        
#         res = max(res, sum_a + (k-idx-1)*max_b)
    
#     return res
def max_xp_opt(n, K, a, b, ct, pt):
    limit   = min(n, K // ct)   # max unlockable modules
    sum_a   = 0
    max_b   = 0
    best    = 0

    for i in range(limit):          # prefix length p = i+1
        sum_a += a[i]
        max_b = max(max_b, b[i])
        rem   = K - (i + 1) * ct
        practices = rem // pt
        best = max(best, sum_a + practices * max_b)

    return best


for t in range(int(input())):
    n, k = (int(_) for _ in input().split())
    arr = [int(_) for _ in input().split()]
    brr = [int(_) for _ in input().split()]
    print(max_xp_opt(n, k, arr, brr, 1, 1))

                