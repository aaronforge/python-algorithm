import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())

dp = [0] * 100

data = list(map(int, input().split()))

dp[0] = data[0]
dp[1] = max(data[0], data[1])

for i in range(2, 4):
    dp[i] = max(dp[i - 1], dp[i - 2] + data[i])

print(dp[n - 1])
