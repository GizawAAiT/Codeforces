def solve(name):
    start = 'a'
    
    total_distance = 0
    for chr in name:
        distance = abs(ord(start)-ord(chr))
        shortest = min(distance, 26-distance)
        # print(f'start:{start}, chr: {chr}, dist: {shortest}')
        total_distance += shortest
        start = chr
    
    print(total_distance
          )

name = input()
solve(name)