# def max_sushi_bruteforce(t):
#     n = len(t)
#     best = 0
#     for mid in range(n - 1):
#         if t[mid] == t[mid + 1]:
#             continue                      # halves must differ
#         l = mid
#         r = mid + 1
#         left_val, right_val = t[l], t[r]
#         while l >= 0 and r < n and t[l] == left_val and t[r] == right_val:
#             length = r - l + 1
#             best = max(best, length)
#             l -= 1
#             r += 1
#     return best

# opt:
# def max_sushi_linear(t):
#     n = len(t)
#     # 1) collect run lengths
#     runs = []
#     cur = 1
#     for i in range(1, n):
#         if t[i] == t[i - 1]:
#             cur += 1
#         else:
#             runs.append(cur)
#             cur = 1
#     runs.append(cur)

#     # 2) scan adjacent pairs
#     best = 0
#     for i in range(len(runs) - 1):
#         best = max(best, 2 * min(runs[i], runs[i + 1]))
#     return best

# No space 
def max_sushi_no_extra_space(t):
    n = len(t)
    best = 0
    prev_len = 0
    cur_len = 1

    for i in range(1, n):
        if t[i] == t[i - 1]:
            cur_len += 1
        else:
            best = max(best, 2 * min(prev_len, cur_len))
            prev_len = cur_len
            cur_len = 1

    best = max(best, 2 * min(prev_len, cur_len))
    return best



n = int(input())
t = [int(_) for _ in input().split()]
print(max_sushi_no_extra_space(t))