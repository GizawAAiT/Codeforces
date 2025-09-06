def solve(calories: list[int], touches: str):
    energy = 0
    for idx in touches:
        idx = int(idx)-1
        
        energy += calories[idx]
        
    return energy

calories = [int(_) for _ in input().split()]
touches = input().strip()

print(solve(calories, touches))