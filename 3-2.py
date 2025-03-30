import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

# 정렬
data.sort()

# 가장 큰 값
first = data[-1]
# 두번째로 큰 값
second = data[-2]

# 수열 반복 횟수
repeat_cnt = int(m / (k + 1))

# 가장 큰 수 반복 횟수(수열 반복 횟수 * k)
first_repeat_cnt = repeat_cnt * k
first_sum = first_repeat_cnt * first

# 두번째 수 반복 합
second_sum = repeat_cnt * second

result = first_sum + second_sum
print(result)