def solve(a, b):
    _mod = a%b
    return _mod if _mod == 0 else b-_mod

if __name__ =='__main__':
    for t in range(int(input())):
        a, b = (int(_) for _ in input().split())
        print(solve(a, b))