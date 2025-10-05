def solve(number: str):
    _min = number[0]
    for num in number:
        _min = min(num, _min)
        
    return _min

for t in range(int(input())):
    number = input().strip()
    print(solve(number))