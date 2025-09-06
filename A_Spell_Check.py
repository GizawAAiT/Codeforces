def solve(name):
    # print(sorted(name))
    if sorted(name) == sorted(['T', 'i', 'm', 'u', 'r']):
        return 'YES'
    
    return 'NO'

for t in range(int(input())):
    n = int(input())
    name = [char for char in input()]
    
    # print(f'name: {name}')
    print(solve(name))
    
    