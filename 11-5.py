import sys


input = lambda: sys.stdin.readline().rstrip()


n, m = map(int, input().split())
weights = list(map(int, input().split()))

# 무게별 갯수
count_by_weights = [0] * (m + 1)
for w in weights:
    count_by_weights[w] += 1

result = 0

for w in range(1, m + 1):
    n -= count_by_weights[w]
    result += count_by_weights[w] * n

print(result)
