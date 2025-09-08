def solve(a, b):
    # assume a is always greater or equal to b:
    a, b = max(a, b), min(a, b)
    
    return [b, max((a-b)//2, 0)]

if __name__ == '__main__':
    a, b = (int(_) for _ in input().split())
    
    print(*solve(a, b))