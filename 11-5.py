import sys


input = lambda: sys.stdin.readline().rstrip()


# N = 공의 수, M = 최대 무게
n, m = map(int, input().split())

# 볼링공별 무게
data = list(map(int, input().split()))

result = 0

for i in range(len(data)):
    for j in data[i:]:
        if data[i] != j:
            result += 1
        

print(result)
