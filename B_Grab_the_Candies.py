even_sum = lambda arr: sum(n for n in arr if not n%2)
odd_sum = lambda arr: sum(n for n in arr if n%2)

for _ in range(int(input())):
    input()
    nums = [int(_) for _ in input().split()]
    if even_sum(nums) > odd_sum(nums):
        print("YES")
    else: print("NO")