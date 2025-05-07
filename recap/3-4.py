n, k = map(int, input().split())

result = 0

while n >= k:
    # 나눈 몫에 k를 곱하면 최대 배수
    target = (n // k) * k
    result += (n - target)
    n = target

    result += 1
    n //= k

result += (n - 1)

print(result)