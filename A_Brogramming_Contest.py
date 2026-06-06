def min_number_of_moves(n: int, s: str) -> int:
    
    moves, match = 0, '0'
    for c in s:
        if c != match:
            moves += 1
            match = c
    
    return moves

if __name__ == "__main__":
    for t in range(int(input())):
        n = int(input())
        s = input()
        print(min_number_of_moves(n, s))