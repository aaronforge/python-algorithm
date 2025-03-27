import sys
input = sys.stdin.readline

coins = [500, 100, 50, 10]
count = 0

n = int(input())

for coin in coins:
    count += n // coin
    n %= coin
    
print(count)