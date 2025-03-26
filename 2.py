n = int(input())

nums = list(map(int, input().split(' ')))
m = max(nums)
result = sum(nums) * 100 / m / n

print(result)