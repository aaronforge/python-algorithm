n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

count = 0
for c in coins[::-1]:
    count += k // c
    k %= c

print(count)
















































n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

result = 0

for c in coins[::-1]:
    result += k // c
    k %= c

print(result)
