from math import gcd

def minimum_number_of_steps_to_brew_potion(k: int) -> int:
    """
    The potion should contain k% magic essence, and (100-k)% water.
    
    Solution Idea:
     - Find gcd of k and 100-k.
     - Devide k, and 100-k by the gcd.
     - Return the sum of the two numbers found in the previous step.
    """
    
    _g = gcd (k, 100-k)
    return k//_g + (100-k)//_g

if __name__ == "__main__":  
    for t in range(int(input())):
        k = int(input())
        print(minimum_number_of_steps_to_brew_potion(k))