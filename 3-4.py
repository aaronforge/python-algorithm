n, k = map(int, input().split())

result = 0

# 나눌 수 있을 때 까지 나누기(나누려는 수와 같거나 크면 됨)
while n >= k:
    while n % k != 0:
        # 나누어 떨어지지 않는 경우 -1
        n -= 1
        result += 1
    
    n //= k
    result += 1

# 1 이상 K 이하 남는 경우
while n > 1:
    n -= 1
    result += 1

print(result)
