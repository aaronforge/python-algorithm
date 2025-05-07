n, m = map(int, input().split())

result = 0

for row in range(n):
    data = map(int, input().split())
    num = min(data)

    result = max(result, num)

print(result)
