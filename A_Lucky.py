def solve(_hex):
    first_half = second_half = 0
    
    # first half:
    for idx in range(3):
        first_half += int(_hex[idx])
    
    # second half:
    for idx in range(3, 6):
        second_half += int(_hex[idx])
    
    if first_half == second_half: return 'YES'
    
    return 'NO'

if __name__ == '__main__':
    for t in range(int(input())):
        _hex = input().strip()
        print(solve(_hex))