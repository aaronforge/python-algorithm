import sys


input = lambda: sys.stdin.readline().rstrip()


# Root Node 찾기
def get_root(parents: list[int], x: int):
    if parents[x] != x:
        parents[x] = get_root(parents, parents[x])

    return parents[x]


# 두 원소가 속한 집합 합치기
def union_parent(parents: list[int], a: int, b: int):
    a = get_root(parents, a)
    b = get_root(parents, b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b


# v = 노드 수, e = 간선(union 연산) 수
v, e = map(int, input().split())

# 부모 테이블
parents = [0] * (v + 1)

# 부모 테이블 자기 자신 Node로 초기화
for i in range(1, v + 1):
    parents[i] = i

# 사이클 발생 유무
cycle = False

# 간선 입력 및 부모 Node 업데이트
for i in range(e):
    a, b = map(int, input().split())

    # Cycle 발생 시 종료
    if get_root(parents, a) == get_root(parents, b):
        cycle = True
        break
    else:
        union_parent(parents, a, b)

if cycle:
    print('Has Cycle')
else:
    print('No Cycle')