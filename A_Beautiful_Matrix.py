def solve_matrix(matrix):
    for idx in range(5):
        for jdx in range(5):
            if matrix[idx][jdx] == 1:
                return abs(jdx-2) + abs(idx-2)

matrix = []
for _ in range(5):
    matrix.append([int(_) for _ in input().strip().split()])

print(solve_matrix(matrix))