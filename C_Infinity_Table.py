from math import sqrt

def find_row_col(k: int) -> tuple[int, int]:
    base_round = int(sqrt(k-1))
    remainder = k - base_round ** 2
    
    if remainder <= base_round+1:
        return remainder, base_round+1
    
    return base_round+1, 2*base_round+2-remainder

if __name__ == "__main__":
    for t in range(int(input())):
        k = int(input())
        row, col = find_row_col(k)
        print(row, col)