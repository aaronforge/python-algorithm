import sys


input = lambda: sys.stdin.readline().rstrip()


# 멤버 수
n = int(input())

# 멤버 공포도 목록
users = list(map(int, input().split()))
users.sort()

# 결과
result = 0

# 현재 그룹 인원
current_member_count = 0

for fear_score in users:
    # 현재 그룹에 인원 추가
    current_member_count += 1

    # 현재 그룹 포함 인원 수가 현재 공포도 이상 -> 그룹 생성
    if current_member_count >= fear_score:
        result += 1
        current_member_count = 0


print(result)

