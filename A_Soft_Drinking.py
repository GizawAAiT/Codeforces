def solve(n, k, l, c, d, p, nl, np):
    drink_unit = k*l//nl
    slice_unit = c*d
    salt_unit = p//np
    
    return min(drink_unit, slice_unit, salt_unit) //n

n, k, l, c, d, p, nl, np = (int(_) for _ in input().split())
print(solve(n, k, l, c, d, p, nl, np))