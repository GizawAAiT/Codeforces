def solve(strings: list[str]):
    return len(set(strings[0] + strings[1])) - 1

for t in range(int(input())):
    strings = []
    for _ in range(2):
        strings.append(input())
    
    print(solve(strings))