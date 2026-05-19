def solve(directions: str) -> int:
    """
    Directions are either L or R. Some directions might be ignored.
    returns:
        int: number of possible destinations considered some (possibly zero)
        directions ignored.
    """
    
    # count Ls and Rs:
    count_L = directions.count('L')
    count_R = directions.count('R')
    
    return count_L + count_R + 1

if __name__ == "__main__":
    n = input()  # not used
    directions = input()
    print(solve(directions))