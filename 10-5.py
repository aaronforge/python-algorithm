import sys


input = lambda: sys.stdin.readline().rstrip()


# Root Node 찾기
def get_root(parents: list[int], x: int):
    if parents[x] != x:
        parents[x] = get_root(parents, parents[x])

    return parents[x]


# 같은 그룹으로 묶기
def union_parent(parents: list[int], a: int, b: int):
    a = get_root(parents, a)
    b = get_root(parents, b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b


# 노드 수, 간선(union 연산) 수
v, e = map(int, input().split())

# 부모 테이블
parents = [0] * (v + 1)

# 모든 간선 정보
edges = []

# 최종 비용
total_cost = 0

# 부모 테이블 본인으로 초기화
for i in range(1, v + 1):
    parents[i] = i

# 간선 정보 입력
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 비용 오름차순 정렬
edges.sort()

# 간선 확인
for edge in edges:
    cost, a, b = edge

    # Cycle 없음
    if get_root(parents, a) != get_root(parents, b):
        union_parent(parents, a, b)
        total_cost += cost

print(total_cost)