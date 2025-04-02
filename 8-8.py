import sys
input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [1_0001] * (m + 1)

dp[0] = 0
for i in range(n):
    coin = coins[i]

    for j in range(coin, m + 1):
        dp[j] = min(dp[j], dp[j - coin] + 1)

if dp[m] == 10_001:
    print(-1)
else:
    print(dp[m])

print(dp)