def solve(n, tasks):
    tackled = set()
    tackled.add(tasks[0])
    
    for idx in range(1, n):
        if tasks[idx] in tackled and tasks[idx-1] != tasks[idx]:
            return 'NO'
        
        tackled.add(tasks[idx])
    
    return 'YES'

for t in range(int(input())):
    n = int(input())
    tasks = input()
    
    print(solve(n, tasks))