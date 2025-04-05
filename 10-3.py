import sys


input = lambda: sys.stdin.readline().rstrip()


# 특정 원소 Root 찾기(압축 기법)
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


# 노드 수 v, 간선 (union 연산) 수
v, e = map(int, input().split())

# 부모 테이블
parents = [0] * (v + 1)

# 부모 테이블 자기 자신 초기화
for i in range(1, v + 1):
    parents[i] = i

# union 연산 입력 및 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parents, a, b)

# 각 원소가 속한 집합
for i in range(1, v + 1):
    root = get_root(parents, i)
    print(root, end=" ")

print()

# 부모 테이블 내용 출력
print(" ".join(str(i) for i in parents[1:]))
