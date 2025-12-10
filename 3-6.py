n, k = map(int, input().split())

result = 0

while True:
    # n이 k의 배수가 될 때 까지 -1 연산이 필요한 수
    target = (n // k) * k
    result += (n - target)

    n = target

    # n이 k 보다 작아 나눌 수 없는 경우
    if n < k:
        break

    # k의 배수 배수 나누기
    n //= k
    result += 1

# n이 1 초과인 경우 1이될 때 까지 빼기
result += (n - 1)

print(result)

# N = 17, K = 4
# 1. 17 - 1 = 16 
# 2. 16 / 4 = 4
# 3. 4 / 4 -> 1