def solve(moves):
    left_most, right_most = moves[0], moves[0]
    for move in moves[1:]:
        if move < left_most-1 or move > right_most+1:
            return "NO"
        
        left_most = min(move, left_most)
        right_most = max(move, right_most)
    
    return "YES"

for t in range(int(input())):
    n = int(input())
    moves = [int(_) for _ in input().split()]
    
    print(solve(moves))