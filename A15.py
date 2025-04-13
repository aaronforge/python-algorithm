from collections import deque

# n = 노드 수, m = 간선 수, k = 최단 거리 목표, x = 출발 노드
n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    # a -> b 연결 정보(거리는 1 고정이라 Pass)
    a, b = map(int, input().split())

    graph[a].append(b)

# 각 노드별 출발 노드로 부터의 최단 거리
distances = [-1] * (n + 1)

# 출발 노드
distances[x] = 0

queue = deque([x])
while queue:
    now = queue.popleft()
    
    for next_node in graph[now]:
        if distances[next_node] == -1:
            distances[next_node] = distances[now] + 1
            queue.append(next_node)

has_city = False

for i in range(1, len(distances)):
    if distances[i] == k:
        print(i)
        has_city = True

if not has_city:
    print(-1)