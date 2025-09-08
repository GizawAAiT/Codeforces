def solve(a, b, c):
    if a + b == c:
        return '+'
    
    return '-'

if __name__ == '__main__':
    for t in range(int(input())):
        a, b, c = (int(_) for _ in input().split())
        print(solve(a, b, c))