def solve(s: str) -> str:
    """
    Approach:
     - if I get 2 distinct characters/Letters in the first half of the 
     pallendrom (excluding the center one), then its possible
    """
    
    for idx in range(len(s)//2):
        if s[idx] != s[0]: return 'YES'
        
    return 'NO'

for t in range(int(input())):
    s = input()
    print(solve(s))