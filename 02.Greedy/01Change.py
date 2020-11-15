change = 1260
coin_count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    coin_count += change // coin
    change %= coin

print(coin_count)

# O(N) = the number of coin_types
