import sys
input = lambda: sys.stdin.readline().rstrip()

INF = int(1e9)

# 노드 수, 간선 수
n, m = map(int, input().split())

# 그래프
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신 초기화
for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    i, j = map(int, input().split())

    # 양방향 거리는 모두 1
    graph[i][j] = 1
    graph[j][i] = 1

# 목표 노드, 방문 필요한 노드 노드
x, k = map(int, input().split())

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # 점화식 적용
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 시작점 -> K -> X 거리
result = graph[1][k] + graph[k][x]

# 도달 불가
if result >= INF:
    print(-1)
# 도달 가능
else:
    print(result)
