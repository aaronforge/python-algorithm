# 5 8 3
# 2 4 5 4 6
# ==> 46

# 6 6 6 5 / 6 6 6 5

# 7 7 2
# 1 2 3 4 5 6 7
# ==> 47
# 7 7 6 / 7 7 6 / 7

n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))
answer = 0

numbers.sort()
big = numbers[n - 1]
small = numbers[n - 2]

# 수열 길이 = k + 1
# 수열 반복 횟수 = m / 수열 길이
# 가장 큰 수 반복 수 = (수열 반복 횟수 * k) + 수열 반복 횟수의 나머지
# 두번째로 큰 수 반복 수 = m - 가장 큰 수 반복 수

bigCount = ((m // (k + 1)) * k) + (m % (k + 1))

answer += bigCount * big
answer += (m - bigCount) * small

print(answer)
