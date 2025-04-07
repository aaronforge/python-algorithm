import sys


input = lambda: sys.stdin.readline().rstrip()


# Root 찾기
def get_root(parents: list[int], x: int):
    if parents[x] != x:
        parents[x] = get_root(parents, parents[x])
    
    return parents[x]


def union_parent(parents: list[int], a: int, b: int):
    a = get_root(parents, a)
    b = get_root(parents, b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b


# n = 노드 수, m = 간선 수
n, m = map(int, input().split())

# 부모 테이블
parents = [0] * (n + 1)

# 노드 연결 비용
edges = []

# 결과
result = 0

# Root를 자기 자신으로 초기화
for i in range(1, n + 1):
    parents[i] = i

# 노드 사이 비용 입력
for _ in range(m):
    a, b, c = map(int, input().split())

    # A <-> B 노드 비용은 C
    edges.append((c, a, b))

# 비용 오름차순 정렬
edges.sort()

# 가장 비싼 비용
most_expensive = 0

for cost, a, b in edges:
    # 사이클 발생 X
    if get_root(parents, a) != get_root(parents, b):
        union_parent(parents, a, b)
        result += cost

        # 오름차순 정렬 했기 때문
        most_expensive = cost

# 전체 비용에서 가장 비싼 간선 비용을 빼서 끊어버리면 됨
print(result - most_expensive)