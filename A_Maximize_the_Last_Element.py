# # def cubic_max_last(a):
# #     n = len(a)
# #     INF_NEG = -10**9
# #     # dp[i][j] valid only for odd length (j - i) % 2 == 0
# #     dp = [[INF_NEG] * n for _ in range(n)]

# #     # length 1
# #     for i in range(n):
# #         dp[i][i] = a[i]

# #     # odd lengths 3,5,…
# #     for length in range(3, n + 1, 2):
# #         for i in range(0, n - length + 1):
# #             j = i + length - 1
# #             best = INF_NEG
# #             for k in range(i, j):          # delete (k, k+1)
# #                 left_i, left_j = i, k - 1
# #                 right_i, right_j = k + 2, j
# #                 if left_i > left_j:
# #                     cand = dp[right_i][right_j]
# #                 elif right_i > right_j:
# #                     cand = dp[left_i][left_j]
# #                 else:
# #                     cand = max(dp[left_i][left_j], dp[right_i][right_j])
# #                 best = max(best, cand)
# #             dp[i][j] = best
# #     return dp[0][n - 1]


# # # Driver for many test cases
# # import sys
# # it = iter(map(int, sys.stdin.buffer.read().split()))
# # t = next(it)
# # for _ in range(t):
# #     n = next(it)
# #     arr = [next(it) for _ in range(n)]
# #     print(cubic_max_last(arr))
# def calculate_max_stability(capacities):
#     n = len(capacities)
#     max_stability = 0
    
#     # Try all possible ways to remove pairs
#     def solve(arr):
#         if len(arr) == 1:
#             return arr[0]
        
#         max_val = 0
#         for i in range(len(arr) - 1):
#             # Remove pair at position i, i+1
#             new_arr = arr[:i] + arr[i+2:]
#             max_val = max(max_val, solve(new_arr))
        
#         return max_val
    
#     return solve(capacities)

# import sys
# it = iter(map(int, sys.stdin.buffer.read().split()))
# t = next(it)
# for _ in range(t):
#     n = next(it)
#     arr = [next(it) for _ in range(n)]
#     print(calculate_max_stability(arr))
def quadratic_max_last(a):
    n = len(a)
    # dp[i][j] only meaningful when (j - i) is even
    dp = [[0] * n for _ in range(n)]

    # length 1 intervals (j == i)
    for i in range(n):
        dp[i][i] = a[i]

    # process odd lengths 3,5,7,…  (step = 2)
    for length in range(3, n + 1, 2):
        for i in range(0, n - length + 1):
            j = i + length - 1
            dp[i][j] = max(dp[i + 2][j], dp[i][j - 2])

    return dp[0][n - 1]


# ---------- driver ----------
import sys
it = iter(map(int, sys.stdin.buffer.read().split()))
t = next(it)
for _ in range(t):
    n = next(it)
    arr = [next(it) for _ in range(n)]
    print(quadratic_max_last(arr))
