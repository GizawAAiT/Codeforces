def solve(arr: list[int]) -> int:
     
    #  Inefficient solution: O(n^2)
    
    #  # Compute the prefix sum array in place
    # for i in range(1, len(arr)):
    #     darr[i] += arr[i - 1]
    
    # # add zero to the beginning of the prefix sum array
    # arr.insert(0, 0)
    
    # max_average = float('-inf')
    # for i in range(len(arr)):
    #     for j in range(i + 1, len(arr)):
    #         average = (arr[j] - arr[i]) / (j - i)
    #         max_average = max(max_average, average)
    
    # return int(max_average                                                       )
    
    # Efficient solution: O(n)
    max_average = float('-inf')
    for num in arr:
        max_average = max(max_average, num)
        
    return max_average

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        result = solve(arr)
        print(result)