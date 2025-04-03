import sys
input = lambda: sys.stdin.readline().rstrip()

INF = int(1e9)

# 노드 수, 간선 수
n, m = map(int, input().split())

# 시작 노드
start = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    # A 노드 > B 노드, C 비용
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

visited = [False] * (n + 1)
distance = [INF] * (n + 1)

# 미방문 노드 중 최단 거리 노드 index
def get_next_node():
    min_value = INF
    index = 0

    for i in range(1, n + 1):
        can_visit = not visited[i]
        cost = distance[i]

        if can_visit and cost < min_value:
            min_value = cost
            index = i

    return index

# 다익스트라
def dijkstra(start: int):
    visited[start] = True
    distance[start] = 0

    # 첫 노드 > 연결 노드 비용 저장
    for node, cost in graph[start]:
        distance[node] = cost
    
    for _ in range(n - 1):
        # 다음 방문 노드
        now = get_next_node()
        visited[now] = True

        # 다음 방문 노드와 연결된 노드, 비용
        for connected_node, cost in graph[now]:
            # 연결된 노드의 현재 비용
            current_cost = distance[connected_node]
            # 연결된 노드의 새로 계산된 비용
            next_cost = distance[now] + cost

            # 새로 계산된 비용이 적은 경우 갱신
            if next_cost < current_cost:
                distance[connected_node] = next_cost

dijkstra(start)

for d in range(1, n + 1):
    cost = distance[d]
    if cost == INF:
        print("INF")
    else:
        print(cost)