import sys


input = lambda: sys.stdin.readline().rstrip()


nums = input()

result = int(nums[0])

for char in nums[1:]:
    num = int(char)
    
    if result <= 1 or num <= 1:
        result += num
    else:
        result *= num

print(result)