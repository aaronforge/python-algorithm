import sys


input = lambda: sys.stdin.readline().rstrip()


# 모험가 수
n = int(input())

# 모험가 공포도
fears = list(map(int, input().split()))

# 그룹화를 위해 오름차순 정렬
fears.sort()

# 현재 그룹 멤버 수
group_count = 0

# 결과
result = 0

for fear in fears:
    group_count += 1

    if group_count >= fear:
        group_count = 0
        result += 1

print(result)