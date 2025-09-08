def solve(a, b):
    _map = {1:'1/1', 2:'5/6', 3:'2/3', 4:'1/2', 5:'1/3', 6:'1/6'}
    
    return _map[max(a, b)]

if __name__ == '__main__':
    a, b = (int(_) for _ in input().split())
    print(solve(a, b))