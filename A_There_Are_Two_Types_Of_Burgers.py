def profit_slow(b, p, f, h, c):
    max_rev = 0
    buns_pairs = b // 2        # total burgers possible
    for x in range(0, min(p, buns_pairs) + 1):    # hamburgers
        remaining_pairs = buns_pairs - x
        y = min(f, remaining_pairs)               # chicken burgers
        rev = x * h + y * c
        max_rev = max(max_rev, rev)
    return max_rev
def profit(b, p, f, h, c):
    buns = b // 2          # burger slots

    # Ensure hamburger has >= price
    if h < c:              # swap labels so h ≥ c
        h, c = c, h
        p, f = f, p

    ham = min(p, buns)     # make pricier burger first
    buns -= ham
    chi = min(f, buns)

    return ham * h + chi * c

for t in range(int(input())):
    b, p, f = (int(_) for _ in input().split())
    h, c = (int(_) for _ in input().split())
    
    print(profit(b, p, f, h, c))