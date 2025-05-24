def solve(arr, n):
    run_sum = _max = 1
    for idx in range(1, n):
        if arr[idx] > arr[idx-1]:
            run_sum += 1
        else:
            run_sum = 1
        
        _max = max(_max, run_sum)
    
    return _max

n = int(input())
arr = [int(__) for __ in input().strip().split(" ")]
print(solve(arr, n))