import heapq

def solve(n: int, a: list[int]) -> int:
    min_heap = []
    
    ans = 0    
    for idx in range(n-1, -1, -1):
        elem = a[idx]
        while min_heap and min_heap[0] < elem:
            ans += 1
            heapq.heappop(min_heap)
        heapq.heappush(min_heap, elem)
    
    return ans
        
for t in range(int(input())):
    n = int(input())
    a = [int(_) for _ in input().split()]
    print(solve(n, a))