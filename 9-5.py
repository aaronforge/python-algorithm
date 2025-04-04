import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()

INF = int(1e9)

# 노드 수, 간선 수, 시작 노드
count_node, count_paths, start = map(int, input().split())

# 그래프
graph = [[] for _ in range(count_node + 1)]

# 거리
distances = [INF] * (count_node + 1)

# 노드 연결 정보
for _ in range(count_paths):
    node_a, node_b, node_distance = map(int, input().split())

    # 노드 A에 연결된 노드 정보를 (거리, 노드) 형태로 추가
    graph[node_a].append((node_distance, node_b))

# 다익스트라 알고리즘을 통한 최단 경로 계산
def dijkstra(start: int):
    queue = []

    # Heap Queue에 첫 노드를 (거리, 노드) 형태로 추가
    heapq.heappush(queue, (0, start))

    # 시작 노드 거리 초기화
    distances[start] = 0

    while queue:
        # 현재 시작 대상 노드
        current_distance, current_node = heapq.heappop(queue)

        # 현재 거리 보다 가까운 거리가 있음(진행 X)
        if distances[current_node] < current_distance:
            continue
            
        # 현재 노드에 연결된 노드
        for next_distance, next_node in graph[current_node]:
            # 현재 거리 + 연결 노드 거리 = 다음 노드 거리
            next_total_distance = current_distance + next_distance

            # 현재 계산된 다음 연결 노드 거리가 저장된 연결 노드 거리 보다 짧음 -> 갱신
            if next_total_distance < distances[next_node]:
                distances[next_node] = next_total_distance
                heapq.heappush(queue, (next_total_distance, next_node))

dijkstra(start)

# 도달 가능한 노드 수(시작 노드 제외 필요하여 -1로 시작)
count_reachable_node = -1

# 최대 거리
max_distance = 0

for distance in distances:
    if distance < INF:
        # 도달 가능 수 추가
        count_reachable_node += 1

        # 최대 거리 갱신
        max_distance = max(max_distance, distance)

print(count_reachable_node, max_distance)