def can_move_numbers_and_maintain_threshold(n: int, nums: list[int]) -> str:
   
    # edge case:
    if n < 2 or n % 2 != 0:
        return 'NO'
    
    _min_odd_place = float('inf')
    _max_even_place = float('-inf')
    
    for idx in range(n):
        if idx % 2 == 0: # Odd
            _min_odd_place = min(_min_odd_place, nums[idx])
        else: # Even
            _max_even_place = max(_max_even_place, nums[idx])
    
    return 'YES' if _min_odd_place > _max_even_place + 1 else 'NO'

if __name__ == '__main__':
    for t in range(int(input())):
        n = int(input())
        nums = [int(_) for _ in input().split()]
        print(can_move_numbers_and_maintain_threshold(n, nums))