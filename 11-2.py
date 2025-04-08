import sys
from functools import reduce


input = lambda: sys.stdin.readline().rstrip()

# 입력(string으로 받아야 함, 첫 자리가 0일 수 있음)
s = input()

# 최댓값 연산 선택해서 결과 업데이트
result = reduce(lambda x, y: max(x + int(y), x * int(y)), s, 0)

print(result)
