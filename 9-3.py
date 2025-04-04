import sys
input = lambda: sys.stdin.readline().rstrip()

INF = int(1e9)

# 노드 수
n = int(input())
# 간선 수
m = int(input())

# 그래프 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신 비용 초기화
for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    # A 노드 -> B 노드, 비용 C
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 최단거리 계산
for k in range(n + 1):
    for i in range(n + 1):
        for j in range(n + 1):
            # 점화식
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 결과 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        d = graph[i][j]

        if d == INF:
            print("INF", end=" ")
        else:
            print(d, end=" ")
    print()