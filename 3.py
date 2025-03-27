import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
prefix_sum = [0]

tmp = 0
for num in data:
    tmp += num
    prefix_sum.append(tmp)



for _ in range(m):
    i, j = map(int, input().split())

    range_sum = prefix_sum[j] - prefix_sum[i - 1]
    
    print(range_sum)