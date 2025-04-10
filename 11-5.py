import sys


input = lambda: sys.stdin.readline().rstrip()


n, m = map(int, input().split())
data = list(map(int, input().split()))

# 무게별 볼링공 수
weight_count = [0] * (m + 1)

for weight in data:
    weight_count[weight] += 1

result = 0

for i in range(1, m + 1): # 현재 무게 수 index
    for j in range(i + 1, m + 1): # 현재 무게 다음 무게 수 부터 index
        result += weight_count[i] * weight_count[j] # 경우의 수 구하기

print(result)
