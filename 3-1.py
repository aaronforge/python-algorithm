coins = [500, 100, 50, 10]
n = 1260 # 500x2, 100x2, 50x1, 10x1 => 6
count = 0

for coin in coins:
    count += n // coin
    n %= coin

print(count)