def min_number_of_keyboards_stolen(n: int, a: list[int]) -> int:
    """
    Approach:
    - Find _min and _max in a. The minimum possible number of keyboards stonen 
    is the missing ones between _min and _max.
    """
    
    _min, _max = min(a), max(a)
    return _max - _min + 1 - n

if __name__ == "__main__":
    n = int(input())
    a = [int(_) for _ in input().split()]
    print(min_number_of_keyboards_stolen(n, a))