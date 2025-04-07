import sys
import copy
from collections import deque


input = lambda: sys.stdin.readline().rstrip()


# 과목 마지막 번호(1 <= n <= 500)
n = int(input())

# 진입차수 초기화
indegree = [0] * (n + 1)

# 강의 시간
time = [0] * (n + 1)

# 그래프
graph = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    data = list(map(int, input().split()))

    time[i] = data[0]
    for x in data[1:-1]:
        # 진입 차수 초기화
        indegree[i] += 1
        graph[x].append(i)


# 위상 정렬
def topology_sort():
    result = copy.deepcopy(time)
    queue = deque()

    # 진입차수가 0인 노드 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)

    # 큐가 빌 때 까지 반복
    while queue:
        now = queue.popleft()

        for i in graph[now]:
            # 최대 시간
            result[i] = max(result[i], result[now] + time[i])

            # 진입 차수 빼기
            indegree[i] -= 1

            # 진입 차수 0이 되는 노드 Queue에 삽입
            if indegree[i] == 0:
                queue.append(i)
        
    for i in range(1, n + 1):
        print(result[i])

topology_sort()
