t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    n = 2 * abs(a - b)  # total people in the circle

    # invalid if c or a or b > n, or if a and b can't exist in same circle
    if a > n or b > n or c > n or a == b:
        print(-1)
        continue

    half = n // 2
    # find the opposite person of c
    if c + half <= n:
        print(c + half)
    else:
        print(c - half)
