n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))
result = 0

numbers.sort()
first_biggest = numbers[n - 1]
second_biggest = numbers[n - 2]

max_count = int(m / (k + 1)) * k
max_count += m % (k + 1)

result += max_count * first_biggest
result += (m - max_count) * second_biggest

print(result)
