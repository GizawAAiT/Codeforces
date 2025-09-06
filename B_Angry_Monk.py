import sys

def solve_opt():
    it = iter(sys.stdin.buffer.read().split())
    t = int(next(it))
    out = []
    for _ in range(t):
        n = int(next(it)); k = int(next(it))
        max_a = 0
        for i in range(k):
            v = int(next(it))
            if v > max_a:
                max_a = v
        # Minimal operations: 2*(n - max_a) - (k - 1)
        ans = 2 * (n - max_a) - (k - 1)
        out.append(str(ans))
    print("\n".join(out))

if __name__ == "__main__":
    solve_opt()
