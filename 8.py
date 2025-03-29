from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x: int, y: int):
    queue = deque([(x, y)])
    
    while queue:
        x, y = queue.popleft()

        # 상하좌우
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 공간 벗어남
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 진행 불가 구역(벽, 0)
            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n - 1][m - 1]

print(bfs(0, 0))