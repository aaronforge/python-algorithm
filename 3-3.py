n, m = map(int, input().split())

result = 0

for _ in range(n):
    row = map(int, input().split())
    result = max(result, min(row))

print(result)