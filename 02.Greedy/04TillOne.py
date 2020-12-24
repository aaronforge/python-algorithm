n, k = map(int, input().split())
result = n
answer = 0

while result >= 1:
    if result == 1:
        break
    if result % k == 0:
        result /= k
    else:
        result -= 1
    answer += 1

print(answer)
