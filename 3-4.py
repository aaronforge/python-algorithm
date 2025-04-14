n, m = map(int, input().split())

result = 0

while True:
    # 더이상 나눌 수 없음
    if n < m:
        # 현재의 N이 1이 될 때 까지 -1 연산이 필요함 -> n - 1이 연산 -1 필요한 수
        result += (n - 1)
        break

    # m으로 나누어 떨어지는 수
    target = (n // m) * m

    # target 까지 -1 연산 필요 수
    result += n - target

    # 이미 빼기 처리 완료 -> n 업데이트
    n = target
    
    # 나누기
    n //= m
    result += 1


print(result)