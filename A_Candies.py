def min_x_brutal(n: int) -> int:
    y = 1
    while True:
        if n % y == 0:
            q = n // y + 1
            if q & (q - 1) == 0 and q != 2:    # q=2 → k=1, not allowed
                return y
        y += 1

for ti in range(int(input())):
    n = int(input())
    print(min_x_brutal(n))