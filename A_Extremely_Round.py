def solve(num: str) -> int:
    
    length, first_dig = len(num), int(num[0])
    
    return first_dig + (length - 1) * 9

for t in range(int(input())):
    num = input().strip()
    print(solve(num))  