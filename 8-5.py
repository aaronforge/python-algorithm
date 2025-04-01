import sys
input = lambda: sys.stdin.readline().rstrip()

memo = [0] * 30_001

x = int(input())

# [0, 1, 2, 3, 4, 5, 6]
# [0, 0, 1, 1, 2, 1, 2]

for i in range(2, x + 1):
    # 현재의 수에서 1을 뺀 수의 연산 수에 +1회
    memo[i] = memo[i - 1] + 1

    if i % 2 == 0:
        # 현재 수에서 2로 나눈 몫까지 가는 최소 연산 수에 +1회
        memo[i] = min(memo[i], memo[i // 2] + 1)
    if i % 3 == 0:
        # 3
        memo[i] = min(memo[i], memo[i // 2] + 1)
    if i % 5 == 0:
        # 5
        memo[i] = min(memo[i], memo[i // 5] + 1)

print(memo[x])