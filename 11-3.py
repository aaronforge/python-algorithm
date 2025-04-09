import sys


input = lambda: sys.stdin.readline().rstrip()


s = input()

# 결과
result = 0

# 시작 숫자
k = int(s[0])

# 마지막 Index는 제외해도 됨
for i in range(len(s) - 1):
    # 현재 숫자
    current_num = int(s[i])

    # 다음 숫자
    next_num = int(s[i + 1])

    # 다음 숫자가 현재 숫자와 다르고 시작 숫자와 다름
    # -> 다음 번에 오는 숫자 쌍들 뒤집어야 함
    if current_num != next_num and next_num != k:
        result += 1

print(result)