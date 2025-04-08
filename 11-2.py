import sys


input = lambda: sys.stdin.readline().rstrip()

# 입력(string으로 받아야 함, 첫 자리가 0일 수 있음)
s = input()

# 결과 최댓값
result = 0

# 최댓값 연산 선택해서 결과 업데이트
for char in s:
    num = int(char)
    result = max(result + num, result * num)

print(result)
