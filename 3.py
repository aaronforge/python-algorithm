import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = map(int, input().split())
prefix_sum = [0]
tmp = 0

for num in numbers:
    tmp += num
    prefix_sum.append(tmp)

for _ in range(m):
    i, j = map(int, input().split())
    result = prefix_sum[j] - prefix_sum[i - 1]
    print(result)