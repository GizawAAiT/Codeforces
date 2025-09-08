def solve(inp):
    if inp == '{}': return 0
    inp = inp.strip('{}')
    characters = inp.split(', ')
    return len(set(characters))

inp = input()

print(solve(inp))