import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# 각 행의 가장 낮은 수 목록
numbers = []

for i in range(n):
    # 행 입력
    row = list(map(int, input().split()))

    # 가장 작은 수 추가
    numbers.append(min(row))

# 가장 큰 수 찾기
print(max(numbers))
