from collections import deque
from sys import stdin

input = stdin.readline

n, m = map(int, input().strip().split())
graph = [list(map(int, input().strip())) for _ in range(n)]

# 상하좌우 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x: int, y: int):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        
        # 상하좌우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 영역 벗어남
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 진행 불가(괴물 있음)
            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                # 해당 영역 첫 방문 시 거리 등록
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    
    return graph[n - 1][m - 1]

# 무조건 1,1 => 0, 0 에서 시작함
print(bfs(0, 0))