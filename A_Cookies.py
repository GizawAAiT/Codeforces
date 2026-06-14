def number_of_ways_to_take_bag_of_cookies(a: list[int]) -> int:
    num_of_evens = num_of_odds = 0
    for num in a:
        num_of_evens += (num+1) % 2
        num_of_odds += num % 2
    
    return num_of_evens if num_of_odds % 2 == 0 else num_of_odds

n = input()
print(number_of_ways_to_take_bag_of_cookies([int(_) for _ in input().split()]))