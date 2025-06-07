
from math import ceil
def pedestal(n):
    first = ceil(n/3)+1
    n -= first

    second = n//2 + 1
    third = n - second

    return [second, first, third]    

for t in range(int(input())):
    n = int(input())
    print(*pedestal(n)
)
