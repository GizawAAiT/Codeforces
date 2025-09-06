import sys
def max_product_after_increment(digits):
    """Return the maximal product after adding 1 to exactly one array element."""
    mn = min(digits)
    used = False
    p = 1
    for v in digits:
        if not used and v == mn:
            p *= v + 1
            used = True
        else:
            p *= v
    return p


if __name__ == "__main__":
    data = list(map(int, sys.stdin.buffer.read().split()))
    t, *vals = data
    idx = 0
    out = []
    for _ in range(t):
        n = vals[idx]; idx += 1
        arr = vals[idx:idx + n]; idx += n
        out.append(str(max_product_after_increment(arr)))
    sys.stdout.write("\n".join(out))
