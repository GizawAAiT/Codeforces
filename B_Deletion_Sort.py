def min_possible_number_of_element_left_after_deletion(
    n: int, arr: list[int]) -> int:
    '''
    Given an array of integers, at a time, we can remove any element if the 
    array is not non-descending. The moment it gets non-descending, we can no 
    longer remove any element. The target is to find the minimum possible 
    number of element left after any number of possible deletions.
    
    Approach:
      - If the array is sorted, we can not delete anything, so return the 
      length of the array(n)
      - otherwise, there must be a greater element found behind a smaller 
      element somewhere in the array and we can keep them and delete all 
      other elements. Then also we can remove one of the two. so, 
      the minimum possible number of element left after any number of possible 
      is 1.
      - So, while moving forward through the array, if we get a decreasing 
      pair, we can return 1. If we reach the end of the array without finding
      a decreasing pair, we can return n.
    Returns:
        The minimum possible number of element left after any number of 
        possible deletions.
    '''
    
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            return 1
    
    return n

if __name__ == "__main__":   
    for t in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        print(min_possible_number_of_element_left_after_deletion(n, arr))