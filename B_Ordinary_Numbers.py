
def ordinary_count_bruteforce(n: int) -> int:
    def is_ordinary(x: int) -> bool:
        s = str(x)
        return len(set(s)) == 1

    return sum(1 for x in range(1, n + 1) if is_ordinary(x))

# def ordinary_count_math(n: int) -> int:
#     s = str(n)
#     len_n = len(s)

#     # 1) all ordinary numbers with fewer digits
#     ans = 9 * (len_n - 1)

#     # 2) numbers with exactly len_n digits
#     base = int('1' * len_n)          # 11..1 (len_n copies)
#     for d in range(1, 10):
#         if d * base <= n:
#             ans += 1
#     return ans
def count_ordinary_numbers(n):
    count = 0
    for length in range(1, 10):
        for digit in range(1, 10):
            num = int(str(digit) * length)
            if num <= n:
                count += 1
            else:
                break
    return count

t = int(input())
for _ in range(t):
    n = int(input())
    print(count_ordinary_numbers(n))


# for t in range(int(input())):
#     print(ordinary_count_bruteforce(n=int(input())))