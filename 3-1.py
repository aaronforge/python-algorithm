coins = [500, 100, 50, 10]
n = 1260

result = 0

for coin in coins:
    result += n // coin
    n = n % coin

print(result, n)
