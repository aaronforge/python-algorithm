import sys


input = lambda: sys.stdin.readline().rstrip()


# n = 마지막 학생 번호, m = 연산의 개수
n, m = map(int, input().split())

# Root 테이블
parents = [0] * (n + 1)


# Root 찾기
def get_root(parents: list[int], x: int):
    if parents[x] != x:
        parents[x] = get_root(parents, parents[x])
    
    return parents[x]

# 두 원소가 속한 집합 합치기
def union_parents(parents: list[int], a: int, b: int):
    a = get_root(parents, a)
    b = get_root(parents, b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b


# 부모를 자기 자신으로 초기화
for i in range(n + 1):
    parents[i] = i

for _ in range(m):
    operator, a, b = map(int, input().split())

    if operator == 0:
        # 팀 합치기(union)
        union_parents(parents, a, b)
    elif operator == 1:
        # 같은 팀 여부 확인
        # 같은 팀이면 YES 아니면 NO 출력
        if parents[a] == parents[b]:
            print('YES')
        else:
            print('NO')
    # 이회 지원하지 않는 공식

