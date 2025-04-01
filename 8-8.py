import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [10_001] * (m + 1)
dp[0] = 0

for coin in coins:
    for i in range(coin, m + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[m])
