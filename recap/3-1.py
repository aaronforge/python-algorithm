coins = [500, 100, 50, 10]
target = int(input())
result = 0

for c in coins:
    result += target // c
    target = target % c

print(result)
