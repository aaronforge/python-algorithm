n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

first = data[-1]
second = data[-2]

first_repeat = (k * m // (k + 1)) + m % (k + 1)

result = first * first_repeat + (m - first_repeat) * second

print(result)