def number_of_rounds(a: int, b: int, c: int) -> int:
    
    """
    Each round, the lowest will raise by 1, and the highest will decrease by 1.
    The moment at least 2 of them are equal, the process ends and the number 
    of rounds taken is returned.
    
    Approach:
    - calculate three distances (a to b, a to c, b to c).
    - return the minimum of the three distances.
    """
        
    distances = [abs(a-b), abs(a-c), abs(b-c)]
    return min(distances)

if __name__ == '__main__':
    for t in range(int(input())):
        a, b, c = map(int, input().split())
        print(number_of_rounds(a, b, c))