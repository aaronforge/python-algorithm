import heapq
import sys

input = lambda: sys.stdin.readline().rstrip()
INF = int(1e9)

# 노드 수, 간선 수
n, m = map(int, input().split())

# 시작 노드 번호
start = int(input())

# 그래프
graph = [[] for _ in range(m + 1)]
for _ in range(m):
    # A -> B 노드 연결, 비용 C
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 거리
distance = [INF] * (n + 1)

def dijkstra(start: int):
    queue = []

    # 시작 노드 비용 초기화
    distance[start] = 0
    # 우선순위 Queue 추가(비용 0, 시작 노드)
    heapq.heappush(queue, (0, start))

    while queue:
        current_cost, current_node = heapq.heappop(queue)

        # 현재 비용 보다 적은 비용으로 갈 수 있는 상태
        if distance[current_node] < current_cost:
            continue
        
        # 현재 노드 인접 노드 방문
        for next_node, next_cost in graph[current_node]:
            next_total_cost = current_cost + next_cost

            if next_total_cost < distance[next_node]:
                distance[next_node] = next_total_cost
                heapq.heappush(queue, (next_total_cost, next_node))


dijkstra(start)

for i in range(1, n + 1):
    cost = distance[i]

    if cost == INF:
        print("INF")
    else:
        print(cost)
