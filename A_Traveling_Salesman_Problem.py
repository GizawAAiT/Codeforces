import sys

def min_moves_bruteforce(groups):
    # groups: dict with keys '+x','-x','+y','-y' mapping to lists of distances
    ans = 0
    for key in ['+x', '-x', '+y', '-y']:
        arr = groups[key]
        if arr:
            arr.sort()                   # brute-ish extra work
            ans += 2 * arr[-1]           # out-and-back to farthest
    return ans

if __name__ == "__main__":  # flip to True if you want this entrypoint
    it = iter(sys.stdin.buffer.read().split())
    t = int(next(it))
    out = []
    for _ in range(t):
        n = int(next(it))
        groups = {'+x': [], '-x': [], '+y': [], '-y': []}
        for _ in range(n):
            x = int(next(it)); y = int(next(it))
            if y == 0 and x > 0: groups['+x'].append(x)
            elif y == 0 and x < 0: groups['-x'].append(-x)
            elif x == 0 and y > 0: groups['+y'].append(y)
            elif x == 0 and y < 0: groups['-y'].append(-y)
            else:
                # Problem guarantees all points lie on axes; no-op otherwise.
                pass
        out.append(str(min_moves_bruteforce(groups)))
    print("\n".join(out))
