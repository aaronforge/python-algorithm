# N = 배열 크기, M = 연산 횟수, K = 하나의 숫자를 연속으로 사용할 수 있는 횟수
n, m, k = map(int, input().split())

data = list(map(int, input().split()))
data.sort()

# 가장 큰 수와 두번째로 큰 수
first = data[-1]
second = data[-2]

# 각 숫자의 반복 수(수열의 반복 수 * k + 수열 반복 후 나머지 수)
first_repeat_count = m // (k + 1) * k + m % (k + 1)
second_repeat_count = m - first_repeat_count

result = (first * first_repeat_count) + (second_repeat_count * second)

print(result)
