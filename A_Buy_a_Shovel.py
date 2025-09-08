def solve(k, r):
    _mod = k % 10
    multiplier = 1
    while (multiplier*_mod)%10 != 0 and (multiplier * _mod) % 10 != r:
        multiplier += 1
    
    print(multiplier)

if __name__ == "__main__":
    k, r = (int(_) for _ in input().split())
    solve(k, r)