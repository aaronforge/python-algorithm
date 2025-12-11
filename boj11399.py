from itertools import accumulate

n = int(input())
arr = sorted(map(int, input().split()))

print(sum(accumulate(arr)))
