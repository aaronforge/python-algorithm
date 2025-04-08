import sys


input = lambda: sys.stdin.readline().rstrip()


n = int(input())

coins = list(map(int, input().split()))

coins.sort()

now = 1

for coin in coins:
    if coin > now:
        break
    now += coin

print(now)