def stabilized_matrix(n: int, m: int, a: list[list[int]]) -> list[list[int]]:
    
    for i in range(n):
        for j in range(m):
            left = a[i][j-1] if j > 0 else float('-inf')
            right = a[i][j+1] if j < m - 1 else float('-inf')
            top = a[i-1][j] if i > 0 else float('-inf')
            bottom = a[i+1][j] if i < n - 1 else float('-inf')
            
            a[i][j] = min(a[i][j], max(left, right, top, bottom))
            
    return a

if __name__ == '__main__':
    for t in range(int(input())):
        n, m = map(int, input().split())
        a = []
        for _ in range(n):
            a.append([int(_) for _ in input().split()])
    
        stabilized = stabilized_matrix(n, m, a)
        
        for row in stabilized:
            print(*row)