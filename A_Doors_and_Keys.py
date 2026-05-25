def solve(key_door: str)-> str:
    found_keys = set()
    for char in key_door:
        if char.islower():
            found_keys.add(char)
        
        elif char.lower() not in found_keys:
            return 'NO'
    
    return 'YES'

for t in range(int(input())):
    key_door = input().strip()
    print(solve(key_door))