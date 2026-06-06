def find_LR_bounds(n: int) -> tuple[int, int]:
    l, r = -n+1, n
    return l, r

if __name__ == "__main__":
    for t in range(int(input())):
        n = int(input())
        l, r = find_LR_bounds(n)
        print(l, r)