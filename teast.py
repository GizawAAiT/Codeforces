import time

def clean_time_bruteforce_explicit(
    n, m, row_robot, col_robot, row_dirt, col_dirt):
    """Simulates the robot cleaner step-by-step, and for each position,"""
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
        
# Example usage
n, m = 3, 3
row_robot, col_robot = 1, 1
row_dirt, col_dirt = 2, 2
start_time = time.time()
result = clean_time_bruteforce_explicit(n, m, row_robot, col_robot, row_dirt, col_dirt)
end_time = time.time()
print(f"Time taken: {end_time - start_time:.6f} seconds")

