n, k = map(int, input().split())

cnt = 0

while n >= k:
    target = (n // k) * k
    cnt += n - target
    
    n = target
    n //= k
    cnt += 1

cnt += (n - 1)

print(cnt)