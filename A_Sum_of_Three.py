def can_be_represented_as_distinct_triplet_sum_of_non_3_multiple(
    n: int) -> str:
    
    """
    - (1) n should be greater than 6 and different from 9, otherwise can't be 
    represented by distinct triplet sum of non 3 multiples.
    - (2) if it passes condition(1) above, then it can be represented as either
    of the following two (a, and b) sequences
        - (a) [1, 2, 4], [1, 2, 5], [1, 2, 7], [1, 2, 8], ... keeping 1, 2
        - (b) [1, 4, 5], [1, 4, 7], [1, 4, 8], [1, 4, 10], [1, 4, 11]...
    
    Formula:
        if n-3 is not divisible by 3, sequence (a) fits. Otherwise, sequence 
        (b) should fit as far as condition 1 holds true
    """
    
    # Implementation:
    if n < 7 or n == 9: return False
    return [1, 2, n-3] if (n-3)%3 != 0 else [1, 4, n-5]

if __name__ == "__main__":
    for t in range(int(input())):
        n = int(input())
        ans = can_be_represented_as_distinct_triplet_sum_of_non_3_multiple(n)
        if not ans:
            print('NO')
        else:
            print('YES')
            print(*ans)