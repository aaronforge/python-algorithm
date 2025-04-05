import sys
from collections import deque


input = lambda: sys.stdin.readline().rstrip()


# 노드 수, 간선 수
v, e = map(int, input().split())

# 모든 노드에 대한 진입차수 테이블
indegree = [0] * (v + 1)

# 그래프
graph = [[] for _ in range(v + 1)]

# 그래프 간선 정보 입력
for _ in range(e):
    a, b = map(int, input().split())

    # A -> B 이동 가능
    graph[a].append(b)

    # 진입 차수 더하기
    # A는 B로 갈 수 있으니 B의 진입 차수가 1개 생기는 것
    indegree[b] += 1

def topology_sort():
    result = []

    queue = deque()

    # 진입 차수가 0인 Node를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            queue.append(i)
    
    while queue:
        now = queue.pop()
        result.append(now)

        for i in graph[now]:
            # 진입 차수 -1
            indegree[i] -= 1

            # 진입차수 0인 Node Queue에 삽입
            if indegree[i] == 0:
                queue.append(i)
    
    for i in result:
        print(i, end=' ')

topology_sort()
