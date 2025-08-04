def max_theorems_naive(a, t, k):
    
    n = len(a)

    # Calculate the total production without any boost
    total_production = sum(a[cycle] for cycle in range(n) if t[cycle])

    # If all machines are already operational, no need for boost
    if t.count(0) == 0:
        return total_production

    best_production = total_production

    # Calculate the additional production gained by applying the boost at each possible starting position
    for start_pos in range(n - k + 1):
        additional_production = 0
        for cycle in range(start_pos, start_pos + k):
            if not t[cycle]:
                additional_production += a[cycle]
        current_production = total_production + additional_production
        best_production = max(best_production, current_production)

    return best_production


n, k = (int(_) for _ in input().split())
a =  [int(_) for _ in input().split()]
t =  [int(_) for _ in input().split()]
print(max_theorems_naive(a, t, k))