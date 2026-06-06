def max_number_of_coins_after_transformation(n: int) -> int:
    """
    In one operation, change a coin with value n to two coins with values 
    floor(n/4).
    """
    num_of_coins = 1
    while n > 3:
        n //= 4
        num_of_coins *= 2
    
    return num_of_coins

if __name__ == "__main__":
    for t in range(int(input())):
        n = int(input())
        print(max_number_of_coins_after_transformation(n))
        
"""
Time complexity: O(log(n, 4))"""