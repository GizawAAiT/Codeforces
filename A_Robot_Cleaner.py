# def solve(n, m, row_robot, col_robot, row_dirt, col_dirt):
    
#     row_move, col_move = 0, 0
    
#     if row_dirt >= row_robot:
#         row_move += row_dirt - row_robot
#     else:
#         row_move += 2*n - row_robot - row_dirt
        
#     if col_dirt >= col_robot:
#         col_move += col_dirt - col_robot
#     else:
#         col_move += 2*m - col_robot - col_dirt
   
# def clean_time_bruteforce(n, m, rb, cb, rd, cd):
#     """
#     Simulate reflections step-by-step until robot's row==rd or col==cd.
#     Time complexity: O(lcm(2(n-1), 2(m-1)))  (<= ~4e4 for n,m<=100)
#     Space complexity: O(1)
#     """
#     dr, dc = 1, 1
#     t = 0
#     # check at time 0
#     if rb == rd or cb == cd:
#         return 0

#     while True:
#         # reflect if next step would hit a wall
#         if rb + dr < 1 or rb + dr > n:
#             dr = -dr
#         if cb + dc < 1 or cb + dc > m:
#             dc = -dc

#         # move one second
#         rb += dr
#         cb += dc
#         t += 1

#         # clean check at this time
#         if rb == rd or cb == cd:
#             return t
    
#     return min(row_move, col_move)
def clean_time_bruteforce_explicit(
    n, m, row_robot, col_robot, row_dirt, col_dirt):
    """
    Simulates the robot cleaner step-by-step, and for each position,
    explicitly checks all cells in the current row and column.
    Returns the first time when the dirty cell (row_dirt, col_dirt) is cleaned.

    Time complexity: O((n + m) * lcm(2(n-1), 2(m-1))) <= ~2e6 max
    Space complexity: O(1)
    """
    dr, dc = 1, 1
    t = 0

    while True:
        # check current row
        for c in range(1, m + 1):
            if (row_robot, c) == (row_dirt, col_dirt):
                return t

        # check current column
        for r in range(1, n + 1):
            if (r, col_robot) == (row_dirt, col_dirt):
                return t

        # reflect if about to hit a wall
        if row_robot + dr < 1 or row_robot + dr > n:
            dr *= -1
        if col_robot + dc < 1 or col_robot + dc > m:
            dc *= -1

        # move
        row_robot += dr
        col_robot += dc
        t += 1

for t in range(int(input())):
    n, m, row_robot, col_robot, row_dirt, col_dirt = (
        int(_) for _ in input().split()
    )
    
    print(clean_time_bruteforce_explicit(
        n, m, row_robot, col_robot, row_dirt, col_dirt))