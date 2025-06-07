from collections import defaultdict

def default_val():
    return float('inf')

for _ in range(int(input())): # t test cases
    
    _min = defaultdict(default_val)

    for _ in range(int(input())): # n

        val, code = input().split(" ")
        _min[code] = min(_min[code], int(val))
    
    res = min (_min["11"], _min["10"] + _min["01"])
    print(res if res != float('inf') else -1)



