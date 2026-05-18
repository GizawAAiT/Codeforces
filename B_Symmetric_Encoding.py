def solve(n: int, s: str) -> str:
    
    sorted_unique_characters = sorted(list(set(s)))
    
    map_table = {} # swap table (mapping)
    for idx, char in enumerate(sorted_unique_characters):
        map_table[char] = sorted_unique_characters[-idx - 1]
    
    ans = ""
    for char in s:
        ans += map_table[char]
        
    return ans

for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    print(solve(n, s))