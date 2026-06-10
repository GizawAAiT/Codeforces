import heapq

def minimum_number_of_month_when_Patya_has_to_water_flowers(
    k: int, growth_at_month: list[int]) -> int:
    
    if sum(growth_at_month) < k: return -1
    
    watering_months, total = [], 0
    for growth in growth_at_month:
        heapq.heappush(watering_months, growth)
        total += growth
        
        # : heappop as far as the total is greater than or equal to k:
        while watering_months and total - watering_months[0] >= k:
            total -= heapq.heappop(watering_months)
        
    return len(watering_months)

if __name__ == '__main__':
    k = int(input())
    growth_at_month = [int(_) for _ in input().split()]
    print(minimum_number_of_month_when_Patya_has_to_water_flowers(
        k = k, growth_at_month = growth_at_month))