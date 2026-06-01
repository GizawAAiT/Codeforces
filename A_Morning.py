def solve(code):
    key_board = '1234567890'
    curr, actions = 0, 0
    for _ in range(4):
        pos = key_board.index(code[_])
        actions += abs(curr - pos) + 1
        curr = pos
    
    return actions

for t in range(int(input())):
    code = input()
    print(solve(code))