from collections import Counter
def solve(coins: list[int]) -> int:
    """
    coins represented by integers (their value).
    returns:
        int: maximum number of pocket needed to distribute coins so that no 
        two coins of same value ended up in the same pocket.
    """
    
    # count num of coins of each value:
    _count = Counter(coins)
    
    # return the max num of coins of same value:
    return max(_count.values())

if __name__ == "__main__":
    n = input()  # am not gonna use it!
    coins = list(map(int, input().split()))
    print(solve(coins))