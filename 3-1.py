n = int(input())
coins = [500, 100, 50, 10]
count = 0


# 1260 -> 500 * 2, 100 * 2, 50 * 1, 10 * 1

for coin in coins:
    count += n // coin
    n %= coin


print(count)
