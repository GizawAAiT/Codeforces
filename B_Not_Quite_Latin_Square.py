def solve(matrix):
    _set = set(["A", 'B', 'C'])
    for row in matrix:
        if '?' in row:
            for chr in row:
                if chr in _set:
                    _set.remove(chr)
            
            print(*_set)
            return
    
for t in range(int(input())):
    matrix = []
    for _ in range(3):
        matrix.append(input())
    
    solve(matrix)