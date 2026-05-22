def solve(monsters: list[int]) -> int:
    # Count ones in the mosters:
    ones = sum(x for x in monsters if x == 1)
    
    return len(monsters) - ones//2

if __name__ == "__main__":
    
    for t in range(int(input())):
        n = int(input())
        monsters = [int(_) for _ in input().strip().split()]
        print(solve(monsters))