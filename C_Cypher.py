def move_up(a, idx):
    if a[idx] == 9:
        a[idx] = 0
    else:
        a[idx] += 1

def move_down(a, idx):
    if a[idx] == 0:
        a[idx] = 9
    else:
        a[idx] -= 1

def solve(a, moves):
    for idx, move in enumerate(moves):
        for m in move:
            if m == 'D':
                move_up(a, idx)
            else:
                move_down(a, idx)
    
    return a

for t in range(int(input())):
    moves = []
    n = int(input())
    a = [int(_) for _ in input().split()]
    for _ in range(n):
        _, move = input().split()
        moves.append(move)
    
    print(*solve(a, moves))