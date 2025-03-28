import sys

input = sys.stdin.readline

n, k = map(int, input().split())

# N이 1이 되어야 함
# 가능한 공식 => N - 1 또는 N / K(나머지가 무조건 0)

count = 0

while True:
    # n을 k의 배수로 만들기
    target = (n // k) * k
    
    # 배수가 될 때 까지는 1씩 빼줘야하기 때문에 연산 수가 1씩 증가함(그대로 더해버리기)
    count += (n - target)

    n = target

    # 더 이상 나눌 수 없는 상황
    if n < k:
        break

    # 나누기
    count += 1
    n //= k

# 더 이상 나눌 수 없어서 남은 나머지를 1로 만들기 위해 필요한 수 계산
count += (n - 1)
print(count)